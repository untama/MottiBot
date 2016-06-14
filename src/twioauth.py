#! /usr/bin/python
# -*- encoding: utf-8 -*-

import logging
import logging.config
import ConfigParser

logging.config.fileConfig('../conf/log_conf.ini')
logger = logging.getLogger(__name__)

class TwitterOauth:
    INI_FILE_PATH = '../conf/twitter_oauth.ini'

    CONSUMER_KEY = 'ConsumerKey'
    CONSUMER_SECRET = 'ConsumerSecret'
    ACCESS_TOKEN = 'AccessToken'
    ACCESS_TOKEN_SECRET = 'AccessTokenSecret'

    def __init__(self):
       logger.info('START')

       self.__oauths = {}

       keys = [TwitterOauth.CONSUMER_KEY, TwitterOauth.CONSUMER_SECRET,
               TwitterOauth.ACCESS_TOKEN, TwitterOauth.ACCESS_TOKEN_SECRET]

       try:
           ini_file = ConfigParser.SafeConfigParser()
           ini_file.read(TwitterOauth.INI_FILE_PATH)

           for key in keys:
               self.__oauths[key] = ini_file.get('OAuth', key)
               logger.debug(key + '=' + self.__oauths[key])
       except ConfigParser.Error as ex:
           logger.exception(ex)
 
       logger.info('END')

    def get_oauths(self):
        return self.__oauths

    oauths = property(get_oauths)

def main():
    oauth = TwitterOauth()

    print(oauth.oauths[TwitterOauth.CONSUMER_KEY])
    print(oauth.oauths[TwitterOauth.CONSUMER_SECRET])
    print(oauth.oauths[TwitterOauth.ACCESS_TOKEN])
    print(oauth.oauths[TwitterOauth.ACCESS_TOKEN_SECRET])

if __name__ == '__main__':
    main()
 
