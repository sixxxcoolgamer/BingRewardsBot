# Handles microsoft edge logic for searches
# needs 20 searches daily for full 100 points

import time
from selenium import webdriver
from login import loginseq, sendkeys, click, SIGNIN
from config import directory, sleeptimer
from textgrab import text

# grabs list of words to search
edgetext = []
for i in range(51, 60):
#for i in range(15, 17):
    temp = text[i]
    edgetext.append(temp)

def edgedriver():
    print("\n>>> Starting Microsoft Edge Searches...")
    start_time = time.time()

    # msedge driver
    browser = webdriver.Edge(executable_path=directory+'msedgedriver.exe')

    for text in edgetext:
        browser = webdriver.Edge(executable_path=directory+'msedgedriver.exe')
        
        # go to bing
        browser.get("https://bing.com")
        time.sleep(sleeptimer)
        # search
        sendkeys(browser, text)
        time.sleep(sleeptimer)
        
        # sign in
        click(browser, SIGNIN)
        time.sleep(sleeptimer)
        loginseq(browser)
        time.sleep(sleeptimer)
        browser.refresh()
        time.sleep(sleeptimer)

        browser.quit()

    print(">>> Finished Microsoft Edge Searches in " + str(round((time.time() - start_time),3)) + "s")


 
