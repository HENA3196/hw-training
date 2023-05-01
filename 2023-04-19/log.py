import logging

# logging.warning('Watch out!')


# FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
# logging.basicConfig(format=FORMAT)
# d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
# logger = logging.getLogger('tcpserver')
# logger.warning('Protocol problem: %s', 'connection reset', extra=d)



import logging

# Configure the logging module
logging.basicConfig(filename='example.log', level=logging.DEBUG)

# Log a message with the DEBUG level
logging.debug('This is a debug message')

# Log a message with the INFO level
logging.info('This is an info message')

# Log a message with the WARNING level
logging.warning('This is a warning message')

# Log a message with the ERROR level
logging.error('This is an error message')

# Log a message with the CRITICAL level
logging.critical('This is a critical message')
