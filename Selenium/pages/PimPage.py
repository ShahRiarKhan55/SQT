import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PimPage:
    def __init__(self, driver):
        self.profileImage = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-user dropdown-img"))
        )
        self.logoutLink = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Logout"))
        )
        self.dropdowns = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "oxd-select-text-input"))
        )
        self.submitBtn = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[type=submit]"))
        )
        self.addEmployeeLinkText = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Add Employee"))
        )
        self.employeeList = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.PARTIAL_LINK_TEXT, "Employee List"))
        )
        self.checkBox = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-switch-input"))
        )
        self.inputFields = WebDriverWait(driver, 10).until(
            EC.visibility_of_all_elements_located((By.CLASS_NAME, "oxd-input"))
        )
        self.title = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "orangehrm-main-title"))
        )
        self.userNameErrorMessage = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-input-field-error-message"))
        )
        self.menu_item = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-main-menu-item"))
        )

    def add_employee(self, first_name, last_name, user_name,emp_id_str, password, confirm_password):
        self.checkBox.click()
        self.inputFields[1].send_keys(first_name)
        self.inputFields[3].send_keys(last_name)

        emp_id_input = self.inputFields[4]

        emp_id_input.clear()
        emp_id_input.send_keys(Keys.CONTROL + "a")
        emp_id_input.send_keys(emp_id_str)

        self.inputFields[5].send_keys(user_name)
        self.inputFields[6].send_keys(password)
        self.inputFields[7].send_keys(confirm_password)
        self.submitBtn.click()

    def check_user_name(self, user_name):
        self.checkBox.click()
        self.inputFields[5].send_keys(user_name)

    def find_employee(self, employee_id):
        self.inputFields[1].send_keys(employee_id)
        self.submitBtn.click()
    def select_employment_status(self, position):
        self.dropdowns[0].click()
        for i in range(position):
            self.dropdowns[0].send_keys(Keys.ARROW_DOWN)
        self.dropdowns[0].send_keys(Keys.ENTER)
        self.submitBtn.click()

    def create_employee_without_username(self, firstname, lastname, employee_id, password, confirm_password):
        self.inputFields[1].send_keys(firstname)
        self.inputFields[3].send_keys(lastname)

        emp_id_input = self.inputFields[4]
        time.sleep(1)
        emp_id_input.clear()
        emp_id_input.send_keys(Keys.CONTROL + "a")
        emp_id_input.send_keys(employee_id)

        self.submitBtn.click()

        self.inputFields[6].send_keys(password)  # input password
        self.inputFields[7].send_keys(confirm_password)  # confirm password
        time.sleep(1.5)
        self.submitBtn.click()

    def update_employee(self, employee_id):
        self.inputFields[5].send_keys(Keys.CONTROL + "a" + Keys.BACK_SPACE)
        time.sleep(1)
        self.inputFields[5].send_keys(employee_id)
        time.sleep(1.5)
        self.submitBtn.click()

    def click_on_pim(self):
        self.menu_item[1].click()
