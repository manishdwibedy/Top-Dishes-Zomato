from bs4 import BeautifulSoup
import urllib2


def getMenuImage(URL):
    page = BeautifulSoup(urllib2.urlopen(URL), "html.parser")

    for img in page.findAll('img'):
        print img.attrs

if __name__ == "__main__":
    URL = "https://www.zomato.com/ncr/impromptu-golf-course-road-gurgaon/menu#tabtop?utm_source=api_basic_user&utm_medium=api&utm_campaign=v2.1"

    getMenuImage(URL)


