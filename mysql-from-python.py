import os
import pymysql

username = os.getenv('C9_USER')

# Connect to the database
connection = pymysql.connect(
                            host='localhost',
                            user=username,
                            password='',
                            db='Chinook'
                            )

try:
    # Run a query
    with connection.cursor() as cursor:
        list_of_names = ['fred', 'Fred']
        # Prepare the string with the same number of placeholders as in
        # list_of_names
        format_strings = ', '.join(['%s']*len(list_of_names))
        print(format_strings)
        cursor.execute("DELETE FROM Friends WHERE name IN ({})".format(
                        format_strings), list_of_names)
        connection.commit()
finally:
    # Close the connection
    connection.close()
