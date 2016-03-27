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

def getMenuImages(URL, browser):
    browser.get(URL)

    list_links = browser.find_elements_by_tag_name('img')

    for link in list_links:
        if "Menu" in link.get_attribute('alt'):
            image_src = link.get_attribute('src')
            if 'menu' in image_src:
                return image_src

if __name__ == "__main__":
    URL = "https://www.zomato.com/ncr/impromptu-golf-course-road-gurgaon/menu#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"

    # Get the menu image
    getMenuImage(URL)

    # Starting the browser
    browser = webdriver.Firefox()

    # Getting the menu image
    getMenuImages(URL. browser)

    # Close the browser
    browser.close()




