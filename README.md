# Mile High Aerials Website
Repository for containing my public website for my drone business, Mile High Aerials. This is my attempt to replace Squarespace and Wix because ~$16 to $18 per month is WAYYY too much.


## Client
- This is a simple, static website that just uses HTML, CSS, and Javascript.
- I've dockerized it using the Chainguard Nginx image and a custom configuration file, which I'm "appending" to the `/etc/nginx/conf.d` directory.
- It has Google reCAPTCHA v3 setup and configured inside the `contact.html` page. I am validating and assessing the reCAPTCHA token using this repo's server.


## Server
- This is a simple Flask server that is utilizing Flask-Limiter alongside a Redis server to rate limit requests to api endpoints (the limits are enforced on a remote_addr basis).
- In order to successfully authenticate and use Google reCAPTCHA v3, you need to download and place the mile-high-aerials-server service account key file inside the `keys` folder.


# All Together Now
- At the root of this repo is a docker compose file, which will deploy the client and server images from my personal Docker Hub account, `rusdog2784`, as well as a Redis server for rate limiting.
