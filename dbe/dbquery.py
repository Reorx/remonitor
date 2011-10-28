import MySQLdb as db

DB_INFO = [
    'localhost',
    'remote',
    'pilved',
    'nmadmin'
]


def execute(exp):
    try:
        data = {}
        conn = db.connect(*DB_INFO)
        cursor = conn.cursor()

        cursor.execute(exp)
        #print dir(cursor)

        data['q_rows'] = cursor.fetchmany()

        data['q_head'] = tuple([i[0] for i in cursor.description])

        cursor.close()
        conn.close()
        
    except db.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        return None

    return data
