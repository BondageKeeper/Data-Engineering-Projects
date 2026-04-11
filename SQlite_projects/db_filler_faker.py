import sqlite3
from faker import Faker
fake = Faker('en_US')
conn = sqlite3.connect('random_personal_staff.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS staff_list')
cursor.execute("""CREATE TABLE IF NOT EXISTS staff_list(
               user_id INTEGER PRIMARY KEY AUTOINCREMENT , 
               full_name TEXT ,
               job TEXT ,
               email TEXT ,
               personal_id TEXT ,
               salary INTEGER ,
               status TEXT ,
               address TEXT ,
               bank_card TEXT , 
               card_code INT ,
               ip_address TEXT
)""")
for _ in range(101):
    user_data = (fake.name(),fake.job(),fake.email(),fake.bothify(text='ID-####'),fake.random_int(min=2500,max=5000),
                 fake.random_element(elements=('Working','On Vacation','Fired')),fake.address(),
                 fake.credit_card_number(card_type='mastercard'),fake.credit_card_expire(),fake.ipv4())
    cursor.execute("""INSERT INTO staff_list (full_name,job,email,personal_id,salary,status,address,bank_card,card_code,ip_address
                   ) VALUES (?,?,?,?,?,?,?,?,?,?)""",user_data)
    cursor.execute('SELECT * FROM staff_list ORDER BY salary ASC')
    try:
        cursor.execute('ALTER TABLE staff_list ADD COLUMN estimation TEXT')
    except:
        pass
    cursor.execute("""UPDATE staff_list 
                   SET estimation = CASE 
                        WHEN salary < 3000 THEN 'low_reputation' 
                        WHEN salary BETWEEN 3000 and 4000 THEN 'middle_reputation'
                        ELSE 'good_reputation'
                   END
                   """)
conn.commit()
conn.close()
