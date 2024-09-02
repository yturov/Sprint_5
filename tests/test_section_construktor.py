from src.config import Config
from src.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestSectionConstruktor:

    def test_section_sous(self, driver):
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        sous_section = driver.find_element(*Locators.SOUS_SECTION)
        nachinki_section = driver.find_element(*Locators.NACHINKI_SECTION)
        bulki_section = driver.find_element(*Locators.BULKI_SECTION)
        sous_section.click()
        assert "current" in sous_section.get_attribute("Class")
        assert "current" not in nachinki_section.get_attribute("Class")
        assert "current" not in bulki_section.get_attribute("Class")

    def test_section_nachinki(self, driver):
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        sous_section = driver.find_element(*Locators.SOUS_SECTION)
        bulki_section = driver.find_element(*Locators.BULKI_SECTION)
        nachinki_section = driver.find_element(*Locators.NACHINKI_SECTION)
        nachinki_section.click()
        assert "current" in nachinki_section.get_attribute("Class")
        assert "current" not in sous_section.get_attribute("Class")
        assert "current" not in bulki_section.get_attribute("Class")

    def test_section_bulki(self, driver):
        WebDriverWait(driver, 2).until(EC.url_to_be(Config.URL))
        sous_section = driver.find_element(*Locators.SOUS_SECTION)
        sous_section.click()
        nachinki_section = driver.find_element(*Locators.NACHINKI_SECTION)
        nachinki_section.click()
        bulki_section = driver.find_element(*Locators.BULKI_SECTION)
        bulki_section.click()
        assert "current" in bulki_section.get_attribute("Class")
        assert "current" not in sous_section.get_attribute("Class")
        assert "current" not in nachinki_section.get_attribute("Class")
