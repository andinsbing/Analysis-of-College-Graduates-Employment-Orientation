import os.path
import os
import json

#改变工作路径
work_dir="C:\\Users\\林鑫\\Desktop\\数据"
os.chdir(work_dir)

#调试文本流
f_log = open("temp.data","w",encoding='utf-8')  

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
            try:
                lines=info.splitlines(True)
                if lines[2].find("已下线")!=-1:   #下线的数据不处理
                    continue
                job=lines[1].split('/')[0].strip()
                money=lines[2].split('/')[0].strip()
                experience=lines[2].split('/')[2].strip()
                file_handle.write("{0} {1} {2}\n".format(job,money,experience))
            except:
                print("emm")
def main():
    for file_name in os.listdir(work_dir):
        if str(file_name).find('.data')==-1: #不是清洗后的数据
            with open(file_name,'r',encoding='utf-8') as file_handle:  
                text=file_handle.read()
                try:
                    deal(file_name,text)
                except:
                    print(file_name)
    f_log.close()

main()


# try:
#     main()
# except:
#     print()

# test_file_name='Perl' #测试用的文件
# with open(test_file_name,'r',encoding='utf-8') as file_handle:
#     text=file_handle.read()
#     deal(text)