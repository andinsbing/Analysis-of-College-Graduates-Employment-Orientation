from selenium import webdriver
from selenium.webdriver.common.by import By
from redis import Redis
import time
from get_from_redis import get_driver
from get_from_redis import save_error_image


def get_hrefs():
    hrefs = []
    r = Redis(host='47.100.11.75', port=6388, db=0, password='password')
    driver = get_driver()
    while True:
        r_type = r.lpop('type_queue')
        if r_type != None:
            job_type = r_type[30:-1]
            try:
                driver.get(r_type)
                pages = int(driver.find_element_by_class_name('totalNum').text)
                for i in range(1, min(pages + 1, 15)):  # 翻页获取href
                    try:
                        driver.get(r_type + str(i))
                        li = driver.find_elements(
                            By.CLASS_NAME, 'position_link')
                        for j in li:
                            href = j.get_attribute('href')
                            print(href)
                            hrefs.append(href + ' ' + job_type)
                    except Exception as e:
                        print(e)
                        # save_error_image(driver)
            except Exception as e:
                print(e)
                # save_error_image(driver)
    driver.close()
    return hrefs


def push_redis_list(txt_path):
    r = Redis(host='47.100.11.75', port=6388, db=0, password='password')
    print(r.keys('*'))
    print('Redis connection OK!')
    hrefs = get_hrefs()
    print('Get hrefs OK!')
    for each in hrefs:
        r.rpush('jobs', each)
    print('Push Redis list Success!')


if __name__ == '__main__':
    push_redis_list('target.txt')
