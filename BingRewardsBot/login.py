# Handles sequences for logging in button preses and typing

import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from config import EMAIL, PASSWORD, sleeptimer

EMAILFIELD = (By.ID, "i0116")
PASSWORDFIELD = (By.ID, "i0118")
NEXTBUTTON = (By.ID, "idSIButton9")
SEARCHBOX = (By.ID, "sb_form_q")
SIGNIN = (By.ID, "id_a")
SIGNINM = (By.ID, "hb_s")
MENU = (By.ID, "mHamburger")
pause = sleeptimer

# Login Sequence
def loginseq(browser):
    # wait for email field and enter email
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(EMAILFIELD)).send_keys(EMAIL)
    time.sleep(pause)
    # Click Next
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    time.sleep(pause)
    # wait for password field and enter password
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(PASSWORDFIELD)).send_keys(PASSWORD)
    time.sleep(pause)
    # Click Login - same id?
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(NEXTBUTTON)).click()
    time.sleep(pause)

def getsite(browser):
    browser.get('https://login.live.com')
    time.sleep(sleeptimer)
    loginseq(browser)
    time.sleep(sleeptimer)
    browser.get("https://bing.com")
    time.sleep(sleeptimer)    

# searching
def sendkeys(browser, text):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(SEARCHBOX)).send_keys(text)
    time.sleep(pause)
    browser.find_element_by_name("q").send_keys(Keys.ENTER)
    time.sleep(pause)

def click(browser, html):
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable(html)).click()
