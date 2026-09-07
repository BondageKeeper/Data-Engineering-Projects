#so , in this version 2 of my code I am going to repeat all essential thinks and find out more useful things
#reffering to databases
#here is a real explanation why we need placeholders:
#without placeholders(%s) we would simply insert data using f-string:
#                   username = 'Alex'
#                   query = f"INSERT INTO users_data (username) VALUES ('{username}')"
#                   cursor.execute(query)
#But what if hacker writes such a thing in the field:   haver', 20); DROP TABLE some_data; --
#Then our SQL will look something like that:(I mean SQL of this so-called hacker)
#
#                   'INSERT INTO users_data (username) VALUES ('haver', 20); DROP TABLE users_data; --'
#our database sees ; - which means that there is next string after VALUES string , and it carries on it deleting itself -- will turn a rest of request into a comment





import psycopg2
from faker import Faker
fake = Faker('en_US')
CONFIGURATIONS = {
    'host' : '127.0.0.1',
    'port' : '5432',
    'database' : 'repeating',
    'user' : 'postgres',
    'password' : '0631'
}

conn = psycopg2.connect(**CONFIGURATIONS)
cursor = conn.cursor()
try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_data(
    id SERIAL PRIMARY KEY ,
    username TEXT , 
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP   
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS products_data(
    product TEXT ,
    price INTEGER ,
    user_id INTEGER REFERENCES users_data(id) ON DELETE CASCADE
    )""")

    many_ids = []
    for _ in range(10):
        cursor.execute('INSERT INTO users_data (username) VALUES (%s) RETURNING id',(fake.name(),))
        #Reminder: We have to write ,(dot) after one element(if there is only one element , because method cursor.execute() needs either TUPLE or LIST. IF DELETE THIS DOT
        #we will give a string to our database and psycopg2 because of that will raise an error
        many_ids.append(cursor.fetchone()[0])
    for unique_id in many_ids:
        for _ in range(3):
            cursor.execute("INSERT INTO products_data (product,price,user_id) VALUES (%s,%s,%s)",(fake.word(),fake.random_int(100,1000),unique_id))

    cursor.execute("""SELECT users_data.username , products_data.product , products_data.price 
                      FROM users_data
                      INNER JOIN products_data ON users_data.id = products_data.user_id;
    """)
    print(cursor.fetchall())

except Exception as error:
    print(f'Something went wrong , more detail: {error}')

