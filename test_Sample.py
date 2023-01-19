import time
from uuid import uuid4

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class Test_Sample():

    def test_sample(self):
        self.driver.get("https://accounts.staging.joveo.com")
        assert self.driver.title == "Joveo Account"
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Email']").send_keys(
            "chakradhar+mojopro@joveo.com")
        self.driver.find_element(By.XPATH, "//input[@data-placeholder='Password']").send_keys("Joveo@1234567890")
        self.driver.find_element(By.XPATH, "//span[text()=' Log In ']").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "/html/body/app-root/app-home/div[2]/div/div[1]/button").click()
        self.driver.find_element(By.XPATH,
                                 "/html/body/jv-root/jv-home/mat-toolbar/div/div[3]/button/span[1]/mat-icon").click()

        self.driver.find_element(By.XPATH, "//span[text()='Publisher Management']").click()
        self.driver.find_element(By.XPATH, "//a[text()=' Publisher Setup ']").click()
        self.driver.find_element(By.XPATH, "//span[text()='Add Publisher']").click()
