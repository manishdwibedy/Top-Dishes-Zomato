import connection

def get(connection, query):
    return connection.zomato.search({'q':query})

def getCount(connection, query):
    docs = connection.zomato.search({'q':query, 'rows': 0})
    return docs.result.response.numFound

if __name__ == '__main__':
    solr = connection.get_connection()
    print getCount(solr, '*:*')


