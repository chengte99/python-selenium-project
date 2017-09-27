import time, unittest
from HTMLTestRunner import HTMLTestRunner

test_dir = './practice_project/test_case'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')

if __name__ == '__main__':
    now = time.strftime("%Y-%m-%d_%H-%M-%S")
    filename = './practice_project/report/' + now + '_report.html'

    fp = open(filename, 'wb')

    runner = HTMLTestRunner(stream=fp, title='測試報告', description='測試案例情況')
    runner.run(discover)

    fp.close()
