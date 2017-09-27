from selenium import webdriver
from public import Login

class LoginTest():

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Python36\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get("http://www.126.com")

    def test_admin_login(self):
        Login().user_login(self.driver)
        #self.driver.quit()

    '''
    def test_guest_login(self):
        Login().user_logout(self.driver)
        self.driver.quit()
    '''

LoginTest().test_admin_login()
#LoginTest().test_guest_login()
