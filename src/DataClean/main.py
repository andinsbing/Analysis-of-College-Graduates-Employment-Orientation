import os.path
import os
import json
import re
import csv
# import jieba 

test_work_dir="C:\\Users\\lx\\Desktop\\科研兴趣\\test"
os.chdir(test_work_dir)

ignore_set=[]
with open('DataSet\\ignore','r',encoding='utf-8') as file_handle:
    ignore_set=file_handle.read().split('\n')

pick_set=[]
pick_hash={}
with open('DataSet\\pick','r',encoding='utf-8') as file_handle:
    pick_set=file_handle.read().split('\n')
    line_count=0
    while line_count<len(pick_set):
        temp=pick_set[line_count].split(' ')
        for x in temp:
            pick_hash[x]=pick_set[line_count+1]
        line_count+=2

post_keywords_set=[]
with open('DataSet\\post_keywords','r',encoding='utf-8') as file_handle:
    post_keywords_set=file_handle.read().split('\n')

pre_keywords_set=[]
with open('DataSet\\pre_keywords','r',encoding='utf-8') as file_handle:
    pre_keywords_set=file_handle.read().split('\n')

def analyze_hash_value(text):
    ret=[]
    for x in pick_hash:
        if x in text:
            ret.append(pick_hash[x])
    return ret

def analyze_duty(lines):
    ret=[]
    for x in lines:
        # for post_keywords in post_keywords_set:
        #     post_pattern=re.compile('\w+'+post_keywords+'\w+')
        #     res=post_pattern.findall(x)
        #     if res==[]:
        #         continue
        #     for x in res:
        for y in analyze_hash_value(x):
            if y not in ret:
                ret.append(y)
    return ret
           

class Recruitment:
    # _pattern=re.compile(r'\d+')#测试用的正则表达式
    _pattern=re.compile(r'^\s*[\(\)\[\]\{\}\<\>（）]?\d+[\(\)\[\]\{\}\<\>\.．、,。，（）:：]{0,2}([^\n]+)')
    def __init__(self,lines):
        self.company_name=lines[0].strip().strip('招聘')
        self.job=lines[1].strip()
        self.money,self.place,self.experience,self.education,self.full_time=\
        [x.strip() for x in lines[2].split('/')]

        line_count=3  #标签
        self.tag=[]
        while lines[line_count].find("发布于")==-1: 
            self.tag.append(lines[line_count].strip())
            line_count+=1
        self.time,self.publish_place=\
        [x.strip().strip('：').strip("发布于").strip('职位诱惑') for x in lines[line_count].split('  ')]
        
        line_count+=1 #职业诱惑 
        self._test_separator(lines[line_count]) 
        self.advantage=\
        [x.strip() for x in lines[line_count].split(self._test_separator(lines[line_count])) if x.strip()!='']

        while lines[line_count].find('职位描述')==-1:    #跳至职业描述模块
            line_count+=1

        self.duty=[]
        line_count+=1
        while lines[line_count].find('工作地址')==-1:   #开始处理职业描述模块
            ans=Recruitment._pattern.findall(lines[line_count]) 
            line_count+=1 
            if ans!=[]:
                temp=ans[0].strip().strip('\n\r;；.。, ').strip()
                self.duty.append(temp)
                # cut=jieba.lcut(temp,cut_all=False)
                # for x in cut:
                #     if len(x)>1:
                #         self.duty.append(x)
        self.duty=analyze_duty(self.duty)
        line_count+=1
        self.work_place=[lines[line_count].strip()][0]

    def _test_separator(self,text):    #检测职业诱惑条目的分隔符
        set=",，、 ;； "
        for x in text:
            if set.find(x)!=-1:
                return x
        return ' ' 
    def to_str(self): 
        return "{0}<!sp>{1}<!sp>{2}<!sp>{3}<!sp>{4}<!sp>'{5}'<!sp>{6}<!sp>{7}<!sp>'{8}'<!sp>'{9}'<!sp>{10}\n".format(\
        self.company_name,self.job,self.money,self.place,self.experience,\
        ','.join(self.tag),self.time,self.publish_place,\
       ','.join(self.advantage),','.join(self.duty),self.work_place)
 

#改变工作路径
work_dir="C:\\Users\\lx\\Desktop\\科研兴趣\\数据已归类"
os.chdir(work_dir)

#调试文本流
f_log = open("a..data.temp","w",encoding='utf-8')  

def log(text):
    f_log.write(text)

#文件内的多个分隔成单个内容
def split(text):
    separator='\n-------------------------------------------------\n'
    text=str(text).strip().strip('\n').strip(separator)
    ls=text.split(separator)
    for i in range(len(ls)):
        ls[i]=ls[i].strip() 
    return ls
 

def deal(file_name,text):
    with open(file_name+'.data','w',encoding='utf-8') as file_handle:
        for info in split(text):
            # try:
                lines=info.splitlines(True)
                if len(lines)<=10:          #数据太短不处理
                    continue
                if lines[2].find("已下线")!=-1:   #下线的数据不处理
                    continue
                # name=lines[0]
                # job=lines[1].split('/')[0]
                # money,place,experience,education,full_time=lines[2].split('/')
                # file_handle.write("{0} {1} {2} {3}\n".format(job.strip(),money.strip(),place.strip(),experience.strip()))
                file_handle.write(Recruitment(lines).to_str())
            # except BaseException as e:
            #     print(file_name+" except")

def handle_file(file_name):
    if str(file_name).find('.data')==-1: #不是清洗后的数据
        with open(file_name,'r',encoding='utf-8') as file_handle:  
            text=file_handle.read() 
            try:
                print('deal :'+file_name)
                deal(file_name,text)
            except BaseException as e:
                print('exception :'+file_name)
    

def handle_dir(dir):
    last_dir=os.getcwd()
    os.chdir(dir)
    for path in os.listdir(dir):
        if os.path.isdir(path):
            handle_dir(last_dir+'\\' +path)
        elif os.path.isfile(path):
            handle_file(path)
    os.chdir(last_dir)
            

def main():
    handle_dir(work_dir)
    f_log.close()

# main()


try:
    main()
except BaseException as e:
    print()
# test_work_dir="C:\\Users\\lx\\Desktop\\科研兴趣\\test"
# os.chdir(test_work_dir)
# test_file_name='.NET.data' #测试用的文件
# with open(test_file_name,'r',encoding='utf-8') as file_handle:
#     text=file_handle.read()
#     # deal(test_file_name,text) 
#     reader=csv.reader(file_handle,delimiter=',',doublequote=False,quotechar="'",strict=True)
#     for row in reader:
#         print(','.join(row))