import csv
import pymysql
# 学波 用于将CSV文件传至数据库
def CsvToDB():
    csvPath = "F:/TomySQL/Resultsalary.csv"
    IDnum = 1
    db = pymysql.Connect(
            host='47.100.11.75',
            port=3306,
            user='root',
            passwd='5880940',
            db='ResearchProject',
            charset='utf8')
    cursor = db.cursor()
    reader = csv.reader(open(csvPath, 'r', encoding="utf-8"))
    for row in reader:
        #print(IDnum,row[0],row[1],row[2],row[3],row[4])
        sql = "INSERT INTO Resultsalary VALUES('%d','%s','%s','%s','%f','%f')"%\
                           (IDnum,row[0],row[1],row[2],float(row[3]),float(row[4]))
        #[(IDnum,row[0],row[1],row[2],row[3],row[4])] %d,%s,%s,%s,%s,%s
        try:
            cursor.execute(sql)
            IDnum += 1
            db.commit()
        except: db.rollback();print ('%d'" : 异常！" %IDnum)
    db.close()
CsvToDB()