from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from utils.Utils import Utils

class PersonalDetailPage:
    def __init__(self, driver):
        self.top_bar_item = self.top_bar_item
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.fake = Faker()

        # Initialize page elements
        self.topBarItem = self.driver.find_elements(By.CLASS_NAME, "oxd-topbar-body-nav-tab-item")
        self.txtInput = self.driver.find_elements(By.CLASS_NAME, "oxd-input")
        self.userMenu = self.driver.find_elements(By.CLASS_NAME, "oxd-main-menu-item")
        self.dropdown = self.driver.find_elements(By.CLASS_NAME, "oxd-select-text-input")
        self.radioBtn = self.driver.find_elements(By.CLASS_NAME, "oxd-radio-input")
        self.contactDetails = self.driver.find_elements(By.CLASS_NAME, "orangehrm-tabs-item")
        self.dropdownCountry = self.driver.find_element(By.CLASS_NAME, "oxd-select-text-input")
        self.Submit = self.driver.find_elements(By.CSS_SELECTOR, "[type=submit]")

    def choose_gender(self):
        self.radioBtn[1].click()
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type=submit]"))).click()

    def choose_blood_type(self):
        dropdown_element = self.dropdown[2]
        dropdown_element.click()

        for _ in range(2):
            dropdown_element.send_keys(Keys.ARROW_DOWN)
            self.wait.until(EC.visibility_of(dropdown_element))

        dropdown_element.send_keys(Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type=submit]"))).click()

    def choose_contact(self):
        self.contactDetails[1].click()
        self.wait.until(EC.visibility_of(self.txtInput[1]))

        street_address = self.fake.address().street_address()
        self.txtInput[1].send_keys(street_address)
        self.txtInput[2].send_keys(street_address)

        city = self.fake.address().city()
        self.txtInput[3].send_keys(city)

        state = self.fake.address().state()
        self.txtInput[4].send_keys(state)

        postal_code = self.fake.address().zip_code()
        self.txtInput[5].send_keys(postal_code)

        self.dropdownCountry.click()

        for _ in range(2):
            self.dropdownCountry.send_keys(Keys.ARROW_DOWN)
            self.wait.until(EC.visibility_of(self.dropdownCountry))

        self.dropdownCountry.send_keys(Keys.ENTER)

        self.txtInput[7].send_keys("+01722023445")

        email = f"test{Utils.generate_number(100, 999)}@gmail.com"
        self.txtInput[9].send_keys(email)

        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "[type=submit]"))).click()