import os
import os.path
#上传至SQLserver DB by 学波
class InputDB:
    def __init__(self):
        self.__dataCount = 0 #记录数
        self.__list = []
        self.__fileName = "" #数据库文件名

    def SaveToProperty(self,fileName):
        self.__fileName = fileName[:-5]
        print(self.__fileName + ": 开始录入")
        self.CreateDBtable()
        self.__dataCount = 0
        with open(fileName, 'r', encoding='utf-8') as fileDate:
            while True :
                data = fileDate.readline()
                if data == '' : print("录入完毕") ;return
                self.__dataCount+=1
                self.__list = self.ReadData(data)
                self.SaveToDatabase()


    def ReadData(self,data):
        strTemp = ''
        strList = []
        for c in data:
            if c=='|' : strList.append(strTemp);strTemp='';continue
            elif c=='\n' :
               strList.append(strTemp);return strList
            strTemp += c

    def CreateDBtable(self):
        try :
            conn = pymssql.connect("47.100.11.75", "cdy", "123456", "Position")
            cursor = conn.cursor()
            cursor.execute("""
            CREATE TABLE {} (
	            PosID int PRIMARY KEY,
	            招聘公司 nchar(100),
	            招聘职业 nchar(80),
	            工资	 nchar(40),
	            工作地点 nchar(50),
	            工作经验要求 nchar(50),
	            标签 nchar(100),
	            发布时间 nchar(40),
	            发布地点 nchar(40),
	            薪酬福利 nchar(200),
	            职位要求 nchar(1500),
	            具体工作地点 nchar(200),
            ) """.format(self.__fileName))
        finally : conn.commit();conn.close()
    def SaveToDatabase(self):
        try:
            conn = pymssql.connect("47.100.11.75", "cdy", "123456", "Position")
            cursor = conn.cursor()
            #list = ('1','2','3','4','5','6','7','8','9','10','11')
            cursor.executemany(\
                "INSERT INTO {} VALUES (%d,%s, %s, %s,%s, %s,%s, %s, %s, %s, %s,%s)".format(self.__fileName),
                [(self.__dataCount,self.__list[0], self.__list[1],self.__list[2],self.__list[3],self.__list[4],
                  self.__list[5],self.__list[6],self.__list[7],self.__list[8],self.__list[9],self.__list[10])])
        except : print ('%d'" :号录入异常！" %self.__dataCount)
        finally: conn.commit();conn.close()
workDir = "E:\数据文件"
os.chdir(workDir) # 路径
#多文件录入
def SaveMostFile():
    inputDB = InputDB()
    for fileName in os.listdir(workDir):
        try:
            inputDB.SaveToProperty(fileName)
        except BaseException as e:
            print(fileName + " : 异常")

#单文件录入
def SaveSingleFile():
    inputDB = InputDB()
    fileNames = []
    try:
        for fileName in fileNames:
            inputDB.SaveToProperty(fileName)
    except BaseException as e:
        print(fileName + " : 异常")

