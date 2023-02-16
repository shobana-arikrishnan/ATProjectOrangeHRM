import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from data.orangehrm_page_data import LoginPageData
from scenarios.orangehrm import OrangeHRM


class TestValidLogin:

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    @pytest.fixture
    def web_page(self, driver):
        yield OrangeHRM(self.driver)

    # TC_Login_01
    def test_valid_login(self, web_page):
        web_page.browse()
        cookie_before = self.driver.get_cookies()[0]['value']
        web_page.login(LoginPageData().login_username, LoginPageData().login_password)
        cookie_after = self.driver.get_cookies()[0]['value']
        actual_url = self.driver.current_url
        assert actual_url == LoginPageData.dashboard_url
        assert cookie_before != cookie_after

