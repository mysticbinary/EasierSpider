import pymysql
import tools.common as com

def getconn(dbname):

    conf = com.jsonToDict("/config/mysql.conf")
    conf = conf[dbname]

    db = pymysql.connect(charset='utf8', host=conf['host'], \
                         user=conf['user'], \
                         passwd=conf['password'], \
                         db=conf['database'], \
                         port=conf['port'])
    return db
