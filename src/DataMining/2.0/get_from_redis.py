from selenium import webdriver
from selenium.webdriver.common.by import By
from redis import Redis
import time

def get_from_redis():
    f = open('data.txt','a',encoding='utf-8')
    r = Redis(host='47.100.11.75',port=6388,db=0,password='redisredis')
    print(r.keys('*'))

    #options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    #driver =
    #webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)

    driver = webdriver.Chrome()

    while True:
        next = r.lpop('tasks')
        if next != None:
            try:
                next = str(next, encoding = "utf-8")  
                driver.get((next.split())[0])
                f.write(next.split()[1] + '\n')
                f.write(driver.find_element_by_class_name('position-content-l').text)
                f.write(driver.find_element_by_class_name('job_detail').text)
                f.write('$thisisaseprator$\n')
            except:
                # 截个屏看看
                driver.save_screenshot((time.ctime(time.time())).replace(' ','_') + '.png')
        else:
            break
    f.close()
    driver.close()

if __name__ == '__main__':
    get_from_redis()