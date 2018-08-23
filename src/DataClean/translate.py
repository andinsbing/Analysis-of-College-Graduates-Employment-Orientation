import os
import os.path
import sys


 
work_dir=r'C:\Users\lx\Desktop\科研兴趣\数据已归类' 

dic={}

def handle_file(file):
        try:
            key=str(file).split('\\')[-1].split('.')[0]
            if key in dic:
                new_name=str(file).replace(key,dic[key])
                if new_name!=file:
                    os.rename(file,new_name) 
        except BaseException as e:
            print(e)

def handle_dir():
    dir=os.getcwd()
    for i in os.listdir():
        if os.path.isdir(i):
            os.chdir(i)
            handle_dir()
            os.chdir(dir) 
        else:
            handle_file(i)  

def translate():
    with open('translate.txt','r',encoding='utf-8') as handle:
        lines=handle.read().split('\n')
        for i in lines:
            val,key=str(i).split()
            dic[key]=val 
    os.chdir(work_dir)
    handle_dir()




# if __name__=='__main__':
#     translate()
#     pass


