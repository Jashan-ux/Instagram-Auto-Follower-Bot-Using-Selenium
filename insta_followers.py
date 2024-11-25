from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)

        username_input = self.wait.until(EC.presence_of_element_located((By.NAME, "username")))
        password_input = self.driver.find_element(By.NAME, "password")
        

        username_input.send_keys(username)
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)

    def find_followers(self, account_to_search):
        self.driver.get(f"https://www.instagram.com/{account_to_search}/")
        time.sleep(5)

        followers_button = self.wait.until(
            EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "followers"))
        )
        followers_button.click()
        time.sleep(5)

    def follow(self):
       
        all_buttons = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        
        for button in all_buttons :
            try:
                
                
                
                button.click()
                time.sleep()  
            except Exception as e:
                print(f"Could not click follow button: {e}")

    def quit(self):
        self.driver.quit()


