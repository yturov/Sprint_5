from src.config import Config
from src.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import UserData


class TestInput:

    def test_input_account_main(self, driver):
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        assert driver.current_url == Config.URL

    def test_input_personal_account(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        assert driver.current_url == Config.URL

    def test_input_registration_form(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_REG))
        driver.find_element(*Locators.INPUT_REGISTER_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        assert driver.current_url == Config.URL

    def test_input_password_recovery(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.PASSWORD_RECOVERY_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_PASS_RECOVERY))
        driver.find_element(*Locators.INPUT_REGISTER_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        assert driver.current_url == Config.URL
