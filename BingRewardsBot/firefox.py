# Handles firefox logic for searches
# needs 30 searches daily for full 150 points

import time
from selenium import webdriver
from login import loginseq, sendkeys, click, getsite, SIGNIN
from config import directory, sleeptimer
from textgrab import text

# grabs list of words to search
pctext = []
for i in range(0, 30):
#for i in range(0, 3):
    temp = text[i]
    pctext.append(temp)

def ffdriver():
    print("\n>>> Starting PC Searches...")
    start_time = time.time()
    
    # firefox - geckodriver for firefox 
    browser = webdriver.Firefox(executable_path=directory+'geckodriver.exe')
    # login to outlook and bing
    getsite(browser)
    browser.refresh()
    time.sleep(sleeptimer)
    
    for text in pctext:
        sendkeys(browser, text)
        time.sleep(sleeptimer)
        browser.get("https://bing.com")

    print(">>> Finished PC Searches in " + str(round((time.time() - start_time),3)) + "s")
    browser.quit()
        
              
       
