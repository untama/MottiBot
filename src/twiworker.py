#! /usr/bin/python
# -*- encoding: utf-8 -*-

import datetime
import locale
import logging
import logging.config
import twython
from twioauth import TwitterOauth

logging.config.fileConfig('../conf/log_conf.ini')
logger = logging.getLogger(__name__)

def tweet_image(filename):
    logger.info('START')
    logger.debug('filename=' + filename)

    result = True
    oauth = TwitterOauth()

    api = twython.Twython(oauth.oauths[TwitterOauth.CONSUMER_KEY],
                          oauth.oauths[TwitterOauth.CONSUMER_SECRET],
                          oauth.oauths[TwitterOauth.ACCESS_TOKEN],
                          oauth.oauths[TwitterOauth.ACCESS_TOKEN_SECRET])

    try:
        with open(filename, 'rb') as tweet_image:
            now = datetime.datetime.today()
            locale.setlocale(locale.LC_ALL, ('ja_JP', 'UTF-8'))
            tweet_time = now.strftime('%x(%a) %X')
            logger.debug('tweet_time=' + tweet_time)

            try:
                media_status = api.upload_media(media=tweet_image)
                logger.debug('media_status[]=' + str(media_status))
                api.update_status(media_ids=[media_status['media_id']],
                                  status=str(tweet_time) + 'の様子です。')
            except twython.TwythonError as ex:
                logger.exception(ex)
                result = False

    except IOError as ex:
        logger.exception(ex)
        result = False

    logger.info('END')
    return result

def main():
    tweet_image('../img/image.jpg')

if __name__ == '__main__':
    main()

