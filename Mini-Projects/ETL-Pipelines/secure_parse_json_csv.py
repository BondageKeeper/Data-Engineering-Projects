import pandas as pd
import json , re ,io
csv_raw_data = """event_id,user_info,access_details,risk_score_raw
"log_101","  USER: ivan_ivanov | IP: 192.168.1.1:8080 | DEPT: IT ","2023-10-01 10:15:30; SUCCESS; auth:ldap","low_risk: 0.15"
"log_102","USER: ALICE.SMITH | IP: 10.0.0.5:443 | DEPT: SECURITY ","2023/10/02 11:00:00; FAIL; auth:otp","HIGH_RISK: 0.88"
"log_103"," USER: bob_johnson | IP: 172.16.254.1:22 | DEPT: dev ","03-10-2023 09:45; success; auth:ssh","medium: 0.45"
"log_101","  USER: ivan_ivanov | IP: 192.168.1.1:8080 | DEPT: IT ","2023-10-01 10:15:30; SUCCESS; auth:ldap","low_risk: 0.15"
"log_104","USER: Charlie_Brown | IP: --- | DEPT: HR ","2023-10-04; FAIL; auth:none","CRITICAL: 0.99"
"log_105"," USER: AnNa_kArEnInA | IP: 192.168.1.55:1194 | DEPT: LEGAL ","2023.10.05 14:20; SUCCESS; auth:vpn","low: 0.05"
"log_106","USER: ivan_ivanov | IP: 192.168.1.1:8080 | DEPT: IT ","2023-10-06 18:00:01; FAIL; auth:ldap","medium: 0.55"
"log_107","USER: ALICE.SMITH | IP: 10.0.0.5:443 | DEPT: SECURITY ","07-10-2023; SUCCESS; auth:otp","low: 0.12"
"log_108"," USER: dmitry_dev | IP: 10.10.10.10:5432 | DEPT: DATABASE ","2023/10/08 22:15; FAIL; auth:password","HIGH_RISK: 0.75"
"log_109","USER: Elena_HR | IP: 192.168.1.20:80 | DEPT: HR ","09.10.2023 09:00; success; auth:none","low_risk: 0.10"
"log_110"," USER: bob_johnson | IP: 172.16.254.1:22 | DEPT: dev ","10-10-2023 10:30; FAIL; auth:ssh","CRITICAL: 0.92"
"log_111","USER: guest_01 | IP: 8.8.8.8:443 | DEPT: EXTERNAL ","2023-10-11; FAIL; auth:unknown","high: 0.81"
"log_102","USER: ALICE.SMITH | IP: 10.0.0.5:443 | DEPT: SECURITY ","2023/10/02 11:00:00; FAIL; auth:otp","HIGH_RISK: 0.88"
"log_112"," USER: Victor_Ops | IP: 192.168.0.100:22 | DEPT: OPS ","12/10/2023 15:45; SUCCESS; auth:ssh","medium: 0.40"
"log_113","USER: Maria_Data | IP: 127.0.0.1:8888 | DEPT: DATA_ENG ","2023-10-13 11:11:11; SUCCESS; auth:token","low: 0.18" """

json_raw_data = """{
  "system_users": {
    "u_001": {
      "full_name": " Ivan Ivanov ",
      "email": "IVAN@CORP.COM",
      "skills": "python,sql,pandas,docker",
      "meta": {"emp_id": "1", "join_date": "2021-01-15"}
    },
    "u_002": {
      "full_name": "ALICE SMITH",
      "email": "alice_work@GMAIL.com",
      "skills": "java,kotlin,wireshark,nmap",
      "meta": {"emp_id": "2", "join_date": "2020-05-20"}
    },
    "u_003": {
      "full_name": "bob_johnson",
      "email": "BOB_private@YANDEX.ru",
      "skills": "go,rust,sql,bash",
      "meta": {"emp_id": "3", "join_date": "2022-11-03"}
    },
    "u_004": {
      "full_name": " Charlie Brown ",
      "email": "charlie@OUTLOOK.com",
      "skills": "python,excel",
      "meta": {"emp_id": "4", "join_date": "2019-08-12"}
    },
    "u_005": {
      "full_name": "AnNa_kArEnInA",
      "email": "anna_best@MAIL.ru",
      "skills": "sql,pandas,tableau,legal_tech",
      "meta": {"emp_id": "5", "join_date": "2023-02-28"}
    }
  }
}"""

