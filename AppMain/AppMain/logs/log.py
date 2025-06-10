from loguru import logger

logger = logger
logger.add('AppMain/logs/debug.log',
           format="{time} - {level} - {message}",
           level="INFO",  # Заглавными буквами!
           rotation="10 MB"
           )


# logger.debug('Уровень DEBUG')
# logger.info('Уровень INFO')
# logger.warning('Уровень WARNING')
# logger.error('Уровень ERROR')
# logger.critical('Уровень CRITICAL')



