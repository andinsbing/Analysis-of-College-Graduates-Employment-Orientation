import pymysql
import traceback
import os.path
#职位要求分析结果上传至MySQL  学波
class DataMySQL:
    def __init__(self):
        self.__dataCount = 0  # 记录数
        self.__fileName = "" #录入文件名
    def SaveToMySQLDB(self,file,fileName):
        self.__fileName = fileName
        if self.__fileName == 'sum':
            self.__fileName = file + '_' + self.__fileName
        print(self.__fileName + ": 开始录入")
        self.CreateTable() #创建表
        self.__dataCount = 0
        with open(file+'\\'+fileName,'r',encoding='utf-8') as fileDate:
            while True :
                data = fileDate.readline()
                if self.__dataCount==0:
                    self.__dataCount=1;continue
                if data[:5] == 'total' : print(self.__fileName + " 录入完成") ;return
                self.__list = data.split(' ')
                self.SaveToDatabase()
                self.__dataCount += 1
    def SaveToDatabase(self):
            db = pymysql.Connect(
                host='47.100.11.75',
                port=3306,
                user='root',
                passwd='5880940',
                db='analysisResults',
                charset='utf8')
            cursor = db.cursor()
            lists=[]
            for x in range(len(self.__list)):
                if self.__list[x]!='':lists.append(self.__list[x])
            sql = "INSERT INTO `%s` VALUES ('%d','%s','%d', '%f', '%f', '%f')"%\
                  (self.__fileName,self.__dataCount, lists[0], int(lists[1]),
                   float(lists[2]), float(lists[3]), float(lists[4]))
            try:
                cursor.execute(sql)
                db.commit()
            except Exception:
                    print ('%d'" : 录入异常！" %self.__dataCount)
                    traceback.print_exc()
            finally: db.close()
    def CreateTable(self):
        db = pymysql.Connect(
            host='47.100.11.75',
            port=3306,
            user='root',
            passwd='5880940',
            db='analysisResults',
            charset='utf8')
        cursor = db.cursor()
        sql = """
                   CREATE TABLE `analysisResults`.`{}` (
  `ID` INT NOT NULL,
  `名称` TEXT NULL,
  `频数` INT NULL,
  `频率` DOUBLE NULL,
  `最高比率` DOUBLE NULL,
  `相对比率` DOUBLE NULL,
  PRIMARY KEY (`ID`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;
        """.format(self.__fileName)
        try:
            cursor.execute(sql)
            db.commit()
        except Exception:
            print(self.__fileName + " ***************创建表失败***************")
            traceback.print_exc()
        finally: db.close()
#多文件录入（二级目录）
def SaveMostFile():
    workDir = "F:\TomySQL\职位要求分析结果"
    os.chdir(workDir)  # 路径
    for file in os.listdir(workDir):
        print('开始录入： '+file)
        for fileName in os.listdir(workDir+'\\'+file):
            inputDB = DataMySQL()
            try:
                inputDB.SaveToMySQLDB(file,fileName)
            except Exception :
                print(file + '\\' + fileName + " : 异常")
                traceback.print_exc()
SaveMostFile()

