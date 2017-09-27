from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
driver.implicitly_wait(10)
driver.get("http://www.baidu.com")
driver.maximize_window()

search_window = driver.current_window_handle

driver.find_element_by_link_text('登录').click()
driver.find_element_by_link_text('立即注册').click()

all_handles = driver.window_handles

for handle in all_handles:
    if handle != search_window:
        driver.switch_to.window(handle)
        print("This is register page")
        driver.find_element_by_name('userName').send_keys("username")
        driver.find_element_by_name('phone').send_keys("123456789")
        driver.find_element_by_name('verifyCode').send_keys("abcde")
        driver.find_element_by_xpath("//input[@id='TANGRAM__PSP_3__password' and @name='password']").send_keys("qwert")


for handle in all_handles:
    if handle == search_window:
        driver.switch_to.window(handle)
        print("This is login page")
        driver.find_element_by_name('userName').send_keys("username1")
        driver.find_element_by_name('password').send_keys("12345678")
