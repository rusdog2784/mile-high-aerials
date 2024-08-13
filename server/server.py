import os
import json
import logging

from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis

from recaptcha import (
    set_GOOGLE_APPLICATION_CREDENTIALS_environment_variable,
    get_captcha_assessment_results
)


# Set up the logging configuration.
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set the environment variable for the Google Cloud service account key file.
set_GOOGLE_APPLICATION_CREDENTIALS_environment_variable()

# Create the Flask app and enable CORS.
app = Flask(__name__)
cors = CORS(app, resources=r'/api/*')
limiter = Limiter(
    key_func=get_remote_address,
    app=app,
    default_limits=["2/second"],
    storage_uri="redis://redis:6379"
)

@app.errorhandler(429)
def ratelimit_handler(e):
    return make_response(
        jsonify(error=f"ratelimit exceeded {e.description}")
        , 429
    )


##############
### Routes ###
##############
@app.route("/ping", methods=["GET"])
@limiter.exempt
def ping():
    return jsonify({
        'message': "Hello, World!"
    }), 200


@app.route('/api/contact', methods=['POST'])
@limiter.limit("2/day")
def contact_form():
    data = request.get_json()
    logger.debug(f"Received the following data:\n{json.dumps(data, indent=2)}")
    
    # TODO: Add code to send automated email to me. Was looking into Mailtrap as 
    # they have a free tier offering 1,000 emails/month, 200 emails/day, 1 sending 
    # domain.
    
    return jsonify({'message': 'Form submitted successfully'})


@app.route('/api/recaptcha', methods=['POST'])
def recaptcha():
    data = request.get_json()
    
    try:
        recaptcha_results = get_captcha_assessment_results(data['token'], data['siteKey'])
    except Exception as e:
        # NOTE: For now, I'm going to default to accepting all form submissions.
        logger.error(f"reCAPTCHA Failed: {e}")
        return jsonify({
            'message': "reCAPTCHA assessment failed, but we are accepting all form submissions",
            'assessment_name': "N/A",
            'score': -1.0,
            'reasons': []
        }), 200
        # return jsonify({'error': str(e)}), 400

    assessment_name = recaptcha_results['assessment_name']
    score = recaptcha_results['score']
    reasons = recaptcha_results['reasons']
    
    return jsonify({
        'message': 'reCAPTCHA assessment completed successfully',
        'assessment_name': assessment_name,
        'score': score,
        'reasons': reasons
    }), 200
    

if __name__ == '__main__':
    debug = bool(int(os.environ.get('DEBUG', "0")))
    app.run(host="0.0.0.0", port=8080, debug=debug)
