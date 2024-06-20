import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By

from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# driver.get("https://google.com")
#
# googleSearchBox = driver.find_element(By.ID, "APjFqb")
# googleSearchBox.send_keys("Automation")
# googleSearchBox.send_keys(Keys.RETURN)
# driver.find_element(By.NAME, "btnK").click()
#
# time.sleep(2)

driver.get("https://trytestingthis.netlify.app/index.html")
driver.find_element(By.ID, "fname").send_keys("Sree")    # firstname
driver.find_element(By.ID, "lname").send_keys("Harsha")  # lastname
time.sleep(2)
driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()    # submit button
time.sleep(5)
