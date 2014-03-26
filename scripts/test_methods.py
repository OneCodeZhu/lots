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
    ch = check_methods.lotCheck()
    print ch.getLast5Index(phase)




switch = int(sys.argv[1])
if switch == 0:
    do_all()
elif switch == 1:
    if sys.argv[2]:
        do_one(sys.argv[2])
    else:
        print "worng param numbers!!!"
else:
    print "the first param be 1 or 0!!!"
