FROM nginx:latest

# remove default config
RUN rm /etc/nginx/conf.d/default.conf

#copy custom config
COPY nginx.conf /etc/nginx/nginx.conf
