#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

class TestGoogle(unittest.TestCase):
    '''Google測試'''
    def setUp(self):
        print("Test start:")
        self.driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.google.com")
        self.driver.maximize_window()

    def test_google_news(self):
        '''Google 新聞切換頁籤測試'''
        driver = self.driver
        driver.find_element_by_xpath("//*[@id='gbwa']/div[1]/a").click()
        driver.find_element_by_xpath("//*[@id='gb5']/span[1]").click()


        drop_down = driver.find_element_by_xpath("//*[@id='gb']/div[3]/div/c-wiz/div/div[1]/c-wiz/div")
        drop_down.click()
        time.sleep(2)

        select_item = driver.find_element_by_xpath("//div[@class='OA0qNb ncFHed' and @jsname='V68bde']/div[@data-value='cn']")
        #select_item = driver.find_element_by_xpath("//*[@id='gb']/div[3]/div/c-wiz/div/div[1]/c-wiz/div/div[2]/div[16]")
        select_item.click()
        time.sleep(2)

        drop_down = driver.find_element_by_xpath("//*[@id='gb']/div[3]/div/c-wiz/div/div[1]/c-wiz/div")
        drop_down.click()
        time.sleep(2)

        select_item = driver.find_element_by_xpath("//div[@class='OA0qNb ncFHed' and @jsname='V68bde']/div[@data-value='tw']")
        #select_item = driver.find_element_by_xpath("//*[@id='gb']/div[3]/div/c-wiz/div/div[1]/c-wiz/div/div[2]/div[16]")
        select_item.click()
        time.sleep(2)

        local = driver.find_element_by_xpath("//*[@id='gb']/div[3]/div/c-wiz/div/div[1]/div[1]/div/div[2]/content/span")
        local.click()
        time.sleep(2)

        recommand = driver.find_element_by_xpath("//*[@id='gb']/div[3]/c-wiz/div/div[1]/div[1]/div/div[3]/content/span")
        recommand.click()
        time.sleep(2)

        top = driver.find_element_by_xpath("//*[@id='gb']/div[3]/c-wiz/div/div[1]/div[1]/div/div[1]/content/span")
        top.click()
        time.sleep(2)

        national = driver.find_element_by_xpath("//*[@id='gb']/div[4]/div[2]/c-wiz/div/div/div/div/a[2]/content/div[2]/div/span[2]")
        national.click()
        time.sleep(2)

    def tearDown(self):
        print("Test end!")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    '''
    suite = unittest.TestSuite()
    suite.addTest(TestGoogle('test_login'))

    runner = unittest.TextTestRunner()
    runner.sun(suite)
    '''
