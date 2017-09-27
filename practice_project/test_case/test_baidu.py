#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from HTMLTestRunner import HTMLTestRunner

class TestBaidu(unittest.TestCase):
    '''百度測試'''
    def setUp(self):
        print("Test start:")
        self.driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.base_url = "http://www.baidu.com"
        self.driver.get(self.base_url)
        self.driver.maximize_window()

    def test_baidu_back_page(self):
        '''百度搜尋, 回上一頁'''
        driver = self.driver
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium 2")
        time.sleep(2)
        driver.execute_script("window.history.go(-1)")
        driver.get(self.base_url)
        time.sleep(2)

    def test_baidu_switch_page_action(self):
        '''百度搜尋, 開啟連結, 切換分頁'''
        driver = self.driver
        main_window = driver.current_window_handle

        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("selenium")
        time.sleep(2)
        driver.find_element_by_xpath("//h3[@class='t c-title-en']/a").click()
        time.sleep(3)

        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != main_window:
                driver.switch_to.window(handle)
                text = driver.find_element_by_xpath("//div[@id='mainContent']/h2").text
                print(text)
                driver.find_element_by_xpath("//li[@id='menu_download']/a").click()
                title = driver.title
                print(title)
                time.sleep(3)
                java_change_log_element = driver.find_element_by_xpath("//*[@id='mainContent']/table[1]/tbody/tr[1]/td[5]/a")
                python_change_log_element = driver.find_element_by_xpath("//div[@id='mainContent']/table[1]/tbody/tr[4]/td[5]/a")
                driver.execute_script("return arguments[0].scrollIntoView(true)", java_change_log_element)
                python_change_log_element.click()
                time.sleep(5)

        driver.switch_to.window(driver.window_handles[0])
        print(driver.title)
        time.sleep(3)

    def tearDown(self):
        print("Test end!")
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
    '''
    suite = unittest.TestSuite()
    suite.addTest(TestBaidu('test_baidu_action'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
    '''
