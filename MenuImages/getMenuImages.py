from bs4 import BeautifulSoup
import urllib2
from selenium import webdriver

def getMenuImage(URL):
    page = BeautifulSoup(urllib2.urlopen(URL), "html.parser")

    for img in page.findAll('img'):
        alt = img.attrs['alt']
        if "Menu" in alt:
            print img.attrs['src']
            break

def getMenuImages(URL):
    browser = webdriver.Firefox()
    browser.get(URL)

    list_links = browser.find_elements_by_tag_name('img')

    for link in list_links:
        print link.get_attribute('src')

    browser.close()


    # pass
if __name__ == "__main__":
    URL = "https://www.zomato.com/ncr/impromptu-golf-course-road-gurgaon/menu#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"

    # getMenuImage(URL)
    getMenuImages(URL)





