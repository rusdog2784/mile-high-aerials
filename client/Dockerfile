# Start with Chainguard Nginx image
FROM cgr.dev/chainguard/nginx:latest-dev

# Copy custom default configuration for Nginx
COPY nginx/local.default.conf /etc/nginx/conf.d/nginx.default.conf

# Copy HTML content
COPY 404.html /usr/share/nginx/html
COPY about.html /usr/share/nginx/html
COPY contact.html /usr/share/nginx/html
COPY index.html /usr/share/nginx/html
COPY styles.css /usr/share/nginx/html

# Copy images
COPY images/ /usr/share/nginx/html/images/

# Set read-only permissions for the /usr/share/nginx/html/images directory
USER root
RUN chmod 555 /usr/share/nginx/html/images/
RUN chmod 444 /usr/share/nginx/html/images/*
USER nginx

# Expose port 8080 as per Chainguard Nginx image
EXPOSE 8080
