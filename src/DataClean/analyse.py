import os.path
import os
import jieba
import re


#-------------------------------------------------
def debug(x):
    print(x)

def debug_set(x):
    for i in x:
        debug(i)

def debug_condition(condition,x):
    if condition==False:
        debug(x)
    return condition 
#-------------------------------------------------
def get_raw_file_path(file_path):
    return file_path.split('.')[0]

def get_org_file_path(file_path):
    return get_raw_file_path(file_path)+'.org'

def get_1st_file_path(file_path):
    return get_raw_file_path(file_path)+'.1st'

#获取目录下所有文件
def get_all_file(work_dir):
    return os.listdir(work_dir)

def file_fliter(ls,text):
    return [x for x in ls if text in x]

def reverse_file_fliter(ls,text):
    return [x for x in ls if text not in x]

def fliter_org_file(ls):
    return file_fliter(ls,".org")

def fliter_raw_file(ls):
    return reverse_file_fliter(ls,'.')

def get_file_set(work_dir,fliter_fun):
    return fliter_fun(get_all_file(work_dir))

#得到work_dir下以org为后缀的文件名
def get_org_file_set(work_dir):
    return get_file_set(work_dir,fliter_org_file)

def get_raw_file_set(work_dir):
    return get_file_set(work_dir,fliter_raw_file)
#-------------------------------------------------

def check_set_in(text,sub_text_set):
    for i in sub_text_set:
        if not check_in(text,i):
            return False
    return True

def check_in(text,sub_text):
    return sub_text in text

def check_1st(text):
    return True

def check_2st(text):
    return  check_in(text,'福利')

def check_3st(text): 
    return check_set_in(text,('月薪','地点','经验','学历','类别'))
 
def check_4st(text):
    return True

def check_5st(text): 
    return True
 
def check_text_style_helper(texts,i):
    ret=True
    ret&=debug_condition(check_1st(texts[i]),'check 1 failed at line {0}:\n'.format(i)+texts[i])
    ret&=debug_condition(check_2st(texts[i+1]),'check 1 failed at line {0}:\n'.format(i)+texts[i+1])
    ret&=debug_condition(check_3st(texts[i+2]),'check 1 failed at line {0}:\n'.format(i)+texts[i+2])
    ret&=debug_condition(check_4st(texts[i+3]),'check 1 failed at line {0}:\n'.format(i)+texts[i+3])
    ret&=debug_condition(check_5st(texts[i+4]),'check 1 failed at line {0}:\n'.format(i)+texts[i+4])
    return ret

#检测文本的格式
def check_text_style(texts):
    if(len(texts)%5!=0):
        debug_condition(False,'texts length not match')
        for i in range(0,len(texts)//5):
            if not check_text_style_helper(texts,i*5):
                break;
        return False;
    ret=True
    for i in range(0,len(texts)//5):
        ret&=check_text_style_helper(texts,i*5)
    return ret

#检测路径为path的文件内容的格式
def check_org_file(file_path): 
    debug_condition(check_text_style(get_file_text_separated(file_path)),file_path+" check failed")

#检测工作空间下所有org文件内容的格式
def check_org_dir(work_dir):
    # i=0
    # ls=get_file_set(work_dir,fliter_org_file)
    for file_name in get_file_set(work_dir,fliter_org_file):
        file_path=work_dir+'\\'+file_name
        check_org_file(file_path)
        # print('{0}: ok'.format(file_name))
        # print('file:{0}/{1}'.format(i,len(ls)))
        # i+=1

#-------------------------------------------------
def encoding_data(data):
    separator=''
    return str(data)+separator

def encoding_data_set(set):
    ret=''
    for i in set:
        ret+=encoding_data(i)
    return ret

def separate_org_file(text):
    separator='\n**********\n'
    return [x.strip() for x in text.split(separator)]

def get_file_text_separated(path):
    with open(path,'r',encoding='utf-8') as handle:
        return separate_org_file(handle.read())

def analyze_1st(text):
    return encoding_data(text.split('\n')[1])

def analyze_2st(text):
    return encoding_data('')

def analyze_3st(text):
    tx=text.split('\n')
    money_range=tx[0].split('：')[1].rstrip('元/月 ')
    work_place=tx[1].split('：')[1].split('-')[0]
    degree=tx[5].split('：')[1]
    work_type=tx[7].split('：')[1]
    experience=tx[4].split('：')[1].rstrip('年')
    return encoding_data_set([money_range,work_place,experience,degree,work_type])

def analyze_4st(text):
    return encoding_data([text]) # TO DO 

def analyze_5st(text):
    tx=text.split('\n')
    industry=tx[6]
    industry_type=tx[4]
    return encoding_data_set([industry,industry_type])

def analyze_org_file_helper(texts,i):
    # return analyze_1st(texts[i*5])+\
    # analyze_2st(texts[i*5+1])+\
    # analyze_3st(texts[i*5+2])+\
    # analyze_4st(texts[i*5+3])+\
    # analyze_5st(texts[i*5+4])
    return analyze_4st(texts[i*5+3])

def analyze_org_file(path):
    ret=''
    texts=get_file_text_separated(get_org_file_path(path))
    for i in range(0,len(texts)//5):
        ret+=analyze_org_file_helper(texts,i)
        ret+='\n'
    return ret

def save_analyzed_org_data(text,org_file_path):
    des_file=org_file_path.split('.')[0]+'.1st'
    with open(des_file,'w',encoding='utf-8') as file_handle:
        file_handle.write(text)

def analyze_org_dir(work_dir):
    for i in get_org_file_set(work_dir):
        file_path=work_dir+'\\'+i;
        save_analyzed_org_data(analyze_org_file(file_path),file_path)
    
#------------------------------------------------- 

def read_file(file_path,text):
    with open(file_path,'r',encoding='utf-8') as handle:
        return handle.read()

def write_file(file_path,text):
    with open(file_path,'r',encoding='utf-8') as handle:
        handle.write(text)

def anaylze_raw_file(file_path):
    write_file(get_org_file_path(file_path),
    anaylze_raw_file_helper(read(get_raw_file_path(file_path))))

def anaylze_raw_dir(work_dir):
    for i in get_raw_file_set(work_dir):
        anaylze_raw_file_helper(work_dir+'\\'+i);

def anaylze_raw_file_helper(text):
    return re.sub(r'\*\*\*\*\*\*\*\*\*\*\n\n','',\
    re.sub(r'\n\*\*\*\*\*\*\*\*\*\*\n福利:\n\n\*\*\*\*\*\*\*\*\*\*\n','',\
    re.sub(r'(\*){11,}','',text.strip(' *\n').strip())))


def anlayze_and_check_file(file_path):
    anaylze_raw_file(file_path)
    check_org_file(file_path)
#-------------------------------------------------

def test():
    work_dir="F:\PythonProject\DataAnalysis\\bigdata" 
    # anaylze_raw_dir(work_dir)
    # check_org_dir(work_dir)
    # file_name='娱乐-体育-休闲_武汉';
    # file_path=work_dir+'\\'+file_name
    # anlyze_and_check_file(file_path)
    analyze_org_dir(work_dir)
test()
