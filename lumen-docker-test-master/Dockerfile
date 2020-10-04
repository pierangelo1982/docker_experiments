FROM debian:stable

MAINTAINER Attivi Digitali <>

RUN apt update

RUN apt install -y curl
# install php dependencies
RUN apt install -y php7.3-fpm php-opcache
RUN apt install -y php7.3-gd php7.3-mysqli php7.3-curl php7.3-json php7.3-phar php7.3-mbstring php7.3-xml php7.3-dom php7.3-xmlwriter php7.3-tokenizer

RUN apt -y install nginx
# installa composer
RUN curl -sS https://getcomposer.org/installer | php -- \
  --install-dir=/usr/bin --filename=composer

# copio nginx.conf in /etc/nginx/nginx.conf
#COPY ./nginx.conf /etc/nginx/nginx.conf

RUN rm -f /etc/nginx/site-available/default
# copio default.conf in /etc/nginx/conf.d/default.conf
COPY ./default.conf /etc/nginx/sites-available/default


# cancello index di default di nginx
RUN rm -rf /var/www/html/index.html

# copio il contenuto
COPY . /var/www/html

RUN chown -R www-data:www-data /var/www/html

WORKDIR /var/www/html

RUN composer install

RUN service php7.3-fpm restart

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]

