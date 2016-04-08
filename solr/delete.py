import connection
import query

def delete(connection, query):
    connection["zomato"].delete({'q':query})
    connection["zomato"].commit()

if __name__ == '__main__':
    connection = connection.get_connection()
    queryString = 'id:*'
    delete(connection, queryString)

    output = query.get(connection, '*:*')
    print output

