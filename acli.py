from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def myFaculty(browser):
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]/table/tbody/tr[7]/td[2]/a').send_keys(Keys.RETURN)
    time.sleep(5)
    print('\nMy Faculty')
    subs = browser.find_elements_by_xpath("//table[@id='tbl2']/tbody/tr")
    #if i == 4 or i == 9:
    #    continue
    for i in range(1, len(subs)):
        try:
            print(browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div/table[1]/tbody/tr[4]/td/div/table/tbody/tr["+str(i)+"]/td/table/tbody/tr/td/table/tbody/tr/td[2]/span[2]").text)
        except:
            pass
    print(len(subs))

def myCourses(browser):
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]/table/tbody/tr[6]/td[2]/a').send_keys(Keys.RETURN)
    core = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridCourses']/tbody/tr")
    open_electives = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridOpenCourses']/tbody/tr")

    #print(len(core), len(open_electives)
    print("\nMy Courses")
    for i in range(2, len(core)+1):
        print(str(i-1)+". " + browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div/table/tbody/tr[3]/td/table/tbody/tr["+str(i) + "]/td[3]").text)

    for i in range(2, len(open_electives)+1):
            print(str(i+len(core)-2)+". " +
                    browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div/table/tbody/tr[4]/td/table/tbody/tr["+str(i)+ "]/td[3]").text)

def attendace(browser):
    print("\n Attendance:")
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]/table/tbody/tr[6]/td[2]/a').send_keys(Keys.RETURN)
    core = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridCourses']/tbody/tr")
    open_electives = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridOpenCourses']/tbody/tr")
    
    for i in range(2, len(core)+1):
        print(str(i-1)+ ". " +
                browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div/table/tbody/tr[3]/td/table/tbody/tr["+str(i)+"]/td[3]").text,
                end='')

        print("{0:>40s}".format(browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div/table/tbody/tr[3]/td/table/tbody/tr["+str(i)+"]/td[8]/a").text))

    for i in range(2, len(open_electives)+1):
        print(str(i+len(core)-2)+". " +
                browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div/table/tbody/tr[4]/td/table/tbody/tr["+str(i)+ "]/td[3]").text)




def init():
    browser = webdriver.Chrome()
    browser.get("https://amizone.net/amizone/")
    browser.set_window_size(1124, 850)

    username = browser.find_element_by_xpath('//div[text()="User Name"]/following-sibling::input[not(@style="display:none;")]')
    password = browser.find_element_by_xpath('//div[text()="Password"]/following-sibling::input[not(@style="display:none;")]')

    username.send_keys("uid")
    password.send_keys("pwd")
    time.sleep(5)

    browser.find_element_by_id('ImgBttn_Login').click()
    time.sleep(5)
    browser.find_element_by_class_name('close').click()
    time.sleep(5)
    print("Welcome, " + browser.find_element_by_id('ctl00_lblUser').text)
    
    time.sleep(5)
    #myCourses(browser)
    myFaculty(browser)
    #browser.close()

init()