parsed_csv_data = pd.read_csv(io.StringIO(csv_raw_data),sep=',')
parsed_json_data = json.loads(json_raw_data)
json_df = pd.DataFrame.from_dict(parsed_json_data['system_users'],orient='index')
meta_df = pd.json_normalize(json_df['meta'])
final_df = pd.concat([json_df.drop('meta',axis=1),meta_df],axis=1)
final_df = final_df.reset_index()

def parsing_csv_user_info(given_csv):
    part1 = (given_csv['user_info'].str.extract(r'\s*USER:\s*([\w.]+)\s*')[0].
                  apply(lambda name: name.replace('_',' ').lower().title() if re.findall(r'\w+_\w+',name)
                  else name.replace('.',' ').lower().title()))
    part2 = (given_csv['user_info'].apply(lambda ip: re.findall(r'IP:\s*(\d+\.\d+\.\d+\.\d+)',ip)[0]
                  if re.findall(r'IP:\s*(\d+\.\d+\.\d+\.\d+)',ip,flags=re.IGNORECASE) else None)).fillna('0.0.0.0')
    part3 = (given_csv['user_info'].apply(lambda port: re.findall(r'IP:\s*\d+\.\d+\.\d+\.\d+:(\d+)',port)[0]
                  if re.findall(r'IP:\s*\d+\.\d+\.\d+\.\d+:(\d+)',port,flags=re.IGNORECASE) else None)).fillna('0')
    given_csv = given_csv.assign(user_name = part1)
    given_csv = given_csv.assign(IP = part2)
    given_csv = given_csv.assign(port_key = part3)
    given_csv = given_csv.drop_duplicates(subset=['user_name','IP','port_key'],keep='first')
    given_csv = given_csv.rename(columns={'risk_score_raw':'risk_score'})
    given_csv = given_csv.reset_index()
    given_csv = given_csv.drop(columns=['index'])
    part1 = given_csv['access_details'].apply(lambda date: re.sub(r'(\d{4})(?:/|-|\.)(\d{2})(?:/|-|\.)(\d{2})'
                                                                  , r'\1-\2-\3', date) if re.findall(
        r'\d{4}(?:/|-|\.)\d{2}(?:/|-|\.)\d{2}', date)
    else re.sub(r'(\d{2})(?:/|-|\.)(\d{2})(?:/|-|\.)(\d{4})', r'\3-\2-\1', date))
    part1 = part1.apply(lambda date: str(re.findall(r'\s*(\d{4}-\d{2}-\d{2})\s*', date)[0]))
    part2 = given_csv['access_details'].str.extract(r'\d+\s*;\s*(\w+)')[0].str.upper()
    part3 = given_csv['access_details'].str.extract(r'auth\s*:\s*(\w+)')[0]
    given_csv['access_details'] = part1 + ' ; ' + part2 + ' ; ' + part3
    given_csv['risk_score'] = given_csv['risk_score'].apply(lambda rate: float(re.findall(r'[\d.]+', rate)[0]))
    return given_csv
secure_data_csv = parsing_csv_user_info(parsed_csv_data)

def parsing_json(given_csv):
    given_csv = given_csv.rename(columns={'full_name':'user_name'})
    given_csv['user_name'] = given_csv['user_name'].str.lower().str.title().apply(lambda name: re.sub('_',' ',name))
    given_csv['emp_id'] = given_csv['emp_id'].str.zfill(5)
    given_csv['skills_counts'] = given_csv['skills'].str.count(',') + 1
    given_csv['sql_skill'] = given_csv['skills'].apply(lambda user_skills: True if 'sql' in user_skills.lower() else False)
    given_csv = given_csv.drop(columns=['index'])
    given_csv['email'] = given_csv['email'].str.lower()
    return given_csv
applications_csv = parsing_json(final_df)

def merge_csv(given_csv1,given_csv2):
    final_security_df = pd.merge(given_csv1,given_csv2,on='user_name',how='outer')
    final_security_df = final_security_df.fillna(False)
    final_security_df = final_security_df.drop(columns=['user_info'])
    final_security_df = final_security_df.loc[(final_security_df['event_id'] != False)]
    final_security_df['priority'] = final_security_df['risk_score'].apply(lambda risk: 'CRITICAL' if risk > 0.8 else(
       'MEDIUM' if 0.8 >= risk >= 0.4 else 'LOW'))
    final_security_df = final_security_df.sort_values(by='risk_score',ascending=False)
    final_security_df.columns = final_security_df.columns.str.lower().str.replace(' ','_')
    final_security_df.to_csv('Unity_csvS.csv', index=False, sep=';')
merge_csv(secure_data_csv,applications_csv)
