import random
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class AddEmployee(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path="/Browser_drivers/chromedriver.exe")
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        self.driver.maximize_window()
        time.sleep(2)
    def tearDown(self):
        self.driver.quit()

    def test_something(self):
        empId = random.randint(10000, 999999)
        # expected_job_title = "QA Manager"        - best practic poin expected result on the top of test
        # expected_employment_status = "Full-Time"


        # login
        # click the Add button
        # Enter First and Last name
        # Enter and remember the empId
        # Save the Employee
        # Go to PIM
        # Search by EmpId

        # Expected: 1 record back
        # Expected Correct Name and EmpId
        driver = self.driver
        # driver.maximize_window()

        driver.find_element(By.XPATH,"//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input").send_keys("Admin")
        time.sleep(2)

        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('admin123')
        time.sleep(2)

        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button").click()
        time.sleep(2)

        # click the Add button
        driver.find_element(By.XPATH, "//button[normalize-space()='Add']").click()
        #  TODO Anna: may need to come back and do something

        # Enter First and Last name
        driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Anna")
        driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Dada")
        # Enter and remember the empId
        driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").clear()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']").send_keys(empId)
        # Save the Employee
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div/form/div[2]/button[2]").click()
        # Go to PIM
        driver.find_element(By.XPATH, "//a[@class='oxd-main-menu-item active']").click()
        #  TODO Anna: may need to come back and do something also

        # Search by EmpId
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/input").send_keys(empId)
        driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]").click()

        # Expected: 1 record back
        lst = driver.find_elements_by_xpath("//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div[1]/div/div[2]")
        self.assertTrue(len(lst) == 1)
        # Expected Correct Full Name

        lastName = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[4]/div").text
        firstName = driver.find_element(By.XPATH, "//*[@id='app']/div[1]/div[2]/div[2]/div/div[2]/div[3]/div/div[2]/div/div/div[3]/div").text

        massage = "Expected the table to contain first name '{0}' but instead the value was '{1}'"
        self.assertEqual("Anna", firstName, message.format(expected_first_name, firstName))  # add assertion here
        self.assertEqual("Dada", lastName)  # add assertion here


if __name__ == '__main__':
    unittest.main()
