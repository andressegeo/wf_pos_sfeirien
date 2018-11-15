#coding: utf8
from flask import abort
import logging
from . import connect_db
from google.appengine.api import users, mail, app_identity
from datetime import datetime

def get_all_process():
    user = users.get_current_user()
    print user
    try:
        items = []
        cursor, con = connect_db.connect()
        query = u"SELECT * FROM process"
        cursor.execute(query)
        for row in cursor.fetchall():
            items.append({
                        u"id": row[0],
                        u"email_sfr": row[1],
                        u"email_com": row[2],
                        u"email_tl": row[3],
                        u"skills": row[4],
                        u"customer": row[5],
                        u"status": row[6]
                    })
        con.commit()
        return items
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8')))
    


def update_process(id_process, new_status):
    try:
        #items = {}
        cursor, con = connect_db.connect()
        query = "UPDATE process SET status = "+ str(new_status) + " WHERE id = " +str(id_process) +""
        print query
        cursor.execute(query)
        con.commit()
        return 1
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8')))
        return 0
    

def send(recipient, sender, subject, body):
    isHTML=True
    print("recep: "+recipient)
    logging.debug(u'Sending mail {} to {}'.format(subject, unicode(recipient)).encode(u'utf-8'))

    message = mail.EmailMessage(
        sender=sender,
        subject=subject,
        to=recipient
    )

    if isHTML:
        message.html = body
    else:
        message.body = body

    message.check_initialized()
    message.send()