import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

DRIVER_PATH = '/Users/andrewdoyle/Documents/selenium-example/chromedriver'
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(DRIVER_PATH, options=options)

driver.get('http://www.google.com/')
driver.save_screenshot('google-screenshot.png')

time.sleep(3) 
driver.quit()