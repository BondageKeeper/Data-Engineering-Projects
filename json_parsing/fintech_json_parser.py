raw_fintech_data = """{
  "system_info": {"node": "FIN-SRV-01", "timestamp": "2026-03-20T12:00:00Z"},
  "transactions": [
    {
      "tx_id": "TX_8810022",
      "details": {
        "sender": "  ACC-777222_Ivanov_I  ",
        "receiver": "ACC-999111_Petrov_P",
        "description": "Payment for services: #INV-99 (Amount: 15 000,00 RUb)"
      },
      "security": {
        "verification": "SMS: [4422] | IP: 192.168.1.1",
        "flags": ["high_priority", "international"]
      }
    },
    {
      "tx_id": "TX_9901133",
      "details": {
        "sender": "ACC-555444_Sidorov_S",
        "receiver": "  ACC-111000_Unknown_  ",
        "description": "Refund (Amount: 2.500,50 Usd)"
      },
      "security": {
        "verification": "APP_CONFIRM | IP: 10.0.0.45",
        "flags": []
      }
    },
    {
      "tx_id": "INVALID_TX",
      "details": "CORRUPTED_DATA_BLOCK",
      "security": null
    },
    {
      "tx_id": "TX_7770001",
      "details": {
        "sender": "ACC-000111_Murphy_A",
        "receiver": "ACC-222333_Detroit_PS",
        "description": "Fine: speed limit (Amount: 500,00 EUR)"
      },
      "security": {
        "verification": "TOKEN: {XYZ-999} | IP: 172.16.254.1",
        "flags": ["automated"]
      }
    }
  ]
}"""


transformed_fintech_data = json.loads(raw_fintech_data)
sender_list = []
receiver_list = []
description_list = []
verification_list = []
list_tx_id = []
WARNING = 'UNKNOWN DATA'
for transaction in transformed_fintech_data['transactions']:

    if 'sender' in transaction['details']:
        sender = transaction['details']['sender']
        sender_list.append(sender)
    else:
        transaction['details'] = {'sender': WARNING}
        sender_list.append(WARNING)

    if 'receiver' in transaction['details']:
        receiver = transaction['details']['receiver']
        receiver_list.append(receiver)
    else:
        transaction['details']['receiver'] = WARNING
        receiver_list.append(WARNING)

    if 'description' in transaction['details']:
        description = transaction['details']['description']
        description_list.append(description)
    else:
        transaction['details']['description'] = WARNING
        description_list.append(WARNING)

    if transaction.get('security') and 'verification' in transaction['security']:
        verification = transaction['security']['verification']
        verification_list.append(verification)
    else:
        transaction['security'] = {'verification': WARNING}
        verification_list.append(WARNING)

    tx_id = transaction['tx_id']
    list_tx_id.append(tx_id)


def sort_out_headline(given_list_from,given_list_to):
    senders_title_list = []
    pattern_1 = r'ACC-\d{6}[\w_.]+'
    pattern_2 = r'\s+'
    pattern_3 = r'ACC-(\d{6})_(\w+)(?=_)\w*'
    for sender_title in given_list_from:
        if re.findall(pattern_1,sender_title):
            new_sender_title = re.sub(pattern_2,'',sender_title)
            new_sender_title = re.sub(pattern_3,r'Account: \1 Surname: \2',new_sender_title)
            senders_title_list.append(new_sender_title)
        else:
            senders_title_list.append(WARNING)
    receivers_title_list = []
    for receiver_title in given_list_to:
        if re.findall( pattern_1,receiver_title):
            new_receiver_title = re.sub(pattern_2,'',receiver_title)
            new_receiver_title = re.sub(pattern_3,r'Account: \1 Surname: \2',new_receiver_title)
            receivers_title_list.append(new_receiver_title)
        else:
            receivers_title_list.append(WARNING)
    return senders_title_list , receivers_title_list
senders_new_info = sort_out_headline(sender_list,receiver_list)[0]
receivers_new_info = sort_out_headline(sender_list,receiver_list)[1]


