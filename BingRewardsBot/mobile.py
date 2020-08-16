# Handles mobile emulation and logic for searches
# needs 4 searches daily for full 20 points

import time
from selenium import webdriver
from login import loginseq, sendkeys, click, getsite, SIGNINM, MENU
from config import directory, sleeptimer
from textgrab import text

# grabs list of words to search 
mobiletext = []
for i in range(30, 50):
#for i in range(4, 7):
    temp = text[i]
    mobiletext.append(temp)

def mobiledriver():
    print("\n>>> Starting Mobile Searches...")
    start_time = time.time()
    
    # mobile emulation intilization
    mobile_emulation = {
        "deviceMetrics": { "width": 360, "height": 640, "pixelRatio": 3.0 },
        "userAgent": "Mozilla/5.0 (Linux; U; Android 4.4.2; en-us; SCH-I535 Build/KOT49H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30"
        }
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    browser = webdriver.Chrome(executable_path=directory+'chromedriver.exe', options=chrome_options)
    # login to outlook and bing
    getsite(browser)
    click(browser, MENU)
    time.sleep(.65)
    click(browser, SIGNINM)
    time.sleep(sleeptimer)
    
    for text in mobiletext:
        #click text box and search
        sendkeys(browser, text)
        time.sleep(sleeptimer)
        browser.get("https://bing.com")
        time.sleep(sleeptimer)
        browser.refresh()
        time.sleep(sleeptimer)

    print(">>> Finished Mobile Searches in " + str(round((time.time() - start_time),3)) + "s")
    browser.quit()

