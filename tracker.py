from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selectorlib import Extractor
import requests
import json
import time

driver = webdriver.Edge(r'C:\Users\ritik\Desktop\Project Material\Big Data Analytics\Amazon Web Tracker\msedgedriver.exe')

item = "Laptops With GTX1650"

driver.get('https://amazon.in')
search_box = driver.find_element_by_id('twotabsearchtextbox').send_keys(item)
driver.implicitly_wait(5)
search_button = driver.find_element_by_id("nav-search-submit-button").click()


