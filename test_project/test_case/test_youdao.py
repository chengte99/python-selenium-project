#coding=utf-8
from selenium import webdriver
import time, unittest

#import sys, io
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class MyTest(unittest.TestCase):
    '''有道搜尋測試'''
    def setUp(self):
        print("test start")
        self.driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.base_url = "http://www.youdao.com"

    def test_youdao(self):
        '''搜尋關鍵字: selenium 2'''
        driver = self.driver
        driver.get(self.driver.base_url + '/')
        driver.find_element_by_xpath("//div[@id='border']/input[2]").clear()
        driver.find_element_by_xpath("//div[@id='border']/input[2]").send_keys("selenium 2")
        driver.find_element_by_xpath("//div[@class='wrap']/form/button").click()
        time.sleep(2)
        title = driver.title
        #print(title)

    def tearDown(self):
        print("test end")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
