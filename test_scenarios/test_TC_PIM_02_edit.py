import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from data.orangehrm_page_data import LoginPageData, EmployeeData
from scenarios.orangehrm import OrangeHRM


class TestEditEmployee:

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    @pytest.fixture
    def web_page(self, driver):
        yield OrangeHRM(self.driver)

    @pytest.fixture
    def setup_web_page(self, web_page):
        web_page.browse()
        web_page.login(LoginPageData().login_username, LoginPageData().login_password)
        web_page.add_employee(EmployeeData.add_user_firstname, EmployeeData.add_user_middlename,
                              EmployeeData.add_user_lastname, EmployeeData.add_user_username)
        yield web_page
        web_page.delete_employee(EmployeeData.add_user_firstname, EmployeeData.add_user_lastname)

    # TC_PIM_02 - TestCase to edit an employee
    def test_edit_employee(self, setup_web_page):
        setup_web_page.edit_employee()
        assert self.driver.execute_script(
            "return document.getElementsByClassName('oxd-input')[4].value") == EmployeeData().user_nickname
        assert self.driver.execute_script(
            "return document.getElementsByClassName('oxd-input')[7].value") == EmployeeData().user_driver_license

        assert self.driver.execute_script(
            "return document.getElementsByClassName('oxd-input')[9].value") == EmployeeData().user_ssn
