from solr import connection, query
from util import constant

def getMenuItems(res_id):
    """
    Getting the menu items for the restaurant
    :param res_id: the ID for the restaurant
    :return: menu items as list
    """
    conn = connection.get_connection()
    response = query.get(conn, constant.RESTAURANTS_COLLECTION, 'id:'+res_id, 1)

    restaurant = response.result.response.docs

    menuList = restaurant[0]['menu']
    return menuList


if __name__ == '__main__':
    print getMenuItems('799')