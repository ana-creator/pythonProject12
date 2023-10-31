import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from fixtures.base import BaseTestCase


class MyTestCase(BaseTestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Browser_drivers/chromedriver.exe")
        self.driver.get("http://hrm-online.portnov.com/symfony/web/index.php/auth/login")
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()

    def test_valid_login(self):
        driver = self.driver
        driver.maximize_window()

        driver.find_element(By.ID, "txtUsername").send_keys("admin")
        time.sleep(2)

        driver.find_element(By.ID, "txtPassword").send_keys('password')
        time.sleep(2)

        driver.find_element(By.ID,"btnLogin").click()
        time.sleep(2)

        logo_element = driver.find_element(By.ID, "//*[@id='branding']/img")
        time.sleep(2)
        # driver.find_element_by_css_selector("#branding > img")
        # driver.find_element(By.ID, 'branding').find_element(By.XPATH(//img")

        logo_size = logo_element.size
        time.sleep(2)
        self.assertEqual(56, logo_size.get("height"))
        time.sleep(2)
        self.assertTrue(logo_size.get("width") == 283)
        time.sleep(2)
        self.assertDictEqual({'width': 283, 'height': 56}, logo_size)
        time.sleep(2)




if __name__ == '__main__':
    unittest.main()
