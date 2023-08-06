import mysql.connector

def connect_to_database(host, user, password, database):
    try:
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        if connection.is_connected():
            print(f"Successfully connected to the database {database}")
            return connection
    except mysql.connector.Error as e:
        print(f"Error: {e}")
        return None

# Example usage:
host = "localhost"           # e.g., "localhost"
user = "root"       # e.g., "root"
password = "12061990"
database = "customer_database"

connection = connect_to_database(host, user, password, database)

if connection:
    connection.close()

