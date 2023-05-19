from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Netspeed():

    def __init__(self):

        self.down_speed = ""
        self.up_speed = ""

        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--incognito')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get("https://www.speedtest.net/")

        tries = 10
        while tries > 0:
            try:
                WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.LINK_TEXT, "GO"))).click()
                break
            except:
                try:
                    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="onetrust-close-btn-container"]/button'))).click()
                    tries -= 1
                except:
                    print("Unexpected error")
                    break

        def get_results(self):
            try:
                down_speed = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.download-speed"))).text
                up_speed = WebDriverWait(driver,60).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "span.upload-speed"))).text
                return (down_speed, up_speed)
            except:
                print("Results not found")

        while "--" in get_results(): 
            sleep(1)
        self.down_speed = get_results()[0] 
        self.up_speed = get_results()[1]
