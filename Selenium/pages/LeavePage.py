from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import selenium

class LeavePage:
    def __init__(self,driver):
        self.driver = driver
        self.leaveMenu = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "menu_leave_viewLeaveModule"))
        )
        self.assignLeaveLink = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.ID, "menu_leave_applyLeave"))
        )
        self.leaveTypeDropdown = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".oxd-icon.bi-caret-down-fill.oxd-select-text--arrow"))
        )
        self.fromDateInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-grid-4 orangehrm-full-width-grid"))
        )
        self.toDateInput = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "oxd-grid-4 orangehrm-full-width-grid"))
        )
        self.commentInput = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-textarea oxd-textarea--active oxd-textarea--resize-vertical"))
        )
        self.assignButton = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "[type=submit]"))
        )
        self.successMessage = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".message.success"))
        )
    def assign_leave(self, leave_type, from_date, to_date, comment):
        self.leaveMenu.click()
        self.assignLeaveLink.click()
        self.leaveTypeDropdown.click()
        leave_type_option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, "li[id^='applyleave_leaveType'][data-value='" + leave_type + "']"))
        )
        leave_type_option.click()
        self.fromDateInput.clear()
        self.fromDateInput.send_keys(from_date)
        self.toDateInput.clear()
        self.toDateInput.send_keys(to_date)
        self.commentInput.send_keys(comment)
        self.assignButton.click()

    def verify_leave_application_success(self):
        return EC.presence_of_element_located((By.CSS_SELECTOR, ".message.success"))
