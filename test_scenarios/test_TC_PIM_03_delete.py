import time

import pytest as pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from data.orangehrm_page_data import LoginPageData, EmployeeData
from locators.orangehrm_page_locators import DashboardPageLocators
from scenarios.orangehrm import OrangeHRM


class TestDeleteEmployee:

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

    # TC_PIM_03 - TestCase to delete an employee
    def test_delete_employee(self, setup_web_page):
        setup_web_page.delete_employee(EmployeeData.add_user_firstname, EmployeeData.add_user_lastname)
        time.sleep(5)
        assert self.driver.find_element(by=By.XPATH,
                                        value=DashboardPageLocators().record_not_found_locator).text == 'No Records Found'
