import sqlite3 , json , re
conn = sqlite3.connect('users_emails.db')
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS user_emails')
cursor.execute("""CREATE TABLE IF NOT EXISTS user_emails (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    user_name TEXT ,
    user_email TEXT ,
    access_number INTEGER
)""")
json_users = """[
  {
    "raw_info": "User: !!Admin_99!!",
    "contact": "Write to: admin@corp.secure (Official)",
    "security_token": "Level-10"
  },
  {
    "raw_info": "User: #Shadow_Hunter#",
    "contact": "Email is shadow_1337@gmail.com; don't share!",
    "security_token": "Level-5"
  },
  {
    "raw_info": "User: ?Agent_007?",
    "contact": "Contact at bond_james_bond@mi6.uk.gov",
    "security_token": "Level-1"
  },
  {
    "raw_info": "User: _Glitch_Master_",
    "contact": "Send logs to glitch.m@provider.net",
    "security_token": "Level-3"
  }
]"""
users = json.loads(json_users)
users_list = []
email_list = []
access_list = []
for user in users:
    users_list.append(user['raw_info'])
    email_list.append(user['contact'])
    access_list.append(user['security_token'])
def clean_users(given_list1,given_list2,given_list3):
    cleaned_names = []
    cleaned_emails = []
    cleaned_access = []
    for name in given_list1:
        name = re.findall(r'User:\s?[_?#! ]*([\w_]+)[_?#! ]*',name,re.I)[0].rstrip('_')
        cleaned_names.append(name)
    for email in given_list2:
        email = re.findall(r'\s?[\w_\.]+@\w+\.\w+',email,re.I)[0]
        cleaned_emails.append(email)
    for access in given_list3:
        access = int(re.findall(r'\d+',access)[0])
        cleaned_access.append(access)
    return cleaned_names , cleaned_emails , cleaned_access
names = clean_users(users_list,email_list,access_list)[0]
emails = clean_users(users_list,email_list,access_list)[1]
keys = clean_users(users_list,email_list,access_list)[2]
def insert_into_db(par1,par2,par3):
    united = list(zip(par1,par2,par3))
    cursor.executemany('INSERT INTO user_emails (user_name,user_email,access_number) VALUES (?,?,?)',united)
    cursor.execute('SELECT * FROM user_emails ORDER BY access_number DESC')
    rows = cursor.fetchall()
    for row in rows:
        print(row)
insert_into_db(names,emails,keys)
conn.commit()
conn.close()
