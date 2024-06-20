# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class TestMySuite1():
    def setup_method(self, method):
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_myTest2(self):
        self.driver.get("https://trytestingthis.netlify.app/index.html")
        self.driver.set_window_size(1382, 736)
        self.driver.find_element(By.CSS_SELECTOR, "button:nth-child(1)").click()
        assert self.driver.switch_to.alert.text == "Press a button!"
        self.driver.switch_to.alert.accept()
        self.driver.find_element(By.ID, "fname").click()
        self.driver.find_element(By.ID, "fname").send_keys("sree")
        self.driver.find_element(By.ID, "lname").click()
        self.driver.find_element(By.ID, "lname").send_keys("harsha")
        self.driver.find_element(By.ID, "male").click()
        self.driver.find_element(By.ID, "option").click()
        dropdown = self.driver.find_element(By.ID, "owc")
        dropdown.find_element(By.XPATH, "//option[. = 'Option 1']").click()
        self.driver.find_element(By.NAME, "option2").click()
        self.driver.find_element(By.NAME, "Options").click()
        self.driver.find_element(By.NAME, "Options").send_keys("Vanilla")
        self.driver.find_element(By.ID, "favcolor").click()
        self.driver.find_element(By.ID, "favcolor").send_keys("#00d150")
        self.driver.find_element(By.CSS_SELECTOR, "fieldset:nth-child(1)").click()
        element = self.driver.find_element(By.ID, "a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click_and_hold().perform()
        element = self.driver.find_element(By.ID, "a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element = self.driver.find_element(By.ID, "a")
        actions = ActionChains(self.driver)
        actions.move_to_element(element).release().perform()
        self.driver.find_element(By.ID, "a").send_keys("100")
        self.driver.find_element(By.ID, "a").click()
        self.driver.find_element(By.NAME, "message").click()
        self.driver.find_element(By.NAME, "message").send_keys("The cat was playing in the garden.\\nok good")
        elements = self.driver.find_elements(By.CSS_SELECTOR, ".btn")
        assert len(elements) > 0
        self.driver.find_element(By.ID, "uname").click()
        self.driver.find_element(By.ID, "uname").send_keys("test")
        self.driver.find_element(By.ID, "pwd").click()
        self.driver.find_element(By.ID, "pwd").send_keys("test")
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(10)").click()
        self.driver.find_element(By.LINK_TEXT, "here").click()
        elements = self.driver.find_elements(By.CSS_SELECTOR, "h2")
        assert len(elements) > 0
