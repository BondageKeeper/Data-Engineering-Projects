import pandas as pd
import json , re , io
network_logs_csv = """log_id,raw_payload,threat_level
"id_990","[2024/01/15 | 10:20:01] SRC_IP: 192.168.1.50 | DST: 8.8.8.8:53 | BYTES: 1024 | DESC: DNS_QUERY","low"
"id_991","[15-01-2024 10:25:30] SRC_IP: 10.0.0.15 | DST: 172.217.16.14:443 | BYTES: 54200 | DESC: HTTPS_POST","MEDIUM"
"id_992"," SRC_IP: --- | DST: 1.1.1.1:80 | BYTES: 0 | DESC: PORT_SCAN","CRITICAL"
"id_990","[2024/01/15 | 10:20:01] SRC_IP: 192.168.1.50 | DST: 8.8.8.8:53 | BYTES: 1024 | DESC: DNS_QUERY","low"
"id_993","[2024-01-17 14:00] SRC_IP: 192.168.1.100 | DST: 192.168.1.1:22 | BYTES: 120 | DESC: SSH_BRUTEFORCE","high_risk"
"id_994","[18/01/2024 09:15] SRC_IP: 192.168.1.55 | DST: 10.10.10.10:8080 | BYTES: 2500 | DESC: HTTP_GET","LOW"
"id_995","[2024.01.19 23:59:59] SRC_IP: 127.0.0.1 | DST: 127.0.0.1:6379 | BYTES: 45 | DESC: REDIS_PING","low"
"id_991","[15-01-2024 10:25:30] SRC_IP: 10.0.0.15 | DST: 172.217.16.14:443 | BYTES: 54200 | DESC: HTTPS_POST","MEDIUM"
"id_996","[2024-01-20] SRC_IP: 192.168.5.5 | DST: --- | BYTES: 999999 | DESC: DATA_EXFILTRATION","critical_alert"
"""

employees_json = """{
  "infosec_dept": {
    "staff": [
      {"uid": "S-101", "name": "  ALEX_vostok  ", "contacts": {"mail": "alex@safe.corp", "ext": "404"}, "clearance": 3},
      {"uid": "S-102", "name": "mariya_data_sec", "contacts": {"mail": "MARIYA@SAFE.CORP", "ext": "101"}, "clearance": 5},
      {"uid": "S-103", "name": "John.Doe", "contacts": {"mail": "j.doe@GMAIL.com", "ext": null}, "clearance": 1},
      {"uid": "S-104", "name": "  karen_key  ", "contacts": {"mail": "k.key@safe.corp", "ext": "777"}, "clearance": 4},
      {"uid": "S-105", "name": "viktor_null", "contacts": {"mail": "v.null@safe.corp", "ext": "000"}, "clearance": 2}
    ]
  }
}"""

network_csv_data = pd.read_csv(io.StringIO(network_logs_csv),sep=',')
parsed_json = json.loads(employees_json)
csv_employees = pd.json_normalize(parsed_json['infosec_dept']['staff'])

def parsing_csv_network_data(given_csv):
    src_ip = given_csv['raw_payload'].apply(lambda ip:re.findall(r'SRC_IP\s?:\s?(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})',ip,flags=re.I)[0] if
                                               re.findall(r'SRC_IP\s?:\s?\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}',ip) else None)

    src_ip = src_ip.fillna('0.0.0.0')
    dst_ip = given_csv['raw_payload'].apply(lambda ip:re.findall(r'DST\s?:\s?(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})',ip,flags=re.I)[0] if
                                               re.findall(r'DST\s?:\s?\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4}',ip) else None)
    dst_ip = dst_ip.fillna('0.0.0.0')
    bytes_amount = given_csv['raw_payload'].apply(lambda byte: re.findall(r'BYTES\s?:\s?(\d+)',byte)[0]).astype(int)

    dates = given_csv['raw_payload'].apply(lambda date: re.sub(r'.*?\[(\d{4})[./-](\d{2})[./-](\d{2}).*?\].*',r'\1-\2-\3',date)
    if re.findall(r'.*?\[(\d{4})[./-](\d{2})[./-](\d{2}).*?\].*',date) else(re.sub(r'.*?\[(\d{2})[./-](\d{2})[./-](\d{4}).*?\].*'
    ,r'\3-\2-\1',date) if re.sub(r'.*?\[(\d{2})[./-](\d{2})[./-](\d{4}).*?\].*',r'\3-\2-\1',date) else 0))
    dates = dates.apply(lambda date: date if len(date) < 11 else None)
    dates = dates.fillna('0000-00-00')
    given_csv = given_csv.drop_duplicates(subset=['log_id'])
    given_csv = given_csv.reset_index()
    given_csv = given_csv.drop(columns='index')
    given_csv['threat_level'] = given_csv['threat_level'].str.lower().str.strip()
    given_csv = given_csv.drop(columns='raw_payload')
    given_csv = given_csv.assign(SRC_IP=src_ip,DST_IP=dst_ip,dates=dates,bytes=bytes_amount)
    given_csv = given_csv.loc[(given_csv['dates'] != '0000-00-00') & (given_csv['bytes'] != 0)]
    given_csv['log_id'] = given_csv['log_id'].apply(lambda number: re.findall(r'id_(\d+)',number)[0]).astype(int)
    start_id = 101
    given_csv['log_id'] = range(start_id,start_id + len(given_csv))
    return given_csv
csv1_security = parsing_csv_network_data(network_csv_data)

def parsing_json_staff(given_csv):
    given_csv['name'] = given_csv['name'].str.lower().str.title().str.replace('.','_')
    given_csv = given_csv.rename(columns={'contacts.mail':'contacts','contacts.ext':'ext'})
    given_csv['contacts'] = given_csv['contacts'].str.lower().str.strip()
    given_csv['ext'] = given_csv['ext'].fillna('000').str.zfill(5)
    given_csv = given_csv.drop(columns='clearance')
    given_csv = given_csv.rename(columns={'uid':'log_id'})
    given_csv['log_id'] = given_csv['log_id'].str.extract(r'S-(\d+)')[0].astype(int)
    return given_csv
csv2_employee = parsing_json_staff(csv_employees)

def merge_tables(csv1,csv2):
    final_csv = pd.merge(csv1,csv2,on='log_id',how='outer')
    final_csv['name'] = final_csv['name'].fillna('UNKNOWN')
    final_csv['contacts'] = final_csv['contacts'].fillna('UNKNOWN')
    final_csv['ext'] = final_csv['ext'].fillna('UNKNOWN')
    final_csv['importance'] = final_csv['threat_level'].apply(lambda threat: '*' if threat == 'low' else('*'*3 if threat == 'medium'
                                                                                                       else '*'*5))
    final_csv.to_csv('security_report',index=False,sep=',')
merge_tables(csv1_security,csv2_employee)

