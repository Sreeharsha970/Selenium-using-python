import time

import pytest
from selenium import webdriver
import selenium.webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_google_search_test(driver):
    driver.get("https://google.com")

    googleSearchBox = driver.find_element(By.ID, "APjFqb")
    googleSearchBox.send_keys("selenium")
    googleSearchBox.send_keys(selenium.webdriver.Keys.RETURN)
    time.sleep(2)
    driver.close()
    driver.quit()
    print("Test completed")
