# import pytest
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
#
#
# @pytest.fixture(autouse=True)
# def setup(request):
#     driver = webdriver.Chrome()
#     wait = WebDriverWait(driver, 10)
#     driver.get("http://localhost/web/index.php/auth/login")
#     driver.maximize_window()
#     print(driver.title)
#     request.cls.driver = driver
#     request.cls.wait = wait
#     driver.close()
#     yield
#     driver.quit()
import time

import pytest
from selenium import webdriver
from selenium.common import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.LoginPage import LoginPage
from pages.PimPage import PimPage


@pytest.fixture(scope="class", autouse=True)
def setup(request):

    try:
        # ChromeDriver setup
        driver = webdriver.Chrome()
        wait = WebDriverWait(driver, 10)

        # Maximize window and set implicit wait
        driver.get("http://localhost/web/index.php/auth/login")
        print(driver.title)
        driver.maximize_window()
        login_page = LoginPage(driver)
        driver.implicitly_wait(5)

        request.cls.wait = wait
        request.cls.driver = driver
        request.cls.login_page = login_page


        yield driver
        btn_profile_tab = driver.find_element(By.CSS_SELECTOR, ".oxd-user dropdown-img")
        link_logout = driver.find_element(By.XPATH, "//a[normalize-space()='Logout']")
        time.sleep(10)
        btn_profile_tab.click()
        link_logout.click()
        driver.quit()
    except WebDriverException as e:
        print(f"WebDriverException: {e}")
