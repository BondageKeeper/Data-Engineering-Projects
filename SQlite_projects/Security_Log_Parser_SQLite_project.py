import pandas as pd
import json , re , sqlite3 , io
json_uuid = """[
  {"meta": "node_id: 001 | uid: {a1b2-c3d4-e5f6} | status: active", "display": "USER_NAME: <<[Nikolay_Admin]>>"},
  {"meta": "node_id: 002 | uid: {f9e8-d7c6-b5a4} | status: active", "display": "USER_NAME: <<[Dmitry_Secure]>>"},
  {"meta": "node_id: 003 | uid: {1234-5678-90ab} | status: offline", "display": "USER_NAME: <<[Ivan_DevOps]>>"}
]"""
csv_file = """log_id;raw_payload
1001;sys_log_event:[auth_success] | source_uid:{a1b2-c3d4-e5f6} | addr:192.168.1.45:8080/TCP
1002;sys_log_event:[unknown_proc] | source_uid:{f9e8-d7c6-b5a4} | addr:10.0.0.12:443/HTTPS
1003;sys_log_event:[danger_zone] | source_uid:{a1b2-c3d4-e5f6} | addr:172.16.0.5:49152/UDP
1004;sys_log_event:[access_denied] | source_uid:{1234-5678-90ab} | addr:127.0.0.1:22/SSH"""

df_logs = pd.read_csv(io.StringIO(csv_file),sep=';')
user_uuid = json.loads(json_uuid)
uuid_list = []
name_list = []

for user_data in user_uuid:
    uuid_list.append(user_data['meta'])
    name_list.append(user_data['display'])

def convert_json_into_db(given_list1,given_list2):
    cleaned_uid = []
    cleaned_names = []
    for uid in given_list1:
        uid = re.findall(r'uid\s?:\s?(?=\{)(.*?)(?<=\})',uid,flags=re.I)[0].strip('{}')
        cleaned_uid.append(uid)
    for name in given_list2:
        name = re.findall(r'\[(.*?)\]',name,re.I)[0].lower().title().strip()
        cleaned_names.append(name)
    json_united_data = list(zip(cleaned_uid,cleaned_names))
    return json_united_data
logs_data = convert_json_into_db(uuid_list,name_list)

def convert_csv_into_db(df):
    csv_uid = df['raw_payload'].apply(lambda source_uuid: re.findall(r'uid\s?:\s?(?=\{)(.*?)(?<=\})',source_uuid)[0]).str.strip('{}').tolist()
    csv_ip_list = df['raw_payload'].apply(lambda ip: re.findall(r'addr:\s?(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})',ip,flags=re.I)[0]).tolist()
    csv_port = df['raw_payload'].apply(lambda port: re.findall(r'addr:\s?\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}:(\d+)\s?(?:/)',port,flags=re.I)[0]).tolist()
    protocol = df['raw_payload'].apply(lambda prt: re.findall(r'/\s?(\w+)$',prt,flags=re.I)[0]).str.upper().tolist()
    csv_united_data = list(zip(csv_uid,csv_ip_list,csv_port,protocol))
    return csv_united_data
ip_data = convert_csv_into_db(df_logs)

def work_with_databases(data1,data2):
    conn = sqlite3.connect('users_ip_and_uid.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users_logs')
    cursor.execute('DROP TABLE IF EXISTS users_ports')
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_logs(
    users_id INTEGER PRIMARY KEY AUTOINCREMENT ,
    uid TEXT , 
    user_name TEXT
    )""")
    cursor.executemany('INSERT INTO users_logs (uid,user_name) VALUES (?,?)',data1)
    cursor.execute("""CREATE TABLE IF NOT EXISTS users_ports(
    uid TEXT ,
    ip INTEGER ,
    port INTEGER ,
    protocol TEXT ,
    FOREIGN KEY (uid) REFERENCES users_logs (uid)
    )""")
    cursor.executemany('INSERT INTO users_ports (uid,ip,port,protocol) VALUES (?,?,?,?)',data2)
    cursor.execute('DROP VIEW IF EXISTS full_report')
    cursor.execute("""CREATE VIEW IF NOT EXISTS full_report AS
                   SELECT users_logs.uid , users_logs.user_name , users_ports.ip,
                   users_ports.port , users_ports.protocol FROM users_ports
                   JOIN users_logs ON users_ports.uid = users_logs.uid 
                   ORDER BY users_ports.port DESC""")
    cursor.execute('SELECT * FROM full_report')
    print(f'result: {cursor.fetchall()}')
    conn.commit()
    conn.close()
work_with_databases(logs_data,ip_data)
