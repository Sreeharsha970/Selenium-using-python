# import driver
import pytest
import time
from selenium import webdriver
# from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from POMDemo.tests.pages.login_page import Loginpage


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    yield driver
    driver.close()
    driver.quit()


def test_login(driver):
    login_page = Loginpage(driver)
    login_page.open_page("https://trytestingthis.netlify.app/")
    time.sleep(2)
    login_page.enter_username("test")
    time.sleep(2)
    login_page.enter_password("test")
    time.sleep(2)
    login_page.click_login()
    time.sleep(2)

    # driver.get("https://trytestingthis.netlify.app/")
    # username_field = driver.find_element(By.ID, "uname")
    # password_field = driver.find_element(By.ID, "pwd")
    # submit_button = driver.find_element(By.XPATH, "//input[@value='Login']")
    #
    # username_field.send_keys()
    # password_field.send_keys()
    # time.sleep(2)
    # submit_button.click()
    # assert 'Successfully' in driver.page_source
    # time.sleep(2)
