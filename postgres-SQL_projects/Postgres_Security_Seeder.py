import psycopg2 , re
import json , io
import pandas as pd

configurations = {
    'host': '127.0.0.1',
    'port': '5432',
    'database': 'sec_users',
    'user': 'postgres',
    'password': '!WRITE HERE YOUR PASSWORD!'
}
json_raw =  """
[
    {"uid": "a1b2-c3d4", "display": "<<Nikolay_Admin>>", "status": "active"},
    {"uid": "f9e8-d7c6", "display": "<<Dmitry_Secure>>", "status": "active"},
    {"uid": "1234-5678", "display": "<<Ivan_DevOps>>", "status": "offline"},
    {"uid": "9999-0000", "display": "<<Unknown_Hacker>>", "status": "banned"}
]
"""
csv_raw = """log_id;event;source_uid;raw_address
1001;auth_success;a1b2-c3d4;192.168.1.45:8080/TCP
1002;unknown_proc;f9e8-d7c6;10.0.0.12:443/HTTPS
1003;danger_zone;a1b2-c3d4;172.16.0.5:49152/UDP
1004;access_denied;1234-5678;127.0.0.1:22/SSH
1005;brute_force;9999-0000;95.161.22.14:80/HTTP
1006;auth_success;f9e8-d7c6;192.168.1.10:3306/MySQL
"""

pyjson_string = json.loads(json_raw)
uid_list = []
name_list = []
for user in pyjson_string:
    uid_list.append(user['uid'])
    name_list.append(user['display'])
pycsv = pd.read_csv(io.StringIO(csv_raw),sep=';')

def deal_with_json_format(list1,list2):
    cleaned_names = []
    cleaned_uid = []
    for name in list1:
        cl_name = re.findall(r'^<<(.*?)>>$',name,re.I)[0]
        cleaned_names.append(cl_name)
    for uid in list2:
        uid = re.findall(r'[\w-]+',uid,re.I)[0]
        cleaned_uid.append(uid)
    total_data1 = list(zip(cleaned_uid,cleaned_names))
    return total_data1
data1 = deal_with_json_format(name_list,uid_list)

def deal_with_csv_format(raw_table):
    ip = raw_table['raw_address'].apply(lambda item: re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}',item, flags = re.I)[0]).tolist()
    protocol = raw_table['raw_address'].apply(lambda item: re.findall(r'/\s?(\w+)',item , flags = re.I)[0]).tolist()
    port = raw_table['raw_address'].apply(lambda item: re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:(\d+)',item)[0]).tolist()
    uid = raw_table['source_uid'].apply(lambda item: re.findall(r'[\w-]+',item,flags=re.I)[0]).tolist()
    total_data2 = list(zip(uid,ip,port,protocol))
    return total_data2
data2 = deal_with_csv_format(pycsv)

def deal_with_sql_database(d1,d2):
    conn = psycopg2.connect(**configurations)
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users_names CASCADE')
    cursor.execute('DROP TABLE IF EXISTS users_security CASCADE')
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_names(
    id SERIAL PRIMARY KEY ,
    uid TEXT UNIQUE ,
    name TEXT 
    )""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_security(
    uid TEXT REFERENCES users_names(uid) ON DELETE CASCADE ,
    ip TEXT ,
    port INTEGER ,
    protocol TEXT   
    )""")
    cursor.executemany('INSERT INTO users_names (uid,name) VALUES (%s,%s)',d1)
    conn.commit()
    cursor.executemany('INSERT INTO users_security (uid,ip,port,protocol) VALUES (%s,%s,%s,%s)',d2)
    cursor.execute("""CREATE OR REPLACE VIEW summary AS 
                   SELECT 
                   users_names.name , users_security.ip , users_security.port , users_security.protocol ,
                   CASE 
                   WHEN users_security.ip LIKE '192.168.%' OR users_security.ip LIKE '127.0.%' THEN 'Internal_Safe'
                   ELSE '!External_Danger!'
                   END AS safety_check
                   FROM users_names
                   JOIN users_security ON users_names.uid = users_security.uid
                   
    """)
    conn.commit()
    cursor.close()
    conn.close()
deal_with_sql_database(data1,data2)