def sort_out_tx_id(given_list):
    sorted_tx_id = []
    for tx in given_list:
        if re.findall(r'TX_\d+',tx,flags=re.IGNORECASE):
            new_tx = re.findall(r'TX_(\d+)',tx,flags=re.IGNORECASE)[0]
            sorted_tx_id.append(new_tx)
        else:
            new_tx = 'INVALID_TX'
            sorted_tx_id.append(new_tx)
    return sorted_tx_id
tx_new_info = sort_out_tx_id(list_tx_id)


def sort_out_payments(given_list):
    amount_list = []
    currency_list = []
    for payment_info in given_list:
        if re.findall(r'Amount:\s?[\d.,]+\s?\w+',payment_info):
            amount = re.findall(r'Amount:\s?([\d,. ]+)',payment_info)
            amount = re.sub(r'(?<=\d)( |\.)(?=\d)','',amount[0])
            amount = re.sub(r'(?<=\d),(?=\d)','.',amount).rstrip(' ')
            amount_list.append(amount)
            currency = re.findall(r'(RUB|USD|EUR)', payment_info, flags=re.IGNORECASE)[0].upper()
            currency_list.append(currency)
        else:
            amount_list.append(WARNING)
            currency_list.append(WARNING)
    return amount_list,currency_list
amount_new_info = sort_out_payments(description_list)[0]
currency_new_info = sort_out_payments(description_list)[1]

def check_verification(given_list):
    ip_list = []
    code_list = []
    for correspondence in given_list:
        if re.findall(r'\s?\|\s?IP:\s?[\d.]+',correspondence,flags=re.IGNORECASE):
            ip_data = re.findall(r'IP:\s?([\d.]+)',correspondence,flags=re.IGNORECASE)[0]
            ip_list.append(ip_data)
        else:
            ip_list.append(WARNING)
        if re.findall(r'\s?(?:\[|\{)[\w-]+(?:\]|\})\s?',correspondence,flags=re.IGNORECASE):
            code_data = re.findall(r'\s?(?:\[|\{)(.*?)(?:\]|\})\s?',correspondence,flags=re.IGNORECASE)[0]
            code_list.append(code_data)
        else:
            code_list.append(WARNING)
    return ip_list,code_list
ip_new_info = check_verification(verification_list)[0]
code_new_info = check_verification(verification_list)[1]


def update_users_data(new_senders_list,new_receivers_list,new_amount_list,new_currency_list,new_info_list,new_code_list,new_tx_list):
    for index,staff1 in enumerate(new_senders_list):
        transformed_fintech_data['transactions'][index]['details']['sender'] = staff1
    for index,staff2 in enumerate(new_receivers_list):
        transformed_fintech_data['transactions'][index]['details']['receiver'] = staff2
    for index,staff3 in enumerate(new_amount_list):
        transformed_fintech_data['transactions'][index]['details']['description'] = {'amount': staff3}
    for index,staff4 in enumerate(new_currency_list):
        transformed_fintech_data['transactions'][index]['details']['description']['currency'] = staff4
    for index,staff5 in enumerate(new_info_list):
        transformed_fintech_data['transactions'][index]['security']['verification'] = {'IP': staff5}
    for index,staff6 in enumerate(new_code_list):
        transformed_fintech_data['transactions'][index]['security']['verification']['confirm code'] = staff6
    for index,staff7 in enumerate(new_tx_list):
        transformed_fintech_data['transactions'][index]['tx_id'] = staff7
update_users_data(senders_new_info,receivers_new_info,amount_new_info,currency_new_info,ip_new_info,code_new_info,tx_new_info)


def delete_invalid_tx_id():
    for index , _ in enumerate(transformed_fintech_data['transactions']):
        if transformed_fintech_data['transactions'][index]['tx_id'] == 'INVALID_TX':
            del transformed_fintech_data['transactions'][index]
delete_invalid_tx_id()


def convert_into_json_format():
    with open('cleaned_data_3.json','w',encoding='utf-8') as new_file_3:
        json.dump(transformed_fintech_data,new_file_3,indent=3)
convert_into_json_format()

