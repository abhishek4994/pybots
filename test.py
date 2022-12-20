from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
import time

TWITTER_ID = "LeviLovesTech"
TWITTER_PASSWORD = "Levi@4994"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
twitter = webdriver.Chrome(options=chrome_options)

twitter.get(url="https://twitter.com/?lang=en")

time.sleep(10)

sign=twitter.find_element_by_link_text("Sign in")
sign.click()
time.sleep(10)

log=twitter.find_element_by_tag_name("input")
log.send_keys("email")
log.send_keys("\ue007")
time.sleep(5)