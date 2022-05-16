import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from get_chrome_driver import GetChromeDriver


get_driver = GetChromeDriver()
get_driver.install()

# Deleting a cache file will invalidate login sessions, etc...
# try:
#     shutil.rmtree(r"C:\chrometemp")  # Remove Cookie, Cache files
# except FileNotFoundError:
#     pass

# get video title and url.
# [...document.querySelectorAll("a#video-title")].map(x => x.innerText).join('\n')
# [...document.querySelectorAll("a#video-title")].map(x => x.href).join('\n')

try:
    subprocess.Popen(r'C:\Program Files\Google\Chrome\Application\chrome.exe --remote-debugging-port=9222 '
                     r'--user-data-dir="C:\chrometemp"')   # Open the debugger chrome
    
except FileNotFoundError:
    subprocess.Popen(os.environ['LOCALAPPDATA'] + r'\Google\Chrome\Application\chrome.exe'
                     r'--remote-debugging-port=9222'
                     r'--user-data-dir="C:\chrometemp"')

option = Options()

option.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

browser = webdriver.Chrome(options=option)

browser.get("https://youtube.com")
browser.implicitly_wait(5)
playlist = input("Enter the playlist name: ")


with open("urls.txt", "r") as f:
    for url in f:
        url = url.strip()
        browser.get(url)
        # wait for the road. if the road is not ready, refresh and wait for 5 seconds.
        try :
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, "#button.style-scope.yt-icon-button[aria-label='재생목록에 저장']"))
            )
        except:
            browser.refresh()
            browser.implicitly_wait(10)
        # click the save button
        browser.find_element_by_css_selector("#button.style-scope.yt-icon-button[aria-label='재생목록에 저장']").click()
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "yt-formatted-string#label.checkbox-height.style-scope.ytd-playlist-add-to-option-renderer[title='" + playlist + "']"))
        ).click()

        # wait for the success alert
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "tp-yt-paper-toast#toast.toast-button.style-scope.yt-notification-action-renderer.paper-toast-open"))
        )