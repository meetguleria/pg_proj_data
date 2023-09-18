import psycopg2


def test_posgresql_connection():
    connection = psycopg2.connect(
        dbname="postgres",
        user="meetg",
        host="localhost"
    )

    cursor = connection.cursor()
    cursor.execute("SELECT 1;")
    result = cursor.fetchone()
    assert result[0] == 1

def test_create_database():
    connection = psycopg2.connect(
        dbname = 'postgres',
        user='meetg',
        host='localhost'
    )
    connection.set_isolation_level(psycopg2.extensions.ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = connection.cursor()

    #Drop the database if it exists and then create
    cursor.execute('DROP DATABASE IF EXISTS test_db;')
    cursor.execute('CREATE DATABASE test_db;')

    cursor.close()
    connection.close()

    #check if we can connect to the new database
    new_conn = psycopg2.connect(
        dbname='test_db',
        user='meetg',
        host='localhost'
    )
    new_cursor = new_conn.cursor()
    new_cursor.execute('SELECT 1;')
    result = new_cursor.fetchone()

    assert result[0] == 1

    new_cursor.close()
    new_conn.close()

def test_crud_operations():
    connection = psycopg2.connect(
        dbname='test_db',
        user='meetg',
        host='localhost'
    )
    cursor = connection.cursor()

    #Create a table
    cursor.execute("DROP TABLE IF EXISTS test_table;")
    cursor.execute("CREATE TABLE test_table (id SERIAL PRIMARY KEY, name VARCHAR(100));")

    #Insert data
    cursor.execute("INSERT INTO test_table (name) VALUES ('TestName');")
    
    #Read Data
    cursor.execute("SELECT name FROM test_table WHERE id = 1;")
    result = cursor.fetchone()
    assert result[0] == 'TestName'

    #Update data
    cursor.execute("UPDATE test_table SET name = 'UpdatedName' WHERE id = 1;")
    cursor.execute("SELECT name FROM test_table WHERE id = 1;")
    result = cursor.fetchone()
    assert result[0] == 'UpdatedName'

    #Delete data
    cursor.execute("DELETE FROM test_table WHERE id = 1;")
    cursor.execute("SELECT name FROM test_table WHERE id = 1;")
    result = cursor.fetchone()
    assert result is None
    
    cursor.close()
    connection.close()