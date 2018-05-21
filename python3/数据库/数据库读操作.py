import sqlite3 as db 
import time
import datetime
import xlwt


splitNumber = 50000
sqlitePath = 'FaceModelTestTool.sqlite'


# 将一个列表分割成小列表
def list_of_groups(init_list, childern_list_len):
    '''
    init_list为初始化的列表，childern_list_len初始化列表中的几个数据组成一个小列表
    :param init_list:
    :param childern_list_len:
    :return:
    '''
    list_of_group = zip(*(iter(init_list),) *childern_list_len)
    end_list = [list(i) for i in list_of_group]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count !=0 else end_list
    return end_list
    
# 读文件
def readFromSqlite(dbPath,cmdSql):
    '''
    读文件
    '''    
    conn = db.connect(dbPath)
    cursor = conn.cursor()

    conn.row_factory = db.Row
    
    cursor.execute(cmdSql)
    
    rows = cursor.fetchall()
    
    return rows

def getTableHeader(dbPath,cmdSql):
    conn = db.connect(dbPath)
    cursor = conn.cursor()

    cursor.execute(cmdSql)
    table_headers = cursor.fetchall()
    
    arrayHeaders = []
    for header in table_headers:
        name = header[1]
        arrayHeaders.append(name)
    
    return arrayHeaders

def writeXlsx(headers,rowsAll,tableName):
    workBook = xlwt.Workbook()               #创建工作簿

    rowsAllList = list_of_groups(rowsAll,splitNumber)
    print(len(rowsAllList))
    for k in range(len(rowsAllList)):
        sheetName = 'sheet-{0}'.format(k+1)
        print(tableName + sheetName)
        sheet = workBook.add_sheet(sheetName,cell_overwrite_ok=True)

        rows = rowsAllList[k]
        # 标题
        for i in range(len(headers)):
            sheet.write(0,i,headers[i])

        # 内容
        for i in range(len(rows)):
            row = rows[i]
            # print(row)
            print("表名:{0} 总共 {1} 组,现在第 {2} 组|进行中 {3} 进度:{4}%".format(tableName,len(rowsAllList),k+1,i+1,(i+1)/len(rows)*100))
            for j in range(len(headers)):
                sheet.write(i+1,j,str(row[j]))           

    timeWrite1 = datetime.datetime.now()
    workBook.save('{0}.xlsx'.format(tableName))  

    timeWrite2 = datetime.datetime.now()
    print("表名:{0} 写入Excel总时间: {1}".format(tableName,timeWrite2-timeWrite1))

def getTable(tableName):
    headers = getTableHeader(sqlitePath,"PRAGMA table_info({0})".format(tableName))

    timeRead1 = datetime.datetime.now()
    rows = readFromSqlite(sqlitePath,"select * from {0}".format(tableName))
    timeRead2 = datetime.datetime.now()
    print("表名:{0} 读取时间: {1}--总数目:{2}".format(tableName,timeRead2-timeRead1,len(rows)))
    
    if not len(rows):
        print("表名:{0} 没有数据".format(tableName))
    else:    
        timeWrite1 = datetime.datetime.now()
        writeXlsx(headers,rows,tableName)
        timeWrite2 = datetime.datetime.now()
        print("表名:{0} 全过程总花费时间: {1}".format(tableName,timeWrite2-timeWrite1))

if __name__ == '__main__':
    # 表名 根据需要选择 ComparedDoorModel | ComparedModelModel | ThresholdModelModel | ThresholdDoorModel

    getTable("ComparedDoorModel")
    getTable("ComparedModelModel")
    getTable("ThresholdModelModel")
    getTable("ThresholdDoorModel")

    
