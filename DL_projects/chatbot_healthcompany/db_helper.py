import mysql.connector

global cnx

cnx = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Baraille11',
    database='chatbot_health'
)

def get_next_customer_id():
    cursor = cnx.cursor()
    query = 'SELECT MAX(customer_id) FROM customers'
    cursor.execute(query)
    max_id = cursor.fetchone()[0]
    cursor.close()

    if max_id is None:
        return 1
    else:
        return max_id + 1

def save_to_db():
    pass