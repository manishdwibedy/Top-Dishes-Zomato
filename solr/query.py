import connection

def get(connection, collection, query):
    """
    Getting the data from collection matching the query
    :param connection: the Solr Connection
    :param collection: the Solr Collection
    :param query: Solr Query
    :return: the list of documents returned by Solr
    """

    return connection[collection].search({'q':query})

def getCount(connection, collection, query):
    """
    Get only the number of documents from the collection matching the query
    :param connection: the Solr Connection
    :param collection: the Solr Collection
    :param query: Solr Query
    :return: the number of documents matched
    """
    docs = connection[collection].search({'q':query, 'rows': 0})
    return docs.result.response.numFound

if __name__ == '__main__':
    solr = connection.get_connection()
    print getCount(solr, 'zomato_reviews','*:*')


