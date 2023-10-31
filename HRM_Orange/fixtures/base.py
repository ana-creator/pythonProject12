import time
import unittest

from selenium.webdriver.chrome import webdriver


class BaseTestCase(unittest.TestCase):
    def setUp(self):     # setUp is special method with data before even test was started
        self.driver = webdriver.Chrome(executable_path="/Browser_drivers/chromedriver.exe")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()
