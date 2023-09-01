""" Constants """

import os
import logging

LOG_LEVEL = logging.INFO
if os.getenv('log.level') == 'DEBUG':
    LOG_LEVEL = logging.DEBUG
elif os.getenv('log.level') == 'WARNING':
    LOG_LEVEL = logging.WARNING
elif os.getenv('log.level') == 'ERROR':
    LOG_LEVEL = logging.ERROR
elif os.getenv('log.level') == 'CRITICAL':
    LOG_LEVEL = logging.CRITICAL

# Postgresql information
POSTGRESQL_USERNAME = os.getenv('user')
POSTGRESQL_PASSWORD = os.getenv('password')
POSTGRESQL_HOSTNAME = os.getenv('host')
POSTGRESQL_PORT = os.getenv('port')
POSTGRESQL_DB = os.getenv('dbname')

DB_DROP_ALL = os.getenv('db.drop_all')
