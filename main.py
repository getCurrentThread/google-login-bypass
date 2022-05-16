# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.utils import keys_to_typing

from get_chrome_driver import GetChromeDriver
import undetected_chromedriver as uc


class EnhancedActionChains(ActionChains):
    def send_keys_1by1(self, keys_to_send, time_s=0.2):
        typing = keys_to_typing(keys_to_send)

        for key in typing:
            self.key_down(key)
            self.key_up(key)
            self.w3c_actions.key_action.pause(time_s)

        return self


# install selenium chrome driver
get_driver = GetChromeDriver()
get_driver.install()

email = input("Enter your email: ")
password = input("Enter your password: ")

# if you want to use the login session on file, you use the user-data-dir.
# driver = uc.Chrome(use_subprocess=True, user_data_dir="C:\\chrometemp")
driver = uc.Chrome(use_subprocess=True)
action = EnhancedActionChains(driver)
url = 'https://accounts.google.com/ServiceLogin'
driver.get(url)


WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'identifier'))
).click()

action.send_keys_1by1(email).send_keys_1by1(Keys.ENTER).perform()

WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.NAME, 'password'))
).click()

action.send_keys_1by1(password).send_keys_1by1(Keys.ENTER).perform()

# input your code here...

input("Done! Press Enter to exit...")

# If a situation is predicted that the process will not be terminated normally (if it cannot be quit),
# You must add "use_subprocess=True" to the `uc.Chrome` class constructor.
driver.quit()
