#! /usr/bin/python
# -*- encoding: utf-8 -*-

import logging
import logging.config
import picamera

logging.config.fileConfig('../conf/log_conf.ini')
logger = logging.getLogger(__name__)

def take_picture(filename):
    logger.info('START')
    logger.debug('filename=' + filename)

    result = True

    try:
        with picamera.PiCamera() as camera:
            camera.capture(filename)
    except (picamera.exc.PiCameraWarning, picamera.exc.PiCameraError) as ex:
        logger.exception(ex)
        result = False

    logger.info('END')
    return result

def main():
    take_picture('../img/image.jpg')

if __name__ == '__main__':
    main()

