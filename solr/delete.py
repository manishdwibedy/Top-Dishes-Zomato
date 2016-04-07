
import connection
import query

# http://localhost:8983/solr/zomato/update?stream.body=%3Cdelete%3E%3Cquery%3Eid:2%3C/query%3E%3C/delete%3E&commit=true

def delete(connection, query):
    connection["zomato"].delete({'q':query})
    connection["zomato"].commit()

if __name__ == '__main__':
    connection = connection.get_connection()
    queryString = 'id:*'
    delete(connection, queryString)

    output = query.get(connection, '*:*')
    print output

