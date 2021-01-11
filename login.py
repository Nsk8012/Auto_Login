from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

usernameStr = 'putYourUsernameHere'
passwordStr = 'putYourPasswordHere'

PATH = "C:\webdriver\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get(('https://accounts.google.com/ServiceLogin?'
            'service=mail&continue=https://mail.google'
            '.com/mail/#identifier'))

# fill in username and hit the next button

username = driver.find_element_by_id('Email')
username.send_keys(usernameStr)

nextButton = driver.find_element_by_id('next')
nextButton.click()

# wait for transition then continue to fill items

password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, "Passwd")))

password.send_keys(passwordStr)

signInButton = driver.find_element_by_id('signIn')
signInButton.click()
