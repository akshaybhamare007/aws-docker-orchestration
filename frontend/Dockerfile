# Use the official Nginx image as the base
FROM nginx:alpine

# Copy your local static website files to the Nginx html directory
COPY ./index.html /usr/share/nginx/html/index.html

# Copy the rulebook (This replaces the default Nginx routing rules)
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port 80 (optional, but documents the intent)
EXPOSE 80

