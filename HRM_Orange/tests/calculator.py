import random
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Calculator(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Browser_drivers/chromedriver.exe")
        self.driver.get("http://www.math.com/students/calculators/source/basic.htm")
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.quit()

    def test_add_numbers(self):
        driver = self.driver

        num1 = random.randint(0, 9)

        driver.find_element(By.XPATH, "/html/body/table[4]/tbody/tr[1]/td[3]/center/form/table/tbody/tr[2]/td/div/input[1]").click()
        driver.find_element(By.XPATH, "/html/body/table[4]/tbody/tr[1]/td[3]/center/form/table/tbody/tr[2]/td/div/input[4]").click()
        driver.find_element(By.XPATH, "/html/body/table[4]/tbody/tr[1]/td[3]/center/form/table/tbody/tr[2]/td/div/input[2]").click()
        driver.find_element(By.XPATH, "/html/body/table[4]/tbody/tr[1]/td[3]/center/form/table/tbody/tr[3]/td/div/input").click()
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
