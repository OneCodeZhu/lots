#!/usr/bin/python

import MySQLdb

class lotCheck():
    def __init__(self):
        """init to connect the database """
        self.host = '10.192.0.5'
        self.user = 'root'
        self.password = 'fengmao'
        self.port = '3306'
        self.database = 'cp'
        self.db = MySQLdb.connect(self.host,self.user,self.password,self.database)
        self.cursor = self.db.cursor()
        self.onshoot = {-1:0, -2:0, -3:0, -4:0, -5:0}

    
    def getCurIndex(self,phase):
        """get current phase index_id"""
        sql_index_id = "select index_id from bingo where phase=%s;" % phase
        self.cursor.execute(sql_index_id)
        (cur_index_id,) = self.cursor.fetchone()
        return cur_index_id
    def getLast5Red(self,phase):
        """get last five issue red ball"""
        sql = "select * from bingo where index_id < (select index_id from bingo where phase=%s) order by index_id desc limit 5;" % phase
        cur_index = self.getCurIndex(phase)
        last5red = {}
        self.cursor.execute(sql)
        last5tuple = self.cursor.fetchall()
        for one in last5tuple:
            last5red[int(one[9]) - int(cur_index)] = one[2:7]
        return last5red
    def getLast5Blue(self,phase):
        """get last five issue blue ball"""
        sql = "select * from bingo where index_id < (select index_id from bingo where phase=%s) order by index_id desc limit 5;" % phase
        cur_index = lotCheck.getCurIndex(self,phase)
        last5blue = {}
        self.cursor.execute(sql)
        for one in self.cursor.fetchall():
            last5blue[int(one[9]) - int(cur_index)] = one[7:9]
        return last5blue
    def getCurRed(self,phase):
        """get current red data"""
        sql_phase = "select r1,r2,r3,r4,r5 from bingo where phase=%s;" % phase
        self.cursor.execute(sql_phase)
        fetch_cur_red = self.cursor.fetchone()
        currentred = [int(x) for x in fetch_cur_red]
        return currentred
    def getCurBlue(self,phase):
        """get current blue data"""
        sql_phase = "select b1,b2 from bingo where phase=%s;" % phase
        self.cursor.execute(sql_phase)
        fetch_cur_blue = self.cursor.fetchone()
        currentblue = [int(x) for x in fetch_cur_blue]
        return currentblue
    def getLast5Index(self,phase):
        """get last 5 issues' index_id"""
        sql_index = "select index_id from bingo where index_id < (select index_id from bingo where phase=%s) order by index_id desc limit 5;" % phase
        last5_index = []
        self.cursor.execute(sql_index)
        for (one,) in self.cursor.fetchall():
            last5_index.append(int(one))
        return last5_index
        






    def Yushuhe(self,phase):
        """e.g. 1 11 19 24 33 ,the result will be 1 + 11 % 10 + 19 %10 + 24 % 10 + 33 %10 = 18"""

        #get current phase index_id
        sql_index_id = "select index_id from bingo where phase=%s;" % phase
        self.cursor.execute(sql_index_id)
        (cur_index_id,) = self.cursor.fetchone()

        #get last five issue data
        sql = "select * from bingo where index_id < (select index_id from bingo where phase=%s) order by index_id desc limit 5;" % phase
        self.cursor.execute(sql)
        dict5 = {}
        for one in self.cursor.fetchall():
            sum_of_remainder = 0
            for i in range(2,7):
                sum_of_remainder += one[i] % 10
            dict5[one[0]] = [sum_of_remainder, one[9] - int(cur_index_id)]

        #get current issue data
        sql_phase = "select r1,r2,r3,r4,r5 id from bingo where phase=%s;" % phase
        self.cursor.execute(sql_phase)
        fetch_cur_phase = self.cursor.fetchone()
        currentphase = [int(x) for x in fetch_cur_phase]
        for key in dict5.keys():
            if dict5[key][0] in currentphase:
                self.onshoot[dict5[key][1]] += 1
#        print self.onshoot

    def get_Yushuhe(self):
        print self.onshoot


