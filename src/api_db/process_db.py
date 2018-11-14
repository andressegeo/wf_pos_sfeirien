#coding: utf8
from flask import abort
from google.appengine.api import users
import logging
from . import connect_db

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
    except BaseException as e:
        logging.error(u'Error: {}'.format(unicode(e).encode(u'utf-8')))
    return items 