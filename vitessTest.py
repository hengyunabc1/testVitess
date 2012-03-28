import dbtest
from multiprocessing import Process
import time
from vtdb import vt_occ2 as vitessDb
import MySQLdb

def getVitessConn():
    conn = vitessDb.connect('localhost:6510', timeout=10000, dbname='mydb')
    return conn

def getMySQLdbConn():
    conn = MySQLdb.connect(host='172.16.1.35', user='testvitess',passwd='testvitess')
    conn.select_db('mydb')
    return conn

if __name__ == '__main__':
    totalInsertSize = 100000
    processNum = 10 

    dbtest.multiProcessInsert(getMySQLdbConn, totalInsertSize, processNum) 
    dbtest.multiProcessInsert(getVitessConn, totalInsertSize, processNum)
    totalSelectSize = 100000
    #the slect range
    start = 0
    end = totalInsertSize 
    dbtest.multiProcessSelect(getMySQLdbConn, start, end, totalSelectSize, processNum) 
    dbtest.multiProcessSelect(getVitessConn, start, end, totalSelectSize, processNum) 
    

