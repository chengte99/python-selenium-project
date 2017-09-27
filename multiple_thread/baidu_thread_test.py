#coding=utf-8
from selenium import webdriver
import threading, time

def test_baidu(browser, search):
    print("test start: %s %s" % (browser, search))

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
    elif browser == 'ie':
        driver = webdriver.Ie(executable_path=r'C:\Python36\IEDriverServer.exe')
    elif browser == 'firefox':
        driver = webdriver.Firefox(executable_path=r'C:\Python36\geckodriver.exe')
    else:
        print("args error, must be ie, chrome, firefox")

    #driver.implicitly_wait(10)
    driver.get("http://www.baidu.com")
    driver.find_element_by_id("kw").clear()
    driver.find_element_by_id("kw").send_keys(search)
    time.sleep(2)
    print("test end: %s %s" % (browser, search))
    driver.quit()

if __name__ == '__main__':
    lists = {'ie': 'webdriver', 'chrome': 'threading', 'firefox': 'unittest'}
    files = range(len(lists))
    threads = []

    for browser, search in lists.items():
        t = threading.Thread(target=test_baidu, args=(browser, search))
        threads.append(t)

    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print('All thread test end %s' % time.ctime())
