import psycopg2
from faker import Faker

fake = Faker('en_US')
configurations = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'fake_user_database',
    'user': 'postgres',
    'password': '!WRITE HERE YOUR PASSWORD!'
}
conn = psycopg2.connect(**configurations)
cursor = conn.cursor()
try:
    cursor.execute("""CREATE TABLE IF NOT EXISTS artificial_users(
        id SERIAL PRIMARY KEY ,
        username TEXT , 
        bio TEXT ,
        credit_card TEXT ,
        registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )""")
    for _ in range(100):
        user_data = (fake.name(),fake.sentence(),fake.credit_card_number(card_type='mastercard'))
        cursor.execute('INSERT INTO artificial_users (username,bio,credit_card) VALUES(%s,%s,%s)',user_data)
    conn.commit()
    cursor.close()
    conn.commit()

except Exception as error:
    print(f'Error connection: {error}')

