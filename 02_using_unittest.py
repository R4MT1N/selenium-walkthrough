import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class WikipediaSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_wikipedia(self):
        driver = self.driver
        driver.get("https://wikipedia.org")
        self.assertIn("Wikipedia", driver.title)
        element = driver.find_element_by_id('searchInput')
        element.clear()
        element.send_keys('selenium')
        element.send_keys(Keys.RETURN)
        title = driver.find_element_by_id('firstHeading')
        self.assertTrue(title.is_displayed() and title.text == "Selenium")

    def tearDown(self):
        self.driver.close()
