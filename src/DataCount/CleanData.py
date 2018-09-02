import jieba
import os
import re
import xlwt
#by 学波 用于词频统计
def NewFile(fileName):
    fob = open(fileName, 'w', encoding='utf-8')
    fob.close()

class CleanData:
    def __init__(self):
        self.__fileCount = 0
        self.__fileData = ""
        self.__wordDict = {}  # 词频统计

    def GetCount(self):
        return self.__fileCount

    def Check(self, string):
        if len(string) <= 1: return False  # 筛选单个字符
        if string.isdigit(): return False  # 筛选数字
        if string.isalpha() and len(string) >= 15: return False  # 筛选字母
        if string.isalnum() and len(string) >= 15: return False  # 筛选字母及数字组合
        return True

    def SigleCount(self, fileName):
        wbk = xlwt.Workbook(encoding='utf-8')
        sheet = wbk.add_sheet("wordCount")
        keyList = []
        sumList = 0
        orderList = sorted(self.__wordDict.items(), key=lambda Dict: (Dict[1], Dict[0]), reverse=True)
        # 筛选
        for key in orderList:
            if self.Check(key[0]):
                keyList.append([key[0], key[1]])
                sumList += key[1]
        #print('总和 : %d , 准备存入 %d 条数据' % (sumList, len(keyList)))
        # 存入格式
        style = xlwt.easyxf(num_format_str='0.0000%')
        sheet.write(0, 1, 'ID')
        sheet.write(0, 0, 'COUNT')
        sheet.write(0, 2, 'PERCENT')
        # 存入
        NewFile('F:\data3st\\' + fileName[:len(fileName) - 4] + '.3st')
        with open('F:\data3st\\' + fileName[:len(fileName) - 4] + '.3st', 'a', encoding='utf-8') as f:
            f.write('总:%d 存:%d\n' % (sumList, len(keyList)))
        for i in range(len(keyList)):
            sheet.write(i + 1, 0, label=keyList[i][0])
            sheet.write(i + 1, 1, label=keyList[i][1])
            sheet.write(i + 1, 2, float(keyList[i][1]) / sumList, style)
            #print('存入 %s       %d        %f' % (keyList[i][0], keyList[i][1], float(keyList[i][1]) / sumList))
            with open('F:\data3st\\' + fileName[:len(fileName) - 4] + '.3st', 'a', encoding='utf-8') as f:
                f.write(keyList[i][0])
                f.write(' ')
                f.write('%d'% keyList[i][1])
                f.write(' ')
                f.write('%.4f%%'% (float(keyList[i][1])*100.0 / sumList))
                f.write('\n')
        # 保存
        wbk.save(fileName[:len(fileName) - 4] + '3st.xls')

    def Scan(self, fileName):
        self.__wordDict = {}
        with open(fileName, 'r', encoding='utf-8') as fileData:
            self.__fileCount = 0
            NewFile('F:\data2st\\' + fileName[:len(fileName) - 4] + '.2st')
            while True:
                self.__fileData = fileData.readline()
                if self.__fileData == '':
                    #print("%s : 共 %d 条记录录入完毕" % (fileName, self.__fileCount));
                    #print("开始词频统计")
                    self.SigleCount(fileName)
                    return
                self.__fileData = self.__fileData.split('\\n')
                self.__fileCount += 1
                for STR in self.__fileData:
                    # 对切出的字符串去特殊符号
                    sss = '[\[\s+\.\!\/_,$%^*(+\"\'\\]\]+|[+——！√，\'•。？ 、Ø·~@#￥%……&*（).）、；◎】→【：☆:;◆-]+'
                    STR = re.sub(sss, "", STR)
                    STR = jieba.cut(STR, cut_all=False)
                    tempStr = '|'.join(STR)
                    #print(tempStr)
                    m = list(tempStr.split('|'))
                    with open('F:\data2st\\' + fileName[:len(fileName) - 4] + '.2st', 'a', encoding='utf-8') as f:
                        for word in m:
                            if word == '\ufeff' or word == '\n':
                                continue
                            else:
                                f.write(word)
                                if word not in self.__wordDict:
                                    self.__wordDict[word] = 1
                                else:
                                    self.__wordDict[word] += 1
                        f.write('\n')
workDir = "F:\data"
os.chdir(workDir)  # 路径

# 多文件录入
def SaveData():
    inputDB = CleanData()
    for fileName in os.listdir(workDir):
        if fileName[len(fileName) - 4:] == '.1st':
            try:
                inputDB.Scan(fileName)
            except BaseException as e:
                print("%s  异常" % (fileName))
    print("Finish")
SaveData()
