import sys
import logging
from pythonjsonlogger import jsonlogger
from flask import Flask
from flask_cors import CORS, cross_origin
from apis import api

ROOT_LOGGER = logging.getLogger()
ROOT_LOGGER.setLevel(logging.DEBUG)
STREAM_HANDLER = logging.StreamHandler(sys.stdout)
# FORMATTER = jsonlogger.JsonFormatter(fmt='%(asctime)s %(levelname)s %(module)s %(message)s')
# STREAM_HANDLER.setFormatter(FORMATTER)
ROOT_LOGGER.addHandler(STREAM_HANDLER)

app = Flask(__name__)
CORS(app)

api.init_app(app)

if __name__ == '__main__':
    logging.info('listening port 5001')
    app.run(host='0.0.0.0', port=5001)
