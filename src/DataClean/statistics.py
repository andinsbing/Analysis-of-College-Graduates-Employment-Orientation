# -*- coding: UTF-8 -*-

import os
import os.path 
import pickle  

base_dir=r'C:\Users\lx\Desktop\科研兴趣' 
mid_sp='<!sp>'

def extract_last_dir(dir):
    return str(dir).split('\\')[-1]

def combin_path(dir,path):
    return dir+'\\'+path

class JobItem: 
    def __init__(self,str):   
        try:
            self.company_name,self.job,self.money,self.place,self.experience,\
            self.tag,self.time,self.publish_place,self.advantage,self.duty,self.work_place=str.split(mid_sp)
        except BaseException as e:
            print(e)
        self.standard()
    def standard(self):
        self.tag=self.tag.split(',')
        self.advantage=self.advantage.strip("'").split(',')
        self.duty=self.duty.strip("'").split(',')

class Job:
    def __init__(self,abs_file_path):
        self.name=extract_last_dir(abs_file_path).split('.data')[0]
        with open(abs_file_path,'r',encoding='utf-8') as file_handle:
             lines=file_handle.read().strip().split('\n')
             self.items=[]
             for i in lines:
                 self.items.append(JobItem(i))  

class JobKind:
    def __init__(self,abs_dir):
        self.name=extract_last_dir(abs_dir)
        self.jobs=[]
        for i in os.listdir(abs_dir):
            if '.data' in i:
                new_path=combin_path(abs_dir,i)
                self.jobs.append(Job(new_path)) 


class JobKindSet:
    def __init__(self,abs_dir):
        self.name=extract_last_dir(abs_dir)
        self.job_kinds=[]
        for i in os.listdir(abs_dir):
            new_path=combin_path(abs_dir,i)
            self.job_kinds.append(JobKind(new_path))

def org_object():
    path=base_dir+r'\数据已归类'   
    return JobKindSet(path)

def save(object):
    with open(combin_path(base_dir,r'dump\dump'),'wb') as f:
        pickle.dump(object,f)

def load()->JobKindSet:
    with open(combin_path(base_dir,r'dump\dump'),'rb') as f:
        return pickle.load(f)
 
def get_duty_dic(obj)->{}:
    dic={}
    for kind in obj.job_kinds:
        for job in kind.jobs:
            for item in job.items:
                for duty in item.duty: 
                    if duty not in dic:
                        dic[duty]=0
                    dic[duty]+=1
    return dic

def	get_duty_list(obj): 
    ls=[]
    for kind in obj.job_kinds:
        for job in kind.jobs:
            for item in job.items:
                for duty in item.duty:
                    if duty not in ls:
                        ls.append(duty) 
    return ls

def make_path(path):
    if not os.path.exists(path):
        os.makedirs(path)

def analyse_duty_mask(dic:dict)->dict:
    ret={}
    if '' in dic.keys():
        ret['其他']=dic['']
        dic.pop('')
    ret['外语基础']=0
    for key in dic:
        if '语' in key:
            ret['外语基础']+=dic[key]
        else:
            ret[key]=dic[key]
    return ret
 
def analyse_duty_save(path,dic:dict,total):
    # dic=analyse_duty_mask(dic)
    sum=0
    max_num=0
    for val in dic.values():
        sum+=val
        max_num=max(max_num,val)
    try:
        with open(path,'w',encoding='utf-8') as f:
            f.write("{:<15}{:8}{:8}{:8}{:8}\n".format("名称",'频数','频率','最高比率','相对比率'))
            for key,val in sorted(dic.items(),key=lambda x:x[1],reverse=True):
                if key !='':
                    f.write("{:<15}{:8}{:8.3f}{:8.3f}{:8.3f}\n".format(key,val,val/total,val/max_num,val/sum))
            f.write("total  {0}\n".format(total))
    except BaseException as e:
        print(e)
    
