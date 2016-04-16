from solr import query, connection
from util import constant

def loadMenuData():
    pass

def readMenuFiles(filename):
    """
    Reading menu items from a file
    :param filename: filename of the file containing menu
    :return: a list of menu items
    """
    conn = connection.get_connection()
    response = query.get(conn, constant.RESTAURANTS_COLLECTION, 'id:*')

    res = response.result.dict['response']['docs']
    menuItems = []

    with open(filename) as menuFile:
        for menuItem in menuFile:
            menuItems.append(menuItem)
    return menuItems

if __name__ == '__main__':
    res_id = 1
    readMenuFiles('menu')