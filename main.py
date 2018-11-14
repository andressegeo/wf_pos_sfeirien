# coding: utf-8
from flask import Flask

from config import CONFIG
from src.utils import init_logger
from src.blueprint import PROCESS_API_BLUEPRINT

logging_config = CONFIG[u"logging"]
init_logger(logging_config[u'pattern'], logging_config[u'pattern_debug'], logging_config[u"level"])


# create flask server
APP = Flask(__name__)
APP.debug = CONFIG[u"app"][u"debug"]
APP.register_blueprint(PROCESS_API_BLUEPRINT, url_prefix = u'/api/process')

if __name__ == u"__main__":
    APP.run(threaded=True, port=5000, debug=True)
