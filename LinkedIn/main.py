from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#----------------------- Logs in LinkedIn and searches jobs ----------------------------
options = Options()
options.add_experimental_option("detach", True)
options.add_argument('--incognito')
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get("https://www.linkedin.com/")
driver.find_element(By.LINK_TEXT, "Sign in").click()
driver.find_element(By.NAME, "session_key").send_keys("username@gmail.com", Keys.TAB, "password")
driver.find_element(By.XPATH, "//button[text()[contains(., 'Sign in')]]").click()
sleep(5)
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="global-nav"]/div/nav/ul/li[3]/a'))).click()
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.jobs-search-box__text-input"))).send_keys("marketing manager", Keys.ENTER)


#----------------------- Scrolls down the lazy loading job div by 25% of the pixels (height) at a time to scrape all the links inside ----------------------------
div = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="main"]/div/section[1]/div')))
sleep(1)
SCROLL_NUM = 4
while SCROLL_NUM > 0:
    driver.execute_script(f"arguments[0].scrollTop = arguments[0].scrollHeight / {SCROLL_NUM}", div)
    sleep(1)
    SCROLL_NUM -= 1

    
#----------------------- Saves jobs one by one and scrolls down by 25% of heigh pixels if the job link is not found ----------------------------
jobs = driver.find_elements(By.XPATH, '//ul[contains(@class, "scaffold-layout__list-container")]//a')
sleep(1)
SCROLL_NUM = 4
for job in jobs:
    try:
        job.click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.jobs-save-button"))).click()
    except:
        driver.execute_script(f"arguments[0].scrollTop = arguments[0].scrollHeight / {SCROLL_NUM}", div)
        SCROLL_NUM -= 1
        sleep(1)
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button.jobs-save-button"))).click()
