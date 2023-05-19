from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Twitterbot():


    def __init__(self):
        
        self.message = ""

        options = Options()
        options.add_experimental_option("detach", True)
        options.add_argument('--incognito')
        driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
        driver.get("https://twitter.com/")
        driver.find_element(By.LINK_TEXT, "Log in").click()
        sleep(2)


        iframe = driver.find_element(By.XPATH, '//iframe[@title="Sign in with Google Button"]')
        driver.switch_to.frame(iframe)
        driver.find_element(By.XPATH, '//*[@id="container"]').click()


        sleep(2)
        try:
            window_before = driver.window_handles[0]
            window_after = driver.window_handles[1]
            driver.switch_to.window(window_after)
            driver.find_element(By.XPATH, '//input[@type="email"]').send_keys("username", Keys.ENTER)
            sleep(1)
            driver.find_element(By.XPATH, '//input[@type="password"]').send_keys("password", Keys.ENTER)
            
        except:
            print(0)

        def complain(self, message):
            pass
# NOT CONTINUING