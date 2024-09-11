import os
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_argument("--start-maximized")  # Open browser in maximized mode
chrome_options.add_argument("--disable-extensions")  # Disable extensions for a clean test

if getattr(sys, 'frozen', False):  # If running as a PyInstaller bundle
    chrome_driver_path = os.path.join(sys._MEIPASS, 'chromedriver.exe')
else:
    chrome_driver_path = 'chromedriver-win64/chromedriver.exe'
    
service = Service(chrome_driver_path)

driver = webdriver.Chrome(service=service, options=chrome_options)
driver.get('https://www.maxi.ca/')

languageButton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'site-language-toggle__item')))
languageButton.click()
