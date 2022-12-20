import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from time import sleep

option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = ChromeService("C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=service, options=option)

TWITTER_ID = "LeviLovesTech"
TWITTER_PASSWORD = "Levi@4994"


class RedditHeadlinesTwitterBot:
    def __init__(self):
        self.driver = driver
        self.redditTrending = 0

    def get_reddit_headline(self):
        self.driver.get("https://www.reddit.com/")
        sleep(10)
        self.redditTrending = self.driver.find_element(By.CLASS_NAME, value="_2Jjv0TAohMSydVpAgyhjhA").text
        print(self.redditTrending)

    def tweet(self):
        self.driver.get("https://twitter.com/home")
        sleep(10)
        email_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        email_input.send_keys(TWITTER_ID)
        sleep(1)
        email_input.send_keys(Keys.ENTER)
        sleep(5)
        try:
            pass_input = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)
        except NoSuchElementException:
            username = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            username.send_keys("example")  #Your Username here in case Twitter asks for username before asking password
            username.send_keys(Keys.ENTER)
            sleep(5)
            pass_input = driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
            pass_input.send_keys(TWITTER_PASSWORD)
            pass_input.send_keys(Keys.ENTER)

        sleep(5)

        input = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        input.send_keys(f"On Reddit Today- {self.redditTrending}")
        sleep(3)
        tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet.click()
        time.sleep(5)
        print("Tweet Done")
        self.driver.quit()


bot = RedditHeadlinesTwitterBot()
bot.get_reddit_headline()
bot.tweet()