import pytest
import time
from faker import Faker
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from pages.EmployeePage import EmployeePage
from utils.Utils import Utils
from pages.DashoardPage import DashboardPage
from pages.LoginPage import LoginPage
from pages.PersonalDetailPage import PersonalDetailPage
from pages.PimPage import PimPage
from setup.conftest import setup


@pytest.mark.usefixtures("setup")
class TestEmployee:

    def test_login(self, setup):
        self.driver = setup
        self.loginPage = LoginPage(self.driver)
        self.employeePage = EmployeePage(self.driver)

        users_list = Utils.load_json_files("../resources/Cred.json", 0)
        user_obj = users_list[-1]
        user_name = user_obj["username"]
        password = user_obj["password"]

        self.loginPage.do_login(user_name, password)
        assert self.employeePage.dashboard.is_displayed()

    def test_create_employee_without_username(self, setup):
        self.driver = setup
        dashboard_page = DashboardPage(self.driver)
        personal_detail_page = PersonalDetailPage(self.driver)
        dashboard_page.menus.get(1).click()
        personal_detail_page.top_bar_item.get(2).click()
        time.sleep(3)

        pim_page = PimPage(self.driver)

        faker = Faker()
        firstname = faker.name().first_name()
        lastname = faker.name().last_name()
        empId = Utils.generate_number(10000, 99999)
        employeeId = str(empId)
        password = "P@ssword123"
        confirm_password = password
        time.sleep(1.5)

        pim_page.create_employee_without_username(firstname, lastname, employeeId, password, confirm_password)

        header_actual = self.driver.find_elements(By.CLASS_NAME, "oxd-text")[15].text.strip()
        header_expected = "Required"
        assert header_actual.contains(header_expected)
        self.driver.refresh()

    def test_create_employee_1(self, setup):
        self.driver = setup
        dashboard_page = DashboardPage(self.driver)
        personal_detail_page = PersonalDetailPage(self.driver)
        pim_page = PimPage(self.driver)

        dashboard_page.menus.get(1).click()
        personal_detail_page.top_bar_item.get(2).click()
        time.sleep(3)

        faker = Faker()
        first_name = faker.name().first_name()
        last_name = faker.name().last_name()
        emp_id_int = Utils.generate_number(10000, 99999)
        emp_id_str = str(emp_id_int)

        emp_id_input = pim_page.inputFields.get(4)
        emp_id_input.clear()
        emp_id_input.send_keys(Keys.CONTROL + "a")
        emp_id_input.send_keys(emp_id_str)

        username = "test" + str(Utils.generate_number(1000, 9999))
        password = "P@ssword123"
        confirm_password = password
        time.sleep(5)

        pim_page.add_employee(first_name, last_name, username, emp_id_str, password, confirm_password)
        time.sleep(7)

        header_actual = self.driver.find_element(By.CLASS_NAME, "orangehrm-main-title").text.strip()
        header_expected = "Personal Details"
        assert header_actual.contains(header_expected)

        Utils.add_json_list(first_name, last_name, emp_id_str, username, password, confirm_password)

        personal_detail_page.top_bar_item.get(2).click()
        time.sleep(3)

    def test_create_employee1(self):
        self.dashboardPage = DashboardPage(self.driver)
        self.dashboardPage.menus[1].click()  # Click on PIM menu

        self.pDetailPage = PersonalDetailPage(self.driver)
        self.pDetailPage.topBarItem[2].click()  # Click on add employee
        time.sleep(3)

        self.pimPage = PimPage(self.driver)
        faker = Faker()
        first_name = faker.first_name()
        last_name = faker.last_name()

        utils = Utils()
        emp_id_int = utils.generate_number(10000, 99999)
        emp_id_str = str(emp_id_int)

        emp_id_input = self.pimPage.inputFields[4]
        emp_id_input.clear()
        emp_id_input.send_keys(Keys.CONTROL + "a")
        emp_id_input.send_keys(emp_id_str)

        username = "test" + str(utils.generate_number(1000, 9999))
        password = "P@ssword123"
        confirm_password = password

        time.sleep(5)
        self.pimPage.add_employee(first_name, last_name, username, emp_id_str, password, confirm_password)
        time.sleep(7)

        header_actual = self.driver.find_element(By.CLASS_NAME, "orangehrm-main-title").text
        header_expected = "Personal Details"

        utils.add_json_list(first_name, last_name, emp_id_str, username, password, confirm_password)

        self.pDetailPage.topBarItem[2].click()
        time.sleep(3)

    def test_create_employee2(self):
        self.pimPage = PimPage(self.driver)
        faker = Faker()
        first_name = faker.first_name()
        last_name = faker.last_name()

        utils = Utils()
        emp_id_int = utils.generate_number(10000, 99999)
        emp_id_str = str(emp_id_int)

        emp_id_input = self.pimPage.inputFields[4]
        emp_id_input.clear()
        emp_id_input.send_keys(Keys.CONTROL + "a")
        emp_id_input.send_keys(emp_id_str)

        username = "test" + str(utils.generate_number(1000, 9999))
        password = "P@ssword123"
        confirm_password = password

        time.sleep(5)
        self.pimPage.add_employee(first_name, last_name, username, emp_id_str, password, confirm_password)
        time.sleep(7)

        header_actual = self.driver.find_element(By.CLASS_NAME, "orangehrm-main-title").text
        header_expected = "Personal Details"

        utils.add_json_list(first_name, last_name, emp_id_str, username, password, confirm_password)

    def test_search_employee(self, setup):
        self.driver = setup
        self.pimPage = PimPage(self.driver)
        self.personalDetailPage = PersonalDetailPage(self.driver)
        self.pimPage.click_on_pim()

        file_name = "../resources/Cred.json"
        json_array = Utils.read_json_array(file_name)
        index_of_first_emp = len(json_array) - 2

        first_emp = json_array[index_of_first_emp]
        first_emp_id = first_emp["empIdStr"]

        time.sleep(2.5)
        self.pimPage.inputFields[1].send_keys(first_emp_id)
        self.pimPage.submitBtn.click()

        Utils.scroll_down(self.driver)
        time.sleep(0.5)
        self.pimPage.employeeList.click()
        time.sleep(3.5)

        actual_record_emp1 = self.pimPage.inputFields[5].get_attribute("value")
        print(actual_record_emp1)

        expected_record_emp1 = first_emp_id

    def test_update_employee(self, setup):
        self.driver = setup
        self.pimPage = PimPage(self.driver)
        emp_id = Utils.generate_number(10000, 99999)
        random_employee_id = str(emp_id)
        Utils.update_emp("../resources/Cred.json", "employeeId", random_employee_id, 0)
        Utils.scroll_down(self.driver)
        self.pimPage.update_employee(random_employee_id)
        time.sleep(1.5)

        header_actual = self.driver.find_elements(By.CLASS_NAME, "orangehrm-main-title")[0].text
        header_expected = "Personal Details"

    def test_search_employee_id(self, setup):
        self.driver = setup
        self.loginPage = LoginPage(self.driver)
        self.dashboardPage = DashboardPage(self.driver)
        self.dashboardPage.menus[1].click()
        user_object = Utils.load_json_files("../resources/Cred.json", 0)
        employee_id = user_object["employeeId"]
        self.pimPage.find_employee(employee_id)
        time.sleep(1.5)
        Utils.scroll_down(self.driver)

        message_actual = self.driver.find_elements(By.CLASS_NAME, "oxd-text--span")[11].text
        message_expected = "Record Found"

    def test_logout(self, setup):
        self.driver = setup
        dashboard_page = DashboardPage(self.driver)
        dashboard_page.do_logout()
