import pytest as pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

from data.orangehrm_page_data import LoginPageData
from scenarios.orangehrm import OrangeHRM


class TestInvalidLogin:

    @pytest.fixture
    def driver(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close()

    @pytest.fixture
    def web_page(self, driver):
        yield OrangeHRM(self.driver)

    # TC_Login_02
    def test_invalid_login(self, web_page):
        web_page.browse().login(LoginPageData().login_username, LoginPageData().invalid_password)
        actual_url = self.driver.current_url
        assert actual_url != LoginPageData.dashboard_url
        error_text = web_page.get_error_text()
        assert error_text.text == 'Invalid credentials'

