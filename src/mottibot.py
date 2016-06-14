#! /usr/bin/python
# -*- encoding: utf-8 -*-

import logging
import logging.config
from camworker import take_picture
from twiworker import tweet_image

logging.config.fileConfig('../conf/log_conf.ini')
logger = logging.getLogger(__name__)

logger.info('START')

if take_picture('../img/image.jpg'):
    tweet_image('../img/image.jpg')

logger.info("END")
