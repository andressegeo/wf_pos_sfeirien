import MySQLdb
from config import CONFIG_DEV

"""
Modul who help to connect to database
"""
CONFIG = CONFIG_DEV
def connect():
    con = MySQLdb.connect(
        host = CONFIG[u'db'][u'host'],
        user = CONFIG[u'db'][u'user'],
        db = CONFIG[u'db'][u'database'],
        passwd = CONFIG[u'db'][u'password'],
        charset=u"utf8",
        use_unicode=True
    )
    cursor = con.cursor()
    return cursor, con
