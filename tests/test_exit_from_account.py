from src.config import Config
from src.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import UserData


class TestExitFromAccount:

    def test_exit_from_account(self, driver):
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_ACCOUNT_PROFILE))
        driver.find_element(*Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        assert driver.current_url == Config.URL_INPUT
