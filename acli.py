from selenium import webdriver
from selenium.webdriver.common.keys import Keys

browser = webdriver.PhantomJS()
browser.get("https://amizone.net/amizone/")

username = browser.find_element_by_xpath('//div[text()="User Name"]/following-sibling::input[not(@style="display:none;")]')
password = browser.find_element_by_xpath('//div[text()="Password"]/following-sibling::input[not(@style="display:none;")]')

username.send_keys("uid")
password.send_keys("pwd")

browser.find_element_by_id('ImgBttn_Login').click()
browser.find_element_by_class_name('close').click()

print("Welcome, " + browser.find_element_by_id('ctl00_lblUser').text)

browser.close()