def analyse_duty(obj:JobKindSet):
    sta_dir=combin_path(base_dir,r'statistics\result\duty')
    total_dic={}
    total_len=0
    total_sun_path=combin_path(sta_dir,"sum")
    make_path(sta_dir)
    for kind in obj.job_kinds:
        kind_dir=combin_path(sta_dir,kind.name)
        make_path(kind_dir)
        kind_sum_path=combin_path(kind_dir,"sum")
        kind_dic={}
        kind_len=0
        for job in kind.jobs:
            job_dic={}
            job_path=combin_path(kind_dir,job.name)
            for item in job.items:
                for duty in item.duty:
                    if duty not in job_dic:
                        job_dic[duty]=0
                    job_dic[duty]+=1
            analyse_duty_save(job_path,job_dic,len(job.items))
            for key,val in job_dic.items():
                if key not in kind_dic:
                    kind_dic[key]=0
                kind_dic[key]+=val
            kind_len+=len(job.items)
        analyse_duty_save(kind_sum_path,kind_dic,kind_len)
        for key,val in kind_dic.items():
            if key not in total_dic:
                total_dic[key]=0
            total_dic[key]+=val
        total_len+=kind_len
    analyse_duty_save(total_sun_path,total_dic,total_len)
            
def extend(obj):
    pass

def extract_duty(): 
    duty_dir=combin_path(base_dir,r'statistics\result\duty')
    total=[]
    for dir in os.listdir(duty_dir):
        file_dir=combin_path(duty_dir,dir)
        if os.path.isdir(file_dir):
            for file in os.listdir(file_dir):
                if file!='sum':
                    file_path=combin_path(file_dir,file) 
                    with open(file_path,'r',encoding='utf-8') as f:
                        lines=f.read().split('\n')
                        if len(lines)>10:
                            r1=lines[1].split()[0]
                            r2=lines[2].split()[0]
                            r3=lines[3].split()[0]
                            r4=lines[4].split()[0]
                            r5=lines[5].split()[0]
                            r6=lines[6].split()[0]
                            r7=lines[7].split()[0]
                            r8=lines[8].split()[0]
                        total.append((file,r1,r2,r3,r4,r5,r6,r7,r8)) 
    with open(combin_path(duty_dir,'extract'),'w',encoding='utf-8') as f:
        for i in total:
            f.write('{0},{1},{2},{3},{4},{5},{6},{7}\n'.format(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7]))

def read_duty_mask():
    mask_path=combin_path(base_dir,r'statistics\list\duty\duty_mask.txt')
    dic={}
    with open(mask_path,'r',encoding='utf-8') as f:
        lines=f.read().split('\n')
        for line in lines:
            v=line.split()
            if len(v)>1:
                dic[v[0]]=v[1]
    return dic
            
def duty_mask(obj:JobKindSet): 
    dic=read_duty_mask()
    for kind in obj.job_kinds:
        for job in kind.jobs:
            for item in job.items:
                for d in item.duty:
                    if d in dic.keys():
                        item.duty.remove(d)
                        item.duty.insert(0,dic[d])

def handle_org_obj():
    obj=org_object()#得到原始对象
    duty_mask(obj)#修改duty
    save(obj)#保存对象

# print('哈哈哈')
# for i in get_duty_list():
# 	print(str(i))
if __name__=='__main__':
    # handle_org_obj()
    job_kind_set=load()
    path=combin_path(base_dir,r'set')
    with open (path,'w',encoding='utf-8') as f:
        for kind in job_kind_set.job_kinds:
            for job in kind.jobs:
                for item in job.items:
                    for d in item.duty:
                        f.write("{0},{1}\n".format(job.name,','.join(item.duty)))



    # extract_duty()
    # analyse_duty(job_kind_set)
    # duty_mask(job_kind_set)
    # save(job_kind_set)
    # pass






    # duty_dic=get_duty_dic(job_kind_set)
    # total=0
    # for key,val in duty_dic.items():
    #     total+=val
    # print(total)
    # for key,val in duty_dic.items():
    #     print("{0}:{1}".format(key,val/total))
    # pass
