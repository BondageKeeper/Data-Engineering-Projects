csv_data = {
    'order_date': ['2023-10-01', '2023-10-01', '2023-10-02', '2023-10-02', '2023-10-03'],
    'item_id': [101, 101, 101, 102, 103],
    'qty': [1, 2, 1, None, 5],
    'raw_price': ['$1000', '$25.5', '$1000', '$500!', '$1000']
}
df_sales = pd.DataFrame(csv_data)

json_raw = """
[
    {"info": "ID:101; NAME:Laptop Pro; CAT:[Tech, Work]"},
    {"info": "ID:102; NAME:Mouse Wireless; CAT:[Tech, Home]"},
    {"info": "ID:103; NAME:Monitor 4K; CAT:[Tech, Office]"}
]
"""
converted_json = json.loads(json_raw)
extracted_info = []
for thing in converted_json:
    extracted_info.append(list(thing.values())[0])

def sort_out_json_file(given_list):
    item_id = []
    item_name = []
    categories = []
    for user in given_list:
        gotten = int(re.findall(r'ID:\s?(\d+)\s?;',user)[0])
        item_id.append(gotten)
        item_name.append(re.findall(r'NAME:\s?([\w ]+)\s?;',user,flags=re.IGNORECASE)[0])
        categories.append(re.findall(r'(?<=\[)(.*?)(?=\])',user)[0])
    new_csv_from_json = pd.DataFrame({'item_id':item_id,
                                      'item_name':item_name,
                                      'categories':categories})
    print(categories)
    return new_csv_from_json
csv_from_json = sort_out_json_file(extracted_info)

def sort_out_csv(given_df):
    given_df = given_df.drop_duplicates(subset=['item_id'],keep='first')
    given_df_time_iterator = pd.to_datetime(given_df['order_date'])
    day_df = given_df_time_iterator.dt.day
    given_df = given_df.assign(day = day_df)
    given_df['qty'] = given_df['qty'].fillna(given_df['qty'].mean())
    given_df['raw_price'] = given_df['raw_price'].apply(lambda price: float(re.findall(r'([\d.]+)',price)[0]))
    return given_df
original_csv = sort_out_csv(df_sales)

def unity_of_files(csv1,csv2):
    final_csv = pd.merge(csv1,csv2,on='item_id',how='outer')
    final_csv = final_csv.explode(['categories'])
    final_csv['categories'] = final_csv['categories'].str.split(', ')
    final_csv = final_csv.explode(['categories'])
    final_csv = final_csv.reset_index(drop=True)
    final_csv.to_csv('United_files',index=False,sep=';')
unity_of_files(csv_from_json,original_csv)
