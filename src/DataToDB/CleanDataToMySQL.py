import pymysql
import traceback
import os.path

#清洗的数据上传至MySQL  学波
class DataMySQL:
    def __init__(self):
        self.__dataCount = 0  # 记录数
        self.__fileName = "" #录入文件名
    def SaveToMySQLDB(self,file,fileName):
        self.__fileName = fileName[:-5]
        print(self.__fileName + ": 开始录入")
        self.CreateTable() #创建表
        self.__dataCount = 0
        with open(file+'\\'+fileName,'r',encoding='utf-8') as fileDate:
            while True :
                data = fileDate.readline()
                if data == '' : print(self.__fileName + " 录入完成") ;return
                self.__dataCount += 1
                self.__list = data.split('<!sp>')
                self.SaveToDatabase()
    def SaveToDatabase(self):
            db = pymysql.Connect(
                host='47.100.11.75',
                port=3306,
                user='root',
                passwd='5880940',
                db='finalData',
                charset='utf8')
            cursor = db.cursor()
            #list = ('1','2','3','4','5','6','7','8','9','10','11')
            for x in range(0,11):
                self.__list.append('')
                self.__list[x] = self.__list[x].strip('\'')
                self.__list[x] = self.__list[x].replace('\'','’')
                #self.__list[x] = '\''+self.__list[x]+'\''

            sql = "INSERT INTO `%s` VALUES ('%d','%s','%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s')"%\
                  (self.__fileName,self.__dataCount, self.__list[0], self.__list[1], self.__list[2], self.__list[3],self.__list[4],
                   self.__list[5], self.__list[6], self.__list[7], self.__list[8], self.__list[9],self.__list[10])
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
            db='finalData',
            charset='utf8')
        cursor = db.cursor()
        sql = """
                   CREATE TABLE `finalData`.`{}` (
  `ID` INT NOT NULL,
  `招聘单位` TEXT NULL,
  `岗位名称` TEXT NULL,
  `工资` CHAR(50) NULL,
  `城市` CHAR(50) NULL,
  `经验要求` CHAR(100) NULL,
  `岗位性质` TEXT NULL,
  `发布时间` CHAR(100) NULL,
  `发布地点` TEXT NULL,
  `公司福利` TEXT NULL,
  `岗位要求` TEXT NULL,
  `具体地点` TEXT NULL,
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
    workDir = "F:\TomySQL\最终数据"
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

