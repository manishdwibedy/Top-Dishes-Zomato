from solr import query, connection, index
from util import constant

def loadMenuData(conn, resList):
    """
    Loading the restaurant info with the menu
    :param conn: Solr connection
    :param resList: the list of restaurant with menu list added
    :return: Nothing
    """
    index.index(conn, constant.RESTAURANTS_COLLECTION, resList)

def readMenuFiles(filename):
    """
    Reading menu items from a file
    :param filename: filename of the file containing menu
    :return: a list of menu items
    """
    conn = connection.get_connection()
    response = query.get(conn, constant.RESTAURANTS_COLLECTION, 'id:*')

    resList = response.result.dict['response']['docs']

    for res in resList:
        menuItems = []
        with open('menuData/menu_' + res['id'] + '.txt') as menuFile:
            for menuItem in menuFile:
                menuItems.append(menuItem.strip())
        res['menu'] = menuItems
    return resList

if __name__ == '__main__':
    res_id = 1
    readMenuFiles('menu')