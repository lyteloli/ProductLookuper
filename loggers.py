from logging.handlers import RotatingFileHandler
import logging

logging.basicConfig(format='|%(asctime)s| %(name)s->%(levelname)s:\t%(message)s', datefmt='%d-%m-%y %H:%M',
                    level=logging.INFO)
console = logging.StreamHandler()  # Init console logging
formatter = logging.Formatter('|%(asctime)s| %(name)s->%(levelname)s:\t%(message)s', datefmt='%d-%m-%y %H:%M')
console.setFormatter(formatter)  # Set console formatting

main_logger = logging.getLogger('')
main_logger.addHandler(console)  # Attach console to the logger
main_logger.addHandler(RotatingFileHandler('log.log', maxBytes=10000000))
