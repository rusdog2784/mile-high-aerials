# Start with Chainguard Nginx image
FROM cgr.dev/chainguard/nginx:latest-dev

# Copy custom nginx files
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/local.default.conf /etc/nginx/conf.d/nginx.default.conf

# Copy HTML content
COPY 404.html /usr/share/nginx/html
COPY about.html /usr/share/nginx/html
COPY contact.html /usr/share/nginx/html
COPY index.html /usr/share/nginx/html
COPY styles.css /usr/share/nginx/html

# Copy images
COPY images/ /usr/share/nginx/html/images/

# Set permissions for extra nginx-specific directories and files
USER root
RUN chown -R nginx:nginx /usr/share/nginx/html/images/
RUN touch /var/log/nginx/mile-high-aerials.access.log
RUN touch /var/log/nginx/mile-high-aerials.error.log
RUN chown -R nginx:nginx /var/log/nginx/
USER nginx

# Expose port 8080 as per Chainguard Nginx image
EXPOSE 8080
