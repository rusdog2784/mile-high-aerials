# Start with Chainguard Nginx image
FROM cgr.dev/chainguard/nginx:latest

# Copy custom nginx files
COPY nginx/nginx.conf /etc/nginx/nginx.conf
COPY nginx/custom.default.conf /etc/nginx/conf.d/nginx.default.conf

# Copy HTML content
COPY 404.html /usr/share/nginx/html
COPY about.html /usr/share/nginx/html
COPY contact.html /usr/share/nginx/html
COPY index.html /usr/share/nginx/html
COPY styles.css /usr/share/nginx/html

# Copy images
COPY images/ /usr/share/nginx/html/images/

# Expose port 8080 as per Chainguard Nginx image
EXPOSE 8080
