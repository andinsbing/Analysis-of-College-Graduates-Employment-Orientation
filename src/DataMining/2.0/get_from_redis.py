from selenium import webdriver
from selenium.webdriver.common.by import By
from redis import Redis
import time
import sys
import os

# 得到截屏的保存路径


def get_save_path():
    path = time.ctime(time.time()).replace(' ', '_').replace(':', '-') + '.png'
    if(os.path.exists('error_images')):
        pass
    else:
        os.mkdir('error_images')
    path = './error_images/'+path
    return path


def save_error_image(driver):
    print(driver.save_screenshot(get_save_path()))

# 针对不同的操作系统生成driver


def get_driver():
    if(sys.platform == 'win32'):
        return webdriver.Chrome()
    else:
        # 在Linux下运行Chrome下要求附加
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.add_argument('--headless')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(
            executable_path="/usr/bin/chromedriver", chrome_options=options)
        return driver


def get_from_redis():
    f = open('data.txt', 'a', encoding='utf-8')
    r = Redis(host='47.100.11.75', port=6388, db=0, password='redisredis')
    print(r.keys('*'))

    driver = get_driver()

    while True:
        next = r.lpop('tasks')
        if next != None:
            try:
                next = str(next, encoding="utf-8")
                driver.get((next.split())[0])
                f.write(next.split()[1] + '\n')
                f.write(driver.find_element_by_class_name(
                    'position-content-l').text)
                f.write(driver.find_element_by_class_name('job_detail').text)
                f.write('\n$thisisaseprator$\n')
            except:
                # 截个屏看看
                save_error_image(driver)
        else:
            break
    f.close()
    driver.close()


if __name__ == '__main__':
    driver = get_driver()
    driver.get('https://www.baidu.com')
    save_error_image(driver)
    driver.close()
