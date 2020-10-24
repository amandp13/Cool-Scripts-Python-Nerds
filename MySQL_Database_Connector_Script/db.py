from mysql.connector import MySQLConnection

def main():
    # Connect to server
    cnx = MySQLConnection(host='<DATABASE_SERVER>',
                          database='<DATABASE_NAME>',
                          port=3306,
                          user='<DATABASE_USER>',
                          password='<DATABASE_PASS>')
    # Get a cursor
    cur = cnx.cursor()

    # Execute a query
    cur.execute("SHOW GRANTS FOR rizwan;")

    # Fetch one result
    row = cur.fetchall()
    for i in row:
        print(i)

    # Close connection
    cnx.close()

if __name__ == '__main__':
    main()
