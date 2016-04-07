import connection
import query

def index(connection, document):
    connection["zomato"].add(document)
    connection["zomato"].commit()

if __name__ == '__main__':
    connection = connection.get_connection()
    docs = [{"id":"1", "name":"a"},{"id":"2","name":"b"}]

    index(connection, docs)
    op = query.queryAll(connection, '*:*')
    print op

