import time
import unittest

from selenium import webdriver
from settings import TestSettings


class LostHatProductPageTests(unittest.TestCase):
    """Tests for web site https://autodemo.testoneo.com/en/ ."""

    @classmethod
    def setUp(self) -> None:
        """Method opens web browser before every single test in present class."""

        driver_settings = TestSettings()
        self.driver = webdriver.Chrome(driver_settings.executable_path)
        self.base_url = 'https://autodemo.testoneo.com/en'
        self.login_page_url = self.base_url + '/login?back=my-account'
        self.item_url = self.base_url + '/men/1-1-hummingbird-printed-t-shirt.html'

    @classmethod
    def tearDown(self) -> None:
        """Method closes web browser after every single test in present class."""
        self.driver.quit()

    def assert_element_text(self, driver, xpath, expected_text):
        """Checking assert based on outherText attribute value of given element.
        :param driver: webdriver instance
        :param xpath: xpath to element with text to be observed
        :param expected_text: text what we expecting to be found
        :return: None
        """
        element_text = driver.find_element_by_xpath(xpath).get_attribute('outerText')
        self.assertEqual(expected_text, element_text, f"Expected text differ from actual on page: {driver.current_url}")

    def test_item_name(self):
        """Testing correct name of t-shirt"""
        expected_text = "HUMMINGBIRD PRINTED T-SHIRT"
        driver = self.driver
        driver.get(self.item_url)
        item_name_xpath = '//h1[@itemprop="name"]'

        time.sleep(1)
        driver.save_screenshot('screens\smoke_test_open_login_page.png')
        self.assert_element_text(driver, item_name_xpath, expected_text)

    def test_item_price(self):
        """Testing correct price of t-shirt"""
        expected_price = "PLN23.52"
        driver = self.driver
        driver.get(self.item_url)
        item_price_xpath = '//*[@itemprop="price"]'

        self.assert_element_text(driver, item_price_xpath, expected_price)
