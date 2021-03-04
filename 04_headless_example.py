import unittest
import configparser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestHeadless(unittest.TestCase):
    def setUp(self):
        self.config = configparser.ConfigParser().read('config.ini')
        chrome_options = Options()
        chrome_options.add_argument("window-size=300,300")
        chrome_options.headless = True
        # or chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=chrome_options)

    def test_software_testing_is_enrolled(self):
        driver = self.driver
        driver.get("https://cw.sharif.edu/login/index.php")
        driver.find_element_by_name("username").send_keys(std_id())
        driver.find_element_by_name("password").send_keys(secret())
        driver.find_element_by_id("login").submit()
        self.assertTrue("آزمون نرم‌افزار" in [c.text.split('|')[0].strip()
                                     for c in driver.find_elements_by_css_selector("#pc-for-in-progress .media-heading a")])
        driver.save_screenshot('cw.png')

    def tearDown(self):
        self.driver.quit()
