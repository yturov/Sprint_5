from src.config import Config
from src.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import UserData


class TestTransitionFromPersonalAccount:

    def test_input_construktor(self, driver):
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_ACCOUNT_PROFILE))
        driver.find_element(*Locators.CONSRUKTOR_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        soberite_burger = driver.find_element(*Locators.SOBERITE_BURGER)
        assert driver.current_url == Config.URL
        assert soberite_burger.text == "Соберите бургер"

    def test_input_logotip(self, driver):
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        driver.find_element(*Locators.ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_ACCOUNT_PROFILE))
        driver.find_element(*Locators.LOGOTIP_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        soberite_burger = driver.find_element(*Locators.SOBERITE_BURGER)
        assert driver.current_url == Config.URL
        assert soberite_burger.text == "Соберите бургер"
