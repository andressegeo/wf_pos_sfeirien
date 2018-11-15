#coding:utf8

from flask import Blueprint, request, json, jsonify, abort, render_template
from .utils_blueprint import flask_construct_response, flask_constructor_error
import logging
from ..api_db import process_db

PROCESS_API_BLUEPRINT = Blueprint(u'process_api', __name__)

#This method as her name indicates allow to list all the process includes in the database
@PROCESS_API_BLUEPRINT.route(u"/list", methods=[u'GET'])
def list_process():
    print "great"
    try:
        all_process = process_db.get_all_process()
        #print all_process
        return flask_construct_response({"Tous les process":all_process})
            
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8'))) 
        return flask_constructor_error(u"Not Found", 404, 404)

#This method allow to update status's process and sendmail to the recipients
@PROCESS_API_BLUEPRINT.route(u"/sendmail", methods=[u'POST'])
def update_process():
    payload = json.loads(request.data)
    try:
        if set((u"mail", u"id", u"status")) <= set(payload.keys()):
            """check status update in database and send mail to the recipient""" 
            try:
                if payload.get("id"):
                    id_process = payload[u"id"]
                    new_status = payload[u"status"]


                    """ Send mail parameters """
                    sender = payload[u"mail"][u"sender"]
                    recipient = payload[u"mail"][u"recipient"]
                    subject = payload[u"mail"][u"subject"]
                    body = payload[u"mail"][u"body"]

                    check = process_db.update_process(id_process, new_status)
                    print "check is: {}".format(check)
                    if check == 1:
                        print "edit sucess"
                        process_db.send(recipient, sender,  subject, body)
                        return flask_construct_response({"response":"mail send"}, 200)
                    else:
                        print "edit failed"
                        return flask_constructor_error(u"Failled to update db", 404, 404)
            except BaseException as e:
                logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8')))
        else:
            return flask_constructor_error(u"expected elements or check your keys elements", 400, 400)
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8')))
        return flask_constructor_error(u"Not Found", 404, 404)
