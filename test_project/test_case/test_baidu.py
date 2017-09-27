#coding=utf-8
from selenium import webdriver
import time, unittest

#import sys, io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class MyTest(unittest.TestCase):
    '''百度搜尋測試'''
    def setUp(self):
        print("test start")
        self.driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.base_url = "http://www.baidu.com"

    def test_baidu(self):
        '''搜尋關鍵字: unittest'''
        driver = self.driver
        driver.get(self.driver.base_url + '/')
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("unittest")
        time.sleep(2)
        title = driver.title
        #print(title)
        #self.assertEqual(title, "unittest_百度搜索")

    def tearDown(self):
        print("test end")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
