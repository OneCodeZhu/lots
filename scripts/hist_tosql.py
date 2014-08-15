#!/usr/bin/python

import MySQLdb
host = '10.192.0.5'
user = 'root'
password = 'fexgmxo'
port = '3306'
database = 'cp'
db = MySQLdb.connect(host,user,password,database)
cursor = db.cursor()

path = '../hist_2007-01-01_2014-03-24.txt'
histd = open(path)

for line in histd:
    sql = "insert into cp.bingo ( phase,releasedate,r1,r2,r3,r4,r5,b1,b2) \
            values (\"%s\",\"%s\",%s,%s,%s,%s,%s,%s,%s);" %(line.split()[0],line.split()[2], line.split()[1].split(',')[0],\
            line.split()[1].split(',')[1],\
            line.split()[1].split(',')[2],\
            line.split()[1].split(',')[3],\
            line.split()[1].split(',')[4],\
            line.split()[1].split(',')[5],\
            line.split()[1].split(',')[6],\
            )
    print sql
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
db.close()
    
