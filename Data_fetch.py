from collections import OrderedDict
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import re
import openpyxl
from openpyxl import workbook
import getpass
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
import time
from datetime import date, datetime, timedelta
from selenium.webdriver.chrome.service import Service
import traceback
import datetime
import os

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
# driver = webdriver.Chrome(r"D:\\Westiminster\\Final project\\FB_SCAM\\chromedriver.exe")
driver.get('https://www.facebook.com/marketplace/london/search/?query=london%20rental%20property')
time.sleep(30)
# span_element = driver.find_element(By.XPATH,'//span[@class="x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u"]')

# # Extract the text content of the <span> element
# text_content = span_element.text

span_classes_to_match = "x193iq5w xeuugli x13faqbe x1vvkbs x1xmvt09 x1lliihq x1s928wv xhkezso x1gmr53x x1cpjm7i x1fgarty x1943h6x xudqn12 x676frb x1lkfr7t x1lbecb7 x1s688f xzsf02u"
span_elements = driver.find_elements(By.XPATH, f'//span[contains(@class, "{span_classes_to_match}")]')
text_contents = []

# Loop through each element and extract the text content
for span_element in span_elements:
    span_text_content = span_element.text
    text_contents.append(span_text_content)
# Print the extracted value
print(text_contents)