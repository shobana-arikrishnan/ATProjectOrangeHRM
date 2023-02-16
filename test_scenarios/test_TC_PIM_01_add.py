import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from data.orangehrm_page_data import LoginPageData
from scenarios.orangehrm import OrangeHRM


class TestAddEmployee:

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    @pytest.fixture
    def web_page(self, driver):
        yield OrangeHRM(self.driver)

    # TC_PIM_01 - TestCase to add new employee
    def test_add_employee(self, web_page):
        web_page.browse()
        web_page.login(LoginPageData().login_username, LoginPageData().login_password)
        web_page.add_employee()
        time.sleep(5)
        look_for = 'viewPersonalDetails/empNumber'
        actual_url = self.driver.current_url
        assert look_for in actual_url

    # Testcase trying to add existing employee
    # def test_add_employee_failure(self, web_page):
    #     web_page.browse()
    #     web_page.login(LoginPageData().login_username, LoginPageData().login_password)
    #     web_page.add_employee()
    #     look_for = 'viewPersonalDetails/empNumber'
    #     actual_url = self.driver.current_url
    #     assert look_for not in actual_url
