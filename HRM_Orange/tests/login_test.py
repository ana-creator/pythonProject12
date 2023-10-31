import time
import unittest

from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# s=Service("C:\\Users\\Gavri\\PycharmProjects\\HRM_Orange\\tests\\chromedriver.exe")
# driver=webdriver.Chrome(service=s)
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



class MyTestCase(unittest.TestCase):

    def setUp(self):     # setUp is special method with data before even test was started

        self.driver = webdriver.Chrome(executable_path="/Browser_drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        time.sleep(2)

    # skip("disabling for debugging")
    def test_valid_login(self):
        driver = self.driver
        driver.maximize_window()

        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin",Keys.RETURN)
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)

        welcome_text = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[1]/header/div[1]/div[1]/span/h6").text
        time.sleep(2)
        self.assertEqual('PIM', welcome_text)  # add assertion here
        time.sleep(2)
    def test_invalid_password(self):
        driver = self.driver
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin", Keys.RETURN)
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin128')
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)
        invalid_cred = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']").text
        self.assertEqual("Invalid credentials", invalid_cred)

    def test_empty_password(self):
        driver = self.driver
        driver.maximize_window()
        driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input').send_keys("Admin", Keys.RETURN)
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)
        required = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/span").text
        self.assertEqual("Required", required)



if __name__ == '__main__':
    unittest.main()
