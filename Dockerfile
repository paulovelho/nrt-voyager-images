FROM php:7.4-apache

COPY ./apache/site.conf /etc/apache2/sites-available/000-default.conf

RUN mkdir /var/www/app

RUN rm /etc/apache2/sites-enabled/000-default.conf

RUN apt-get update -y \
	&& apt-get install -y libpng-dev \
		libfreetype6-dev \
		libwebp-dev \
		libjpeg62-turbo-dev

RUN docker-php-ext-install gd \
	&& docker-php-ext-configure gd \
		--with-jpeg \
    && docker-php-ext-install -j$(nproc) gd
RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli


RUN a2enmod rewrite
RUN a2enmod ssl
RUN a2ensite 000-default.conf

RUN service apache2 restart



RUN chown -R www-data:www-data /var/www


EXPOSE 80
EXPOSE 443
