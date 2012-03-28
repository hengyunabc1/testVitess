import MySQLdb
import datetime
import random
from multiprocessing import Process

def getSeconds(startTime):
    seconds = (datetime.datetime.now() - startTime).seconds
    if seconds == 0:
        seconds = 1
    return seconds
 
def insert(conn, size):
    insertSql = 'insert into mytable(u, pw)  values(\'test\', \'test\')'
    curs = conn.cursor()
    i = 0
    while i < size:
        conn.begin()
        curs.execute(insertSql)
        conn.commit()
        i = i + 1

def mutilProcessInsert(getConnFunc, totalSize, processNum):
    i = 0
    insertSize = totalSize/processNum
    print 'per Process insertSize:', insertSize
    processList = list()
    while i < processNum:
        i = i + 1
        p = Process(target=insert, args=(getConnFunc(), insertSize))
        processList.append(p)

    startTime = datetime.datetime.now()
#    print 'startTime:', startTime
    for p in processList:
        p.start()

    for p in processList:
        p.join()

    print 'mutilProcessInsert,totalsize:', totalSize, ',processNum:', processNum
    print 'size/s:', totalSize/float(getSeconds(startTime))

def mutilProcessSelect(getConnFunc, start, end, totalSelectSize, processNum):
    selectSize = totalSelectSize/processNum
    processList = list()
    i = 0
    while i < processNum:
        i = i + 1
        p = Process(target=select, args=(getConnFunc(), start, end, selectSize))
        processList.append(p)

    startTime = datetime.datetime.now()
#    print 'startTime:', startTime
    for p in processList:
        p.start()

    for p in processList:
        p.join()

    print 'mutilProcessSelect,totalsize:', totalSelectSize, ',processNum:', processNum
    print 'size/s:', totalSelectSize/float(getSeconds(startTime))

        
def select(conn, start, end, times):
    selectSql = 'select * from mytable where uid = '
    curs = conn.cursor()
    i = 0
    while i < times:
        curs.execute(selectSql + str(random.randint(start, end)))
        i = i + 1
 

