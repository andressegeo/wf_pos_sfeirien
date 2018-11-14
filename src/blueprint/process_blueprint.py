#coding:utf8

from flask import Blueprint, request, json, jsonify, abort, render_template
from .utils_blueprint import flask_construct_response, flask_constructor_error
import logging
from ..api_db import process_db

PROCESS_API_BLUEPRINT = Blueprint(u'process_api', __name__)

@PROCESS_API_BLUEPRINT.route(u"/list", methods=[u'GET'])
def list_process():
    print "great"
    try:
        all_process = process_db.get_all_process()
        #print all_process
        return flask_construct_response({"Tous les process":all_process}, 200)
            
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8'))) 
        return flask_constructor_error(u"Not Found", 404, 404)


