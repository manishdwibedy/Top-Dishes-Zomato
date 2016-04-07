from bs4 import BeautifulSoup
import urllib2
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import InvalidSelectorException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By


def getMenuImage(URL):
    page = BeautifulSoup(urllib2.urlopen(URL), "html.parser")

    for img in page.findAll('img'):
        alt = img.attrs['alt']
        if "Menu" in alt:
            print img.attrs['src']
            break

def getMenuImages(URL, browser):
    browser.get(URL)

    list_links = browser.find_elements_by_tag_name('img')

    for link in list_links:
        if "Menu" in link.get_attribute('alt'):
            image_src = link.get_attribute('src')
            if 'menu' in image_src:
                print image_src

    # tag = browser.find_element_by_id('menutop')



    box = browser.wait.until(expected_conditions.presence_of_element_located(
        (By.ID, "menutop")))
    box.click()

    print 'done'

    # try:
    #     print "about to look for element"
    #     def find(driver):
    #         e = driver.find_element_by_id("menutop")
    #         if (e.get_attribute("disabled")=='true'):
    #             return False
    #         return e
    #     element = WebDriverWait(browser, 10).until(find)
    #     list_links = browser.find_elements_by_tag_name('img')
    #
    #     for link in list_links:
    #         if "Menu" in link.get_attribute('alt'):
    #             image_src = link.get_attribute('src')
    #             if 'menu' in image_src:
    #                 print image_src
    #
    # finally: print 'yowp'
    # print "ok, left the loop"


    # try:
    #     tag.click()
    # except:
    #     print 'Error'

    # untested Python pseudo code, only provides the logic
    # try:
    #     tag.click()
    # except ElementNotVisibleException:
    #     print "ElementNotVisibleException"
    # except NoSuchElementException:
    #     print "NoSuchElementException"
    # except InvalidSelectorException:
    #     print "InvalidSelectorException"
    # except:
    #     print "Other exception types possible"
    #     raise
    #
    #
    # list_links = browser.find_elements_by_tag_name('img')
    #
    # for link in list_links:
    #     if "Menu" in link.get_attribute('alt'):
    #         image_src = link.get_attribute('src')
    #         if 'menu' in image_src:
    #             print image_src
    #
    # nextImage = browser.find_element_by_id('menutop').click()



if __name__ == "__main__":
    URL = "https://www.zomato.com/ncr/impromptu-golf-course-road-gurgaon/menu#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"

    # Get the menu image
    getMenuImage(URL)

    # Starting the browser
    browser = webdriver.Firefox()

    # Getting the menu image
    getMenuImages(URL, browser)

    # Close the browser
    browser.close()




