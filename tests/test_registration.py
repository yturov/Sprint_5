from src.config import Config
from src.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support import expected_conditions as EC
from src.data import UserData
from src.helpers import get_sign_up_data


class TestRegistration:

    def test_main_page(self, driver):
        assert driver.current_url == Config.URL

    def test_signup(self, driver):
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(Locators.REGISTER_BUTTON))
        driver.find_element(*Locators.REGISTER_BUTTON).click()
        email, password = get_sign_up_data()

        driver.find_element(*Locators.NAME_FIELD).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTER_FINAL_BUTTON).click()
        WebDriverWait(driver, 4).until(EC.url_to_be(Config.URL_INPUT))

        assert driver.current_url == Config.URL_INPUT

    def test_empty_name(self, driver):
        driver.get(Config.URL_REG)
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_REG))
        email, password = get_sign_up_data()

        name_field = driver.find_element(*Locators.NAME_FIELD)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Locators.REGISTER_FINAL_BUTTON).click()
        driver.find_element(*Locators.REGISTER_FINAL_BUTTON).click()
        driver.find_element(*Locators.REGISTER_FINAL_BUTTON).click()

        assert name_field.get_attribute("value") == ""
        assert driver.current_url != Config.URL_INPUT

    def test_incorrect_password(self, driver):
        driver.get(Config.URL_REG)
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_REG))
        email = get_sign_up_data()

        driver.find_element(*Locators.NAME_FIELD).send_keys(UserData.LOGIN)
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys("asdfg")
        driver.find_element(*Locators.REGISTER_FINAL_BUTTON).click()

        message_incorrect_password = (WebDriverWait(driver, 2).
        until(
            expected_conditions.visibility_of_element_located(Locators.MESSAGE_INCORRECT_PASSWORD)))

        assert driver.current_url != Config.URL_INPUT
        assert message_incorrect_password.is_enabled()
        assert message_incorrect_password.is_displayed()

