from selenium import webdriver
from selenium.webdriver.common.by import By
from redis import Redis
import time

def get_task_urls(txt_path):
    f = open(txt_path)
    lists = []
    for url in f.readlines():
        url = url.strip()
        lists.append(url)
    f.close()
    return lists

def get_hrefs(tasks):
    hrefs = []

    #options = Options()
    #options.add_argument('--headless')
    #options.add_argument('--no-sandbox')
    #options.add_argument('--disable-dev-shm-usage')
    #driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",chrome_options=options)

    driver = webdriver.Chrome()
    for task in tasks:
        job_type = task[30:-1]
        driver.get(task)
        pages = int(driver.find_element_by_class_name('totalNum').text)
        for i in range(1, min(pages + 1,3)):  # 翻页获取href
            driver.get(task + str(i))
            li = driver.find_elements(By.CLASS_NAME, 'position_link')
            for j in li:
                href = j.get_attribute('href')
                print(href)
                hrefs.append(href + ' ' + job_type)
    driver.close()
    return hrefs

def push_redis_list(txt_path):
    r = Redis(host='47.100.11.75',port=6388,db=0,password='redisredis')
    print(r.keys('*'))
    print('Redis connection OK!')
    tasks = get_task_urls(txt_path)
    print('Get Tasks OK!')
    hrefs = get_hrefs(tasks)
    print('Get hrefs OK!')
    for each in hrefs:
        r.rpush('tasks',each)
    print('Push Redis list Success!')

if __name__ == '__main__':
    push_redis_list('tasks.txt')