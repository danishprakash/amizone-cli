#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import getpass


def timetable(browser):
    print("\nTimetable\n")
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]/'
                                  'table/tbody/tr[5]/td[2]/a').send_keys(Keys.RETURN)
    for i in range(1, 8):
        print(browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[3]/'
                                            'div/table/tbody/tr[2]/td/table/tbody/tr['
                                            + str(i) + ']/td[1]').text)
        for j in range(1, 12):
            try:
                if browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[3]/'
                                                 'div/table/tbody/tr[2]/td/table/tbody/tr['
                                                         + str(i) + ']/td[' + str(j) + ']/div').text != '':
                    print(browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]'
                                                        '/td[3]/div/table/tbody/tr[2]/td/'
                                                        'table/tbody/tr[1]/td['
                                                        + str(j) + ']').text[11:] + ' - ', end='')
                    print(browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/'
                                                        'td[3]/div/table/tbody/tr[2]/td/table/tbody/tr['
                                                        + str(i) + ']/td[' + str(j) + ']/div').text)
            except:
                pass
        print('\n')


def myMentor(browser):
    print("\nMy Mentor\n")
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]/'
                                  'table/tbody/tr[8]/td[2]/a').send_keys(Keys.RETURN)
    print("Name: " + browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]"
                                                   "/td[3]/div/table/tbody/tr[2]/td/div[1]"
                                                   "/table/tbody/tr[2]/td[2]/div/span").text)
    print("Email: " + browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]"
                                                    "/div/table/tbody/tr[2]/td/div[1]/table"
                                                    "/tbody/tr[3]/td[2]/div/span").text)
    print("Phone: " + browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]"
                                                    "/td[3]/div/table/tbody/tr[2]/td/"
                                                    "div[1]/table/tbody/tr[4]/td[2]/div/span").text)


def myFaculty(browser):
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]'
                                  '/table/tbody/tr[7]/td[2]/a').send_keys(Keys.RETURN)
    time.sleep(1)
    print('\nMy Faculty\n')
    subs = browser.find_elements_by_xpath("//table[@id='tbl2']/tbody/tr")
    for i in range(1, len(subs) + 1):
        try:
            print(str(i) + ". ", end="")
            print(browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]"
                                                "/td[3]/div/table[1]/tbody/tr[4]/td/div"
                                                "/table/tbody/tr[" + str(i)
                                                + "]/td/div/table/tbody/tr/td/b/span[2]").text)
            print("   " + browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]"
                                                        "/td[3]/div/table[1]/tbody/tr[4]/td/div"
                                                        "/table/tbody/tr[" + str(i)
                                                        + "]/td/table/tbody/tr/td/table/tbody/tr/td[2]/span[2]").text)
            print("\n")
        except:
            print("   <no-faculty-data-available>\n")
            pass


def myCourses(browser):
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]/table'
                                  '/tbody/tr[6]/td[2]/a').send_keys(Keys.RETURN)
    core = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridCourses']"
                                          "/tbody/tr")
    open_electives = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridOpenCourses']"
                                                    "/tbody/tr")

    print("\nMy Courses")
    for i in range(2, len(core) + 1):
        print(str(i - 1) + ". " + browser.find_element_by_xpath("/html/body/form/table/tbody/"
                                                                "tr[2]/td[3]/div/table/tbody/tr[3]/td"
                                                                "/table/tbody/tr[" + str(i) + "]/td[3]").text)

    for i in range(2, len(open_electives) + 1):
        print(str(i + len(core) - 2) + ". " +
              browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div"
                                            "/table/tbody/tr[4]/td/table/tbody/tr[" + str(i) + "]/td[3]").text)


def attendace(browser):
    print("\n Attendance:")
    browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]/td[1]/table/tbody'
                                  '/tr[6]/td[2]/a').send_keys(Keys.RETURN)
    core = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridCourses']"
                                          "/tbody/tr")
    open_electives = browser.find_elements_by_xpath("//table[@id='ctl00_ContentPlaceHolder1_GridOpenCourses']"
                                                    "/tbody/tr")

    for i in range(2, len(core) + 1):
        print(str(i - 1) + ". " +
              browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]"
                                            "/div/table/tbody/tr[3]/td/table/tbody/tr["
                                            + str(i) + "]/td[3]").text, end='')

        print(" - " + browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]"
                                                    "/td[3]/div/table/tbody/tr[3]/td"
                                                    "/table/tbody/tr[" + str(i) + "]/td[8]/a").text)

    for i in range(2, len(open_electives) + 1):
        print(str(i + len(core) - 2) + ". " +
              browser.find_element_by_xpath("/html/body/form/table/tbody/tr[2]/td[3]/div/table"
                                            "/tbody/tr[4]/td/table/tbody/tr[" + str(i)
                                            + "]/td[3]").text, end='')
        print(" - " + browser.find_element_by_xpath('/html/body/form/table/tbody/tr[2]'
                                                    '/td[3]/div/table/tbody/tr[4]/td/table/tbody/tr['
                                                    + str(i) + ']/td[7]/a').text)


'''
    Fires up the browser, Asks for uid and pwd and clicks login, logs in (unsuccessfull login not handled right now)
    Closes popup(s), and displays the menu -> calls required function and loops until user quits explicitly (Ctrl-D or 'q') in which case, it logs out
    and quits the browser.
'''


def init():
    choice = ''
    browser = webdriver.Chrome()
    browser.get("https://amizone.net/amizone/")
    browser.set_window_size(1124, 850)

    username = browser.find_element_by_xpath('//div[text()="User Name"]/following-sibling::input'
                                             '[not(@style="display:none;")]')
    password = browser.find_element_by_xpath('//div[text()="Password"]/following-sibling::input'
                                             '[not(@style="display:none;")]')

    username.send_keys(input('Username: '))
    password.send_keys(getpass.getpass('Password: '))

    browser.find_element_by_id('ImgBttn_Login').click()
    time.sleep(1)

    '''
        Exits popup(s) that are sometimes displayed immediately after logging in.
    '''
    print("\nWelcome, " + browser.find_element_by_id('ctl00_lblUser').text)

    time.sleep(1)
    while True:
        print("\n===== Menu =====\n\n1. My Courses\n2. Attendance\n3. My Faculty\n4. "
              "My Mentor\n5. Timetable\n\nq: Log out & exit\n")
        choice = input(': ')

        if choice == '1':
            myCourses(browser)
        elif choice == '2':
            attendace(browser)
        elif choice == '3':
            myFaculty(browser)
        elif choice == '4':
            myMentor(browser)
        elif choice == '5':
            timetable(browser)
        elif choice == 'q':
            print('Logging out..')
            browser.find_element_by_xpath("/html/body/form/table/tbody/tr[1]/td/table/tbody/tr"
                                          "/td[3]/table/tbody/tr[1]/td/table/tbody/tr/td[2]/a").send_keys(Keys.RETURN)
            break
        else:
            print('Please enter a valid choice\n')
    browser.close()


init()
