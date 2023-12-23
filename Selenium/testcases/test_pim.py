import pytest
import time

from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.LoginPage import LoginPage
from pages.PimPage import PimPage
from pages.DashoardPage import DashboardPage
from utils.Utils import Utils
from setup.conftest import setup

@pytest.mark.usefixtures("setup")
class TestPIMPage():
    def test_login(self, setup):
        driver = setup
        login_page = LoginPage(driver)
        login_page.do_login("parvez", "Israa2001@")
        time.sleep(5)
        actual_url = driver.current_url
        expected_url = "dashboard"
        assert expected_url in actual_url
        # element_to_hover_over = driver.find_elements(By.XPATH, "//a[@class='oxd-main-menu-item active']")
        # actions = ActionChains(driver)
        # actions.move_to_element(element_to_hover_over).perform()

    @pytest.mark.priority(1)
    def test_employment_status_full_time_permanent(self,setup):
        self.driver = setup
        try:
            self.pim_page = PimPage(self.driver)
            self.driver.execute_script("window.scrollTo(0, 0);")
            self.pim_page.select_employment_status(self.driver, 3)
            time.sleep(5)
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            table = self.driver.find_element(By.CLASS_NAME, "oxd-table-body")
            all_rows = table.find_elements(By.CSS_SELECTOR, "[role=row]")
            for row in all_rows:
                all_cells = row.find_elements(By.CSS_SELECTOR, "[role=cell]")
                assert "Permanent" in all_cells[5].text
        except TimeoutException as te:

            print(f"TimeoutException occurred: {te}")
    @pytest.mark.priority(2)
    def test_employment_status_full_time_probation(self,setup):
        driver = setup
        try:
            Utils.scroll_up(driver)
            self.pim_page = PimPage(driver)
            driver.execute_script("window.scrollTo(0, 0);")
            self.pim_page.select_employment_status(driver, 4)
            Utils.scroll_down(driver)
            table = driver.find_element_by_class_name("oxd-table-body")
            action_chains = ActionChains(driver)
            action_chains.move_to_element(table).perform()
            all_rows = table.find_elements_by_css_selector("[role=row]")
            for row in all_rows:
                all_cells = row.find_elements(By.CSS_SELECTOR, "[role=cell]")
                assert "Full-Time Probation" in all_cells[5].text
        except TimeoutException as te:

            print(f"TimeoutException occurred: {te}")
    @pytest.mark.priority(3)
    def test_add_first_employee(self, setup):
        try:
            driver = setup
            login_page = LoginPage(driver)
            login_page.do_login("parvez", "Israa2001@")

            pim_page = PimPage(driver)
            PIM_page = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-text oxd-text--span oxd-main-menu-item--name"))
            )

            for index, span_element in enumerate(PIM_page, start=1):
                # Print the text content of each span element
                span_text = span_element.text
                span_text.click()
                print(f"Text content of span element {index}: {span_text}")

            pim_page.addEmployeeLinkText.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )

            faker = Faker()
            first_name = faker.first_name()
            last_name = faker.last_name()
            user_name = faker.user_name()
            employee_id = pim_page.inputFields[4].get_attribute("value")
            password = "Str0ngP@ssword"

            pim_page.add_employee(first_name, last_name, user_name, password, password)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".message.success"))
            )

            expected_name = first_name + " " + last_name
            list_h6 = driver.find_elements(By.TAG_NAME, "h6")
            WebDriverWait(driver, 10).until(
                EC.visibility_of(list_h6[1])
            )

            actual_name = list_h6[1].text
            assert expected_name in actual_name

            if list_h6[1].is_displayed():
                Utils.add_json_list(user_name, password, employee_id)


        except TimeoutException as te:

            print(f"TimeoutException occurred: {te}")
    @pytest.mark.priority(4)
    def test_add_second_employee(self,setup):
        try:
            driver = setup
            login_page = LoginPage(driver)
            login_page.do_login("parvez", "Israa2001@")

            pim_page = PimPage(driver)
            PIM_page = WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located((By.CLASS_NAME, "oxd-text oxd-text--span oxd-main-menu-item--name"))
            )

            for index, span_element in enumerate(PIM_page, start=1):
                # Print the text content of each span element
                span_text = span_element.text
                span_text.click()
                print(f"Text content of span element {index}: {span_text}")

            pim_page.addEmployeeLinkText.click()
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "firstName"))
            )

            faker = Faker()
            first_name = faker.first_name()
            last_name = faker.last_name()
            user_name = faker.user_name()
            employee_id = pim_page.inputFields[4].get_attribute("value")
            password = "Str0ngP@ssword"

            pim_page.add_employee(first_name, last_name, user_name, password, password)
            WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".message.success"))
            )

            expected_name = first_name + " " + last_name
            list_h6 = driver.find_elements(By.TAG_NAME, "h6")
            WebDriverWait(driver, 10).until(
                EC.visibility_of(list_h6[1])
            )

            actual_name = list_h6[1].text
            assert expected_name in actual_name

            if list_h6[1].is_displayed():
                Utils.add_json_list(user_name, password, employee_id)


        except TimeoutException as te:

            print(f"TimeoutException occurred: {te}")
    def test_logout(self,setup):
        self.driver = setup
        self.driver.btn_profile_tab.click()
        self.driver.link_logout.click()

