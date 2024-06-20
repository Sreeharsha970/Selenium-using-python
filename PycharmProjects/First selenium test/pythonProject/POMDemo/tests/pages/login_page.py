from selenium.webdriver.common.by import By


class Loginpage:

    def __int__(self, driver):  # send from arguments or give some values to variables
        self.driver = driver
        self.username_textbox = (By.ID, "uname")       # username textbox in loginpage
        self.password_textbox = (By.ID, "pwd")
        self.login_button = (By.XPATH, "//input[@value='Login']")

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        self.driver.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()




