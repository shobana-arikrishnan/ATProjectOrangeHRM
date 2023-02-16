import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from data.orangehrm_page_data import LoginPageData, EmployeeData
from locators.orangehrm_page_locators import LoginPageLocators, DashboardPageLocators


class OrangeHRM:

    def __init__(self, driver):
        self.url = LoginPageData().url
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 20)

    def browse(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        return self

    def login(self, username, password):
        try:
            username_locator = self.wait.until(
                EC.presence_of_element_located((By.NAME, LoginPageLocators().username_input)))
            password_locator = self.wait.until(
                EC.presence_of_element_located((By.NAME, LoginPageLocators().password_input)))
            submit_button = self.wait.until(EC.presence_of_element_located((By.XPATH, LoginPageLocators().LoginButton)))

            username_locator.send_keys(username)
            password_locator.send_keys(password)
            submit_button.click()

        except NoSuchElementException:
            print('Some of the elements are missing!')

    def get_error_text(self):
        error_msg_locator = self.wait.until(
            EC.presence_of_element_located((By.CLASS_NAME, LoginPageLocators().login_error_locator)))
        return error_msg_locator

    def add_employee(self):
        pim_option = self.wait.until(EC.presence_of_element_located((By.XPATH, DashboardPageLocators().pim_locator)))
        pim_option.click()
        add_employee_option = self.wait.until(
            EC.presence_of_element_located((By.XPATH, DashboardPageLocators().add_employee_locator)))
        add_employee_option.click()
        try:
            firstname_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, DashboardPageLocators().firstname_locator)))
            middlename_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, DashboardPageLocators().middle_name_locator)))
            lastname_input = self.wait.until(
                EC.presence_of_element_located((By.NAME, DashboardPageLocators().lastname_locator)))

            firstname_input.send_keys(EmployeeData().new_user_firstname)
            middlename_input.send_keys(EmployeeData().new_user_middlename)
            lastname_input.send_keys(EmployeeData().new_user_lastname)

            create_login_details_checkbox = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, DashboardPageLocators().create_login_details_checkbox_locator)))

            create_login_details_checkbox.click()

            username_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().username_locator)))
            password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().password_locator)))
            confirm_password_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().confirm_password_locator)))

            username_input.send_keys(EmployeeData().new_user_username)
            password_input.send_keys(EmployeeData().new_user_password)
            confirm_password_input.send_keys(EmployeeData().new_user_password)

            save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().save_button_locator)))

            save_button.click()

        except NoSuchElementException:
            print('Some of the elements are missing!')

    def edit_employee(self):
        try:
            pim_option = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().pim_locator)))
            pim_option.click()
            # employee_list_option = self.wait.until(
            #     EC.presence_of_element_located((By.XPATH, DashboardPageLocators().employee_list_locator)))
            # employee_list_option.click()
            time.sleep(3)
            employee_name_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().employee_name_locator)))
            employee_name_input.click()
            employee_name_input.send_keys(EmployeeData().new_user_firstname + ' ' + EmployeeData().new_user_lastname)
            time.sleep(3)
            search_button = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, DashboardPageLocators().search_locator)))
            search_button.click()
            time.sleep(3)
            edit_icon = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().edit_icon_locator)))
            edit_icon.click()
            time.sleep(5)
            nickname_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().nickname_locator)))
            nickname_input.clear()
            nickname_input.send_keys(EmployeeData().user_nickname)
            driver_license_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().driver_license_locator)))
            driver_license_input.clear()
            driver_license_input.send_keys(EmployeeData().user_driver_license)

            ssn_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().ssn_locator)))
            ssn_input.clear()

            ssn_input.send_keys(EmployeeData().user_ssn)

            nationality = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, DashboardPageLocators().nationality_dropdown_locator))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, DashboardPageLocators().nationality_to_select
                 ))).click()
            marital_status = self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, DashboardPageLocators().marital_status_dropdown_locator))).click()
            self.wait.until(EC.element_to_be_clickable(
                (By.XPATH, DashboardPageLocators().marital_status_to_select
                 ))).click()
            time.sleep(3)
            editpage_save_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().edit_save_button_locator)))

            editpage_save_button.click()

        except NoSuchElementException:
            print('Some of the elements are missing!')

    def delete_employee(self):
        try:
            pim_option = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().pim_locator)))
            pim_option.click()
            # employee_list_option = self.wait.until(
            #     EC.presence_of_element_located((By.XPATH, DashboardPageLocators().employee_list_locator)))
            # employee_list_option.click()
            time.sleep(3)
            employee_name_input = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().employee_name_locator)))
            employee_name_input.send_keys(EmployeeData().new_user_firstname + ' ' + EmployeeData().new_user_lastname)

            search_button = self.wait.until(
                EC.presence_of_element_located(
                    (By.XPATH, DashboardPageLocators().search_locator)))

            search_button.click()
            time.sleep(5)

            delete_icon = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().delete_icon_locator)))
            delete_icon.click()
            delete_button = self.wait.until(
                EC.presence_of_element_located((By.XPATH, DashboardPageLocators().delete_button_locator)))
            delete_button.click()

        except NoSuchElementException:
            print('Some of the elements are missing!')
