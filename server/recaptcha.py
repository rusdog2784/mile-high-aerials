import os
import logging

from google.cloud import recaptchaenterprise_v1
from google.cloud.recaptchaenterprise_v1 import Assessment
from google.cloud.recaptchaenterprise_v1.types import recaptchaenterprise


logger = logging.getLogger(__name__)


def set_GOOGLE_APPLICATION_CREDENTIALS_environment_variable():
    """Set the environment variable for the Google Cloud service account key file."""
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './server-sa.json'


def get_captcha_assessment_results(token, recaptcha_key):
    """Verify the reCAPTCHA token and return the recaptcha results.
    
    reCAPTCHA V3 Google Documentation:
    https://cloud.google.com/recaptcha/docs/create-assessment-website
    
    Args:
        token (str): The reCAPTCHA token.
        recaptcha_key (str): The reCAPTCHA site key.
    
    Returns:
        dict: The assessment name ('assessment_name'), risk score ('score'), 
            and reasons ('reasons').
    
    Raises:
        Exception: If the token is invalid or the action attribute 
            in the reCAPTCHA tag does not match the action you are 
            expecting to score.
    """
    project_id = "mile-high-aerials"
    recaptcha_action = 'contact_form'
    
    client = recaptchaenterprise_v1.RecaptchaEnterpriseServiceClient()
    
    # Set the properties of the event to be tracked.
    event = recaptchaenterprise_v1.Event()
    event.site_key = recaptcha_key
    event.token = token
    
    assessment = Assessment()
    assessment.event = event
    
    project_name = f"projects/{project_id}"
    
    # Build the assessment request.
    assessment_request = recaptchaenterprise_v1.CreateAssessmentRequest()
    assessment_request.assessment = assessment
    assessment_request.parent = project_name
    
    response: recaptchaenterprise.Assessment = client.create_assessment(
        assessment_request
    )
    """
    Main `recaptchaenterprise.Assessment` Properties:
        name: The unique assessment id for the assessment.
        
        event.expectedAction: the expected action from a user that you 
            specified when creating the assessment.
        
        token_properties.valid: indicates whether the provided user response
            token is valid. When valid = false, the reason is specified in 
            invalidReason. valid = false can also indicate that a user has 
            failed to solve a challenge or there is a siteKey mismatch.
        token_properties.invalidReason: Reason associated with the response 
            when valid = false.
        token_properties.action: a user interaction that triggered reCAPTCHA 
            verification.
        
        risk_analysis.score: level of risk the user interaction poses.
        risk_analysis.reasons: additional information about how reCAPTCHA 
            has interpreted the user interaction.
    """
    
    # Check if the token is valid.
    if not response.token_properties.valid:
        logger.error(
            "The CreateAssessment call failed because the token was "
            + "invalid for the following reasons: "
            + str(response.token_properties.invalid_reason)
        )
        raise Exception("The token is invalid")

    # Check if the expected action was executed.
    if response.token_properties.action != recaptcha_action:
        logger.error(
            "The action attribute in your reCAPTCHA tag does "
            + "not match the action you are expecting to score"
        )
        raise Exception(
            "The action attribute in your reCAPTCHA tag does "
            + "not match the action you are expecting to score"
        )
    else:
        assessment_name = client.parse_assessment_path(response.name).get("assessment")
        assessment_results = {
            'assessment_name': str(assessment_name),
            'score': float(response.risk_analysis.score),
            'reasons': [str(reason) for reason in response.risk_analysis.reasons]
        }
        logger.debug(
            f"Returning risk analysis results for assessment "
            + f"'{assessment_name}': {assessment_results}"
        )
        return assessment_results
