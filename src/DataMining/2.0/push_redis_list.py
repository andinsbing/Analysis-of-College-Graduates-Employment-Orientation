from selenium import webdriver
from selenium.webdriver.common.by import By
from redis import Redis
import time
from get_from_redis import get_driver
from get_from_redis import save_error_image

def get_task_urls(txt_path):
    f = open(txt_path)
    for url in f.readlines():
        url = url.strip()
        # this different
        yield url[1:-2]
    f.close()


def get_hrefs(tasks):
    hrefs = []

    driver = get_driver()

    for task in tasks:
        job_type = task[30:-1]
        try:
            driver.get(task)
            pages = int(driver.find_element_by_class_name('totalNum').text)
            for i in range(1, min(pages + 1, 15)):  # 翻页获取href
                try:
                    driver.get(task + str(i))
                    li = driver.find_elements(By.CLASS_NAME, 'position_link')
                    for j in li:
                        href = j.get_attribute('href')
                        print(href)
                        hrefs.append(href + ' ' + job_type)
                except Exception as e:
                    print(e)
                    save_error_image(driver)
        except Exception as e:
            print(e)
            save_error_image(driver)
    driver.close()
    return hrefs


def push_redis_list(txt_path):
    r = Redis(host='47.100.11.75', port=6388, db=0, password='redisredis')
    print(r.keys('*'))
    print('Redis connection OK!')
    tasks = get_task_urls(txt_path)
    print('Get Tasks OK!')
    hrefs = get_hrefs(tasks)
    print('Get hrefs OK!')
    # 需要去重
    # TODO
    for each in hrefs:
        r.rpush('tasks', each)
    print('Push Redis list Success!')


if __name__ == '__main__':
    push_redis_list('target.txt')
