import requests
import os
from util import constant

def getText(menuItems):

    headers = {'Accept': 'text/html'}

    menuText = {}
    for filename, menuImage in menuItems.iteritems():
        with open(menuImage) as fh:
            mydata = fh.read()
            response = requests.put(constant.TIKA_CONTENT_URL, headers=headers, data=mydata)
            menu_ocr_text = response.text

            menuText[filename] = menu_ocr_text

    return menuText

def getMenuImages():
    '''
    Getting all the menu images for all the restaurants
    :return: a list of menu files
    '''
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    menuDirectory = os.path.join(currentDirectory, 'images')

    menuItems = {}
    for root, dirs, files in os.walk(menuDirectory, topdown=False):
        for name in files:
            menuItems[name] = os.path.join(root, name)

    return menuItems

def writeMenuText(menuText):
    currentDirectory = os.path.dirname(os.path.realpath(__file__))
    textDirectory = os.path.join(currentDirectory, 'ocr_text')

    for filename, menu in menuText.iteritems():

        file_location = os.path.join(textDirectory, filename)
        target = open(file_location + '.txt', 'wb')
        target.write(menu.encode("UTF-8"))
        target.close()
    pass

if __name__ == '__main__':
    menuItems = getMenuImages()
    menuText = getText(menuItems)

    writeMenuText(menuText)

    print 'Text extraction done!'