from selenium import webdriver
from selenium.webdriver.common.by import By
import logging


options = webdriver.ChromeOptions()
options.add_argument("--disable-blink-features=AutomationControlled")
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options)
driver.implicitly_wait(10)
logging.basicConfig(format='%(asctime)s %(message)s')


def login_twitter(id,passwd,name):
    driver.get("https://twitter.com/login")
    try:
        driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input").send_keys(id)
        driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]").click()

        driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(passwd)
        driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div").click()

        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[10]/div/div[1]/svg")
    except:
        try:
            driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input").send_keys(name)
            driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/header/div/div/div/div[1]/div[2]/nav/a[10]/div/div[1]/svg")
        except:
            try:
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input").send_keys(passwd)
                driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div").click()
            except:
                logging.error("X Login Error")

def get_tweet_selenium(id):
    driver.get("https://twitter.com/" + id)
    try:
        driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/section/div/div/div[1]/div/div/article/div/div/div[2]/div[2]/div[2]/div").click
    except:
        logging.warning('Failed to access twitter')

tweet_Time = str

def get_tweet(id):
    global tweet_Time 
    
    driver.get("https://twitter.com/" + id)
    try:
        get_Tweet = driver.find_element(By.TAG_NAME,"time")
        new_Tweet_Time = re.match(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}\.\d{3}Z',get_Tweet.get_attribute('outerHTML'))
        if new_Tweet_Time != tweet_Time:
            return get_Tweet.find_element(By.XPATH, "./..").get_attribute("href")
    except:
        logging.warning('Failed to access twitter')


