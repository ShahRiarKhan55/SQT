import json
import random
from json.decoder import JSONDecodeError
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Utils:
    @staticmethod
    def scroll_down(driver):
        js = driver.execute_script
        js("window.scrollBy(0,document.body.scrollHeight)")

    @staticmethod
    def scroll_up(driver):
        js = driver.execute_script
        js("window.scrollBy(0, -document.body.scrollHeight)")

    @staticmethod
    def load_json_files(file_location, index):
        with open(file_location, 'r') as file:
            data = json.load(file)
            return data[index]

    @staticmethod
    def wait_for_element(driver, web_element, time_unit_sec):
        wait = WebDriverWait(driver, time_unit_sec)
        wait.until(EC.visibility_of(web_element))

    @staticmethod
    def generate_number(min_val, max_val):
        return round((max_val - min_val) * random.random() + min_val)

    @staticmethod
    def add_json_list(first_name, last_name, emp_id_str, username, password, confirm_password):
        file_name = "./seleniumProject/resources/UserList.json"

        try:
            with open(file_name, 'r') as file:
                json_data = json.load(file)
        except JSONDecodeError:
            json_data = []

        user_obj = {
            "firstname": first_name,
            "lastname": last_name,
            "empIdStr": emp_id_str,
            "username": username,
            "password": password,
            "confirmPassword": confirm_password
        }

        json_data.append(user_obj)

        with open(file_name, 'w') as file:
            json.dump(json_data, file, indent=4)

    @staticmethod
    def update_emp(file_name, key, value, index):
        with open(file_name, 'r') as file:
            json_data = json.load(file)

        json_data[index][key] = value

        with open(file_name, 'w') as file:
            json.dump(json_data, file, indent=4)

    @staticmethod
    def read_json_array(file_name):
        with open(file_name, 'r') as file:
            json_data = json.load(file)
            return json_data

    @staticmethod
    def read_jsons_array(file_name):
        with open(file_name, 'r') as file:
            json_data = json.load(file)
            return json_data

