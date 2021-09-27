# pylint: disable-all
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


DRIVER_PATH = '/Users/andrewdoyle/Documents/selenium-example/chromedriver'

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(DRIVER_PATH)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in driver.page_source


    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()