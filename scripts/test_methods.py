import check_methods
import sys
import MySQLdb

def do_all():
    db = MySQLdb.connect('10.192.0.5','root','fengmao','cp')
    cursor = db.cursor()
    sql = 'select phase from bingo where index_id > 5'
    cursor.execute(sql)
    querelist = cursor.fetchall()
    ch = check_methods.lotCheck()
    for (phase,) in querelist:
        print ch.getLast5Red(phase)

def do_one(phase):
    




switch = sys.argv[1]
if switch == 0:
