import os
import time
import shutil
import pyautogui
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_chrome_driver import GetChromeDriver


get_driver = GetChromeDriver()
get_driver.install()

# Deleting a cache file will invalidate login sessions, etc...
try:
    shutil.rmtree(r"C:\chrometemp")  # Remove Cookie, Cache files
except FileNotFoundError:
    pass

# Open the debugger chrome
# remote-debugging-port : will be used to connect to the chrome debugger port
# user-data-dir : will be used to store the cookies, cache, etc...
try:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')   # Open the debugger chrome

except FileNotFoundError:
    subprocess.Popen(os.environ['LOCALAPPDATA'] + r'\Google\Chrome\Application\chrome.exe'
                     r'--remote-debugging-port=9222'
                     r'--user-data-dir="C:\chrometemp"')

options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=options)
driver.get("https://google.com")
driver.implicitly_wait(5)

driver.get("https://accounts.google.com/signin")
driver.implicitly_wait(5)

email = input("Enter your email: ")
password = input("Enter your password: ")

# selenium press key. now deprecated :(...
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='identifierId']"))
).send_keys(email)
driver.find_element_by_id("identifierNext").click()
WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.XPATH, "//input[@name='password']"))
).send_keys(password)
driver.find_element_by_id("passwordNext").click()


# pyautogui.write(email)  # your email
# pyautogui.press('tab', presses=3)  # Press the Tab key 3 times
# pyautogui.press('enter')
# time.sleep(3)  # wait a process

# pyautogui.write(password)   # your password
# pyautogui.hotkey('ctrl', 'c')
# pyautogui.press('enter')
# time.sleep(3)  # wait a process
# pyautogui.hotkey('ctrl', 'v')
# pyautogui.press('enter')

# input your code here...

input("Done! Press Enter to continue...")

driver.quit()
