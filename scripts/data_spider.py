#!/usr/bin/python

import urllib2
import re
import time
import MySQLdb


def spider(url):
    """parse the website"""
    fq = urllib2.urlopen(url)
    fq_cts = fq.read()
    #phase date
    fq_phase = re.findall("<span id=\"jq_short_openTime\">\d\d-\d\d</span>", fq_cts)
    if len(fq_phase) == 1:
        fq_phase_md = re.search("(\d\d-\d\d)",fq_phase[0])
        fq_phase_ymd = "%d-" % time.localtime().tm_year + fq_phase_md.group(0)
    else:
        print "find %d fq_phase, fq_phase: %r" % (len(fq_phase),fq_phase)

    #number list
    fq_result = re.findall("div id=\"jq_openResult\".*?\/div>", fq_cts, re.S)
    if len(fq_result) == 1:
        fq_list = re.findall("\d\d", fq_result[0])
        fq_num = [int(x) for x in fq_list]
    else:
        print "find %d number_list, numberlist: %r" %(len(fq_result), fq_list)

    #phase issue
    fq_issue = re.findall("<select id=\"jq_last10_issue_no\".*?</option>", fq_cts, re.S)
    if len(fq_issue) == 1:
        fq_issue_number = re.search("(\d\d\d\d\d)", fq_issue[0]).group(0)
    else:
        print "find %d fq_issue, fq_issue: %r" % (len(fq_issue), fq_issue)

    if len(fq_phase) == 1 and len(fq_result) == 1 and len(fq_issue) == 1:
        return [fq_phase_ymd, fq_num, fq_issue_number]



def tosql(numlist):
    host = '10.192.0.5'
    user = 'root'
    password = 'fengmao'
    port = '3306'
    database = 'cp'
    db = MySQLdb.connect(host,user,password,database)
    cursor = db.cursor()
    sql_insert = "insert into cp.bingo ( phase,releasedate,r1,r2,r3,r4,r5,b1,b2) \
                  values (\"%s\",\"%s\",%s,%s,%s,%s,%s,%s,%s);"                  \
                 % (numlist[2], numlist[0], numlist[1][0], numlist[1][1], numlist[1][2], numlist[1][3], numlist[1][4], numlist[1][5], numlist[1][6])
    cursor.execute('select count(*) from cp.bingo where phase=\'%s\'' % (numlist[2]))
    (check_num,) = cursor.fetchone()
    print str(check_num)
    if int(check_num) == 0:
        cursor.execute(sql_insert)
        db.commit()
        print "update successfully!"
    else:
        print "this issue is in database, no action needed!"




url = "http://sina.aicai.com/kaijiang/tcdlt/"
data_receive = spider(url)
print data_receive
tosql(data_receive)
