from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

class EmployeePage:
    def __init__(self, driver):
        self.driver = driver
        self.dashboard = self.find_element(By.CLASS_NAME, "oxd-text--h6")
        self.profileImage = self.find_element(By.CLASS_NAME, "oxd-userdropdown-img")
        self.logoutLink = self.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.menuItems = self.find_elements(By.CLASS_NAME, "oxd-main-menu-item--name")
        self.inputFields = self.find_elements(By.CLASS_NAME, "oxd-input")
        self.selectButtons = self.find_elements(By.CLASS_NAME, "oxd-select-text-input")
        self.submitButtons = self.find_elements(By.CSS_SELECTOR, "[type=submit]")

    def find_element(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((by, value)))

    def find_elements(self, by, value):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((by, value)))

    def select_nationality(self):
        nationality_button = self.selectButtons[0]
        nationality_button.send_keys("b")
        nationality_button.send_keys(Keys.ARROW_DOWN)
        nationality_button.send_keys(Keys.ARROW_DOWN)
        nationality_button.send_keys(Keys.ENTER)
        self.submitButtons[0].click()

    def select_blood_group(self):
        blood_group_button = self.selectButtons[2]
        blood_group_button.send_keys(Keys.ARROW_DOWN)
        blood_group_button.send_keys(Keys.ENTER)
        self.submitButtons[1].click()

# # Example Usage:
# # Assuming you have a WebDriver instance (e.g., ChromeDriver) named 'driver'
# employee_page = EmployeePage(driver)
# employee_page.select_nationality()
# employee_page.select_blood_group()
