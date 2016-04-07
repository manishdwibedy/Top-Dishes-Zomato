
import connection

def queryAll(connection, query):
    return connection.zomato.search({'q':query})


if __name__ == '__main__':
    solr = connection.get_connection()
    print queryAll(solr, '')


