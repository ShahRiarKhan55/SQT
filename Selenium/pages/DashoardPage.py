from selenium.webdriver.common.by import By


class DashboardPage:
    def __init__(self, driver):
        self.driver = driver
        self.btn_profile_tab = driver.find_element(By.CLASS_NAME, "oxd-userdropdown-tab")
        self.link_logout = driver.find_element(By.PARTIAL_LINK_TEXT, "Logout")
        self.menus = driver.find_elements(By.CLASS_NAME, "oxd-main-menu-item--name")
        self.dropdowns = driver.find_elements(By.CLASS_NAME, "oxd-select-text-input")

    def do_logout(self):
        self.btn_profile_tab.click()
        self.link_logout.click()
