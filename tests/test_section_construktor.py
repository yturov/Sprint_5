from selenium.webdriver.support.expected_conditions import element_to_be_clickable, visibility_of_element_located

from src.config import Config
from src.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.data import UserData
import time


class TestSectionConstruktor:

    def test_section_sous(self, driver):
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        sous_section = driver.find_element(*Locators.SOUS_SECTION)
        sous_section.click()
        assert sous_section.text == "Соусы"
        assert driver.current_url == Config.URL

    def test_section_nachinki(self, driver):
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        nachinki_section = driver.find_element(*Locators.NACHINKI_SECTION)
        nachinki_section.click()
        assert nachinki_section.text == "Начинки"
        assert driver.current_url == Config.URL

    def test_section_bulki(self, driver):
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL_INPUT))
        driver.find_element(*Locators.EMAIL_FIELD).send_keys(UserData.EMAIL)
        driver.find_element(*Locators.PASSWORD_FIELD).send_keys(UserData.PASSWORD)
        driver.find_element(*Locators.INPUT_MAIN_BUTTON).click()
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        driver.find_element(*Locators.NACHINKI_SECTION).click()
        driver.find_element(*Locators.SOUS_SECTION).click()
        bulki_section = driver.find_element(*Locators.BULKI_SECTION)
        bulki_section.click()
        assert bulki_section.text == "Булки"
        assert driver.current_url == Config.URL
