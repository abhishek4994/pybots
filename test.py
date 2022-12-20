from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.common.exceptions import NoSuchElementException
import time

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = ChromeService("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=option)

driver.get("https://quillbot.com/")
time.sleep(10)
driver_input = driver.find_element(By.XPATH,'//*[@id="inputText"]')
driver_input.send_keys("hello there good day to you")
#driver_input.send_keys(f"On Reddit Today- {self.redditTrending}")
time.sleep(3)
paraphrase = driver.find_element(By.XPATH, '//*[@id="InputBottomQuillControl"]/div/div/div/div[2]/div/div/div/div/button')
paraphrase.click()
time.sleep(5)
paraphrasedTweet = driver.find_element(By.XPATH,'//*[@id="editable-content-within-article"]')
print(paraphrasedTweet.text)
time.sleep(2)
print("Quillbot Done")



# TWITTER_ID = "LeviLovesTech"
# TWITTER_PASSWORD = "Levi@4994"

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)
# twitter = webdriver.Chrome(options=chrome_options)

# twitter.get(url="https://twitter.com/?lang=en")

# time.sleep(10)

# sign=twitter.find_element_by_link_text("Sign in")
# sign.click()
# time.sleep(10)

# log=twitter.find_element_by_tag_name("input")
# log.send_keys("email")
# log.send_keys("\ue007")
# time.sleep(5)