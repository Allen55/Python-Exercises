import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ['PATH'] = r"/Users/allenharper/Desktop"
driver = webdriver.Chrome()

driver.get("https://www.amazon.com/Amazon-Video/b/?ie=UTF8&node=2858778011&ref_=nav_cs_prime_video")

search = driver.find_element_by_id("twotabsearchtextbox")
search.send_keys("pulp fiction")
search.submit()