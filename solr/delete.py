import connection
import query

def delete(connection, collection, query):
    """
    Deleting the documents from the collection matching the query
    :param connection: the Solr Connection
    :param collection: the Solr Collection
    :param query: Query
    :return: Nothing
    """
    connection[collection].delete({'q':query})
    connection[collection].commit()

if __name__ == '__main__':
    connection = connection.get_connection()
    queryString = 'id:2'
    delete(connection, 'zomato_reviews',queryString)

    # output = query.get(connection, '*:*')
    # print output

