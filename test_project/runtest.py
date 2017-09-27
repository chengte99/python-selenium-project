import unittest, time
from HTMLTestRunner import HTMLTestRunner

'''
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
'''

# 使用Atom跑的話, 當前目錄為Python Project(當前所開的最上層資料夾)
#test_dir = './test_project/test_case'

# 使用window cmd跑的話 需要改成以runtest.py當前目錄下
# HTMLTestRunner 必須放在當前目錄
test_dir = './test_case'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = './' + now + '_result.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp, title='測試報告', description='案例情況:')
    runner.run(discover)

    fp.close()
