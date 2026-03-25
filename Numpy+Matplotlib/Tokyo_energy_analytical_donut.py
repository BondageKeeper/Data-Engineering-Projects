raw_smart_city_data = """
{
  "city": "Neo-Tokyo",
  "monitoring_date": "2026-03-26",
  "districts": [
    {
      "name": "Shibuya",
      "sectors": {
        "Residential": "Usage: 4500.50 kWh",
        "Commercial": "3200.20!!",
        "Transport": "null_detected",
        "Industrial": " 1200.10_v1 "
      }
    },
    {
      "name": "Shinjuku",
      "sectors": {
        "Industrial": "8900.00_Unit",
        "Commercial": " 5100.75 ",
        "Residential": "Error_999",
        "Public": "1500.40"
      }
    },
    {
      "name": "Minato",
      "sectors": {
        "Transport": "2200.40_v2",
        "Industrial": " 7500.10_Fixed",
        "Residential": " 1200.30 ",
        "Public": " 900.50_est "
      }
    }
  ]
}
"""
converted_data = json.loads(raw_smart_city_data)
districts_energy_info = []
for sector in converted_data['districts']:
    districts_energy_info.append(sector['sectors'])

def sort_out_energy_quantity(given_list):
    total_info = {}
    for department in given_list:
        for type_consumerism , energy_quantity in department.items():
            if re.findall(r'\s?[\d.]+',energy_quantity):
                sorted_energy_quantity = float(re.findall(r'([\d.]+)',energy_quantity)[0])
            else:
                sorted_energy_quantity = 0.0
            if sorted_energy_quantity > 0:
                if type_consumerism in total_info:
                    total_info[type_consumerism] += sorted_energy_quantity
                else:
                    total_info[type_consumerism] = sorted_energy_quantity
    return total_info
types_enumeration = list(sort_out_energy_quantity(districts_energy_info).keys())
energy_enumeration = list(sort_out_energy_quantity(districts_energy_info).values())

def render_statistics(types,energy):
    print(types)
    arr_energy = np.array(energy)
    total_consumption = np.sum(arr_energy)
    figure , axis = plt.subplots(figsize=(10,6))
    axis.pie(arr_energy,labels=types,colors=['#ccd5ae','#e9edc9','#fefae0','#faedcd','#d4a373'],shadow=True,explode=(0.1,0.1,0.1,0.03,0.03),
             wedgeprops=dict(width=0.7,edgecolor='white'),textprops=dict(fontsize=14,weight='bold',color='#e4c1f9'),autopct='%1.1f%%',
             pctdistance=0.7)
    axis.set_title('Distribution of consumption of energy in Tokyo:',color='#ff99c8',weight='bold',fontsize=18)
    axis.annotate(text=f'{total_consumption} kWh',xy=(0,0),xytext=(-0.29,0),color='#ff99c8',weight='bold',fontsize=12)
    plt.tight_layout()
    plt.show()
render_statistics(types_enumeration,energy_enumeration)
