import os
import xlwt
#by 学波 用于词频统计
class CountData:
    def __init__(self):
        self.__CountList = {}
        self.__fileCount = 0
        self.__SumRecode = 0
    def Countsub(self,strFile):
        #print(strFile)
        with  open(strFile,'r',encoding='utf-8') as f:
            fileData = f.readline()
            fileData = list(fileData.split(' '))
            fileData = fileData[0][2:]
            self.__SumRecode+=int(fileData)
            while True:
                fileData = f.readline()
                if(fileData=='') :
                    return
                fileData = fileData.rstrip('\n')
                fileData = list(fileData.split(' '))
                #print("%s %s"%(fileData[0],fileData[1]))
                if fileData[0] in self.__CountList:
                    self.__CountList[fileData[0]] += int(fileData[1])
                else :
                    self.__CountList[fileData[0]] = int(fileData[1])
    def Input(self):
        orderList = sorted(self.__CountList.items(), key=lambda Dict: (Dict[1], Dict[0]), reverse=True)
        fob = open("F:\data4st\data.4st", 'w', encoding='utf-8')
        fob.close()
        wbk = xlwt.Workbook(encoding='utf-8')
        sheet = wbk.add_sheet("wordCount")
        style = xlwt.easyxf(num_format_str='0.0000%')
        sheet.write(0, 1, 'ID')
        sheet.write(0, 0, 'COUNT')
        sheet.write(0, 2, 'PERCENT')
        i = 1
        with open("F:\data4st\data.4st",'a',encoding='utf-8') as f:
            for str in orderList:
                f.write(str[0]);f.write(' ')
                f.write('%d'%str[1]);f.write(' ')
                f.write('%.7f%%'%((float(str[1])) * 100.0/self.__SumRecode));f.write('\n')
                #sheet.write(i, 0, label=str[0])
                #sheet.write(i, 1, label=str[1])
                #sheet.write(i, 2, float(str[1]) / self.__SumRecode, style)
                #i+=1
                print('%s %s'%(str[0],str[1]))
        #wbk.save('data4st.xls')
workDir = "F:\data3st"
os.chdir(workDir)  # 路径

# 多文件录入
def SaveData():
    inputDB = CountData()
    count = 0
    for fileName in os.listdir(workDir):
        if fileName[len(fileName) - 4:] == '.3st':
            try:
                inputDB.Countsub(fileName)
                count+=1
            except BaseException as e:
                print("%s  异常" % (fileName))
    print("共%d文件读取完毕" % count)
    try:
        inputDB.Input()
    except BaseException as e:
        print("异常")
    print("finish")
SaveData()