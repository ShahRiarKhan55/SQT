
import time
import pytest
from selenium import webdriver
from selenium.common import TimeoutException

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage
from pages.DashoardPage import DashboardPage
from setup.conftest import setup

@pytest.mark.usefixtures("setup")
class TestLogin:
    def test_failed_login(self,setup):
        driver = setup
        login_page = LoginPage(driver)

        login_page.do_login("parvez", "Wrong Password")
        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))
        )
        expected_text = "Invalid credentials"
        actual_text = element.text
        assert expected_text in actual_text
        time.sleep(2)

    def test_login(self,setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.do_login("parvez", "Israa2001@")
        time.sleep(5)
        actual_url = self.driver.current_url
        expected_url = "dashboard"
        assert expected_url in actual_url

    # def test_profile_image_existence(self,setup):
    #     driver = setup
    #     image_exist = driver.find_element(By.CLASS_NAME, ".oxd-user dropdown-img").is_displayed()
    #     assert image_exist

    def test_logout(self,setup):
        self.dashboard = setup
        self.dashboard.btn_profile_tab.click()
        self.dashboard.link_logout.click()

    # def test_failed_login(self,setup):
    #     driver = setup
    #     login_page = LoginPage(driver)
    #
    #     login_page.do_login("parvez", "Wrong Password")
    #     element = WebDriverWait(driver, 10).until(
    #         EC.presence_of_element_located((By.CLASS_NAME, "oxd-alert-content-text"))
    #     )
    #     expected_text = "Invalid credentials"
    #     actual_text = element.text
    #     assert expected_text in actual_text
    #     time.sleep(2)