raw_logistics_data = """[{
  "delivery_batch": "SHIP-99-ALPHA",
  "orders": [
    {
      "order_id": "ORD_001",
      "info": "Item: Laptop | Price: 1 200,50 USD | Date: 2024/05/12",
      "customer": "  ivanov.i@mail.ru  ",
      "tracking": "TRK888222111 (Status: In Transit)"
    },
    {
      "order_id": "ORD_002",
      "info": "Item: Mouse | Price: 25.00 EUR | Date: 15-06-2024",
      "customer": "PETROV_WORK@COMPANY.COM",
      "tracking": "none"
    },
    {
      "order_id": "ORD_003",
      "info": "Item: Keyboard | Price: 15000 RUB | Date: 01.01.2024",
      "customer": "wrong_email_123",
      "tracking": "TRK555444333 (Status: DELIVERED)"
    },
    {
      "order_id": "ORD_004",
      "info": "Item: Monitor | Price: 450,75 USD | Date: 2024.12.31",
      "customer": "   Sidor.S@yandex.ru",
      "tracking": "  TRK111000999 (Status: pending)  "
    }
  ]
}]"""

orders_data = json.loads(raw_logistics_data)
id_orders = orders_data[0]['orders']
items_info = []
emails_info = []
dates_info = []
tracking_info = []
for order in id_orders:

    staff_name = order['info']
    items_info.append(staff_name)

    email_name = order['customer']
    emails_info.append(email_name)

    dates_name = order['info']
    dates_info.append(dates_name)

    tracking_name = order['tracking']
    tracking_info.append(tracking_name)


def sort_out_items_info(given_list):
    only_prices = []
    only_names = []
    for item in given_list:
        names = re.findall('Item:\s*(\w+)\s*\|',item)
        prices = re.findall(r'Item:\s*\w+\s*\|\s*Price:\s*([\w., ]+)',item)
        corrected_price = re.sub(',','.',prices[0])
        corrected_price = re.sub('(?<=\d)\s+(?=\d)','',corrected_price)
        only_prices.append(corrected_price)
        only_names.append(names[0])
    return only_names , only_prices
items_new_info = sort_out_items_info(items_info)

def sort_out_date(given_list):
    only_date = []
    for date in given_list:
        date_search = re.findall('\s?Date:\s?[\w/\-.]+',date)[0] #YYYY-MM-DD - this is a desirable pattern
        if re.findall(r'\s?Date:\s?(\d{2})(?:-|.|/)(\d{2})(?:-|.|/)(\d{4})',date_search):
            pattern_date_1 = re.sub(r'\s?Date:\s?(\d{2})(?:-|.|/)(\d{2})(?:-|.|/)(\d{4})',r'\3-\2-\1',date_search)
            only_date.append(pattern_date_1)
        if re.findall(r'\s?Date:\s?(\d{4})(?:-|.|/)(\d{2})(?:-|.|/)(\d{2})',date_search):
            pattern_date_2 = re.sub(r'\s?Date:\s?(\d{4})(?:-|.|/)(\d{2})(?:-|.|/)(\d{2})',r'\1-\2-\3',date_search)
            only_date.append(pattern_date_2)
    return only_date
new_date = sort_out_date(dates_info)

def sort_out_tracking(given_list):
    new_tracks = []
    for track in given_list:
        if re.findall(r'\s*\w+\s?\(Status:.*?\)',track):
            new_track = re.sub('(?<= )\s+(?=\w)','',track)
            new_tracks.append(new_track)
        else:
            new_track = '!INVALID_TRACK!'
            new_tracks.append(new_track)
    return new_tracks
new_updates_tracks = sort_out_tracking(tracking_info)


def sort_out_emails(given_list):
    current_emails = []
    for email in given_list:
        email = re.sub(r'','',email).lower()
        if re.findall(r'[\w_.-]+@\w+\.(?:ru|com)',email):
             current_emails.append(email)
        else:
            email = '!INVALID_EMAIL!'
            current_emails.append(email)
    return current_emails
checked_emails = sort_out_emails(emails_info)


def update_orders_info(given_names,given_emails,given_date,given_tracks):
    for index,item1 in enumerate(given_names[0]):
        orders_data[0]['orders'][index]['info'] = item1
    for index,item2 in enumerate(given_names[1]):
        orders_data[0]['orders'][index]['Price'] = item2
    for index,item3 in enumerate(given_emails):
        orders_data[0]['orders'][index]['customer'] = item3
    for index,item4 in enumerate(given_date):
        orders_data[0]['orders'][index]['Date'] = item4
    for index,item5 in enumerate(given_tracks):
        orders_data[0]['orders'][index]['tracking'] = item5
update_orders_info(items_new_info,checked_emails,new_date,new_updates_tracks)


def create_new_json():
    with open('cleaned_data_2.json','w',encoding='utf-8') as new_file_2:
       json.dump(orders_data,new_file_2,indent=3)
create_new_json()



