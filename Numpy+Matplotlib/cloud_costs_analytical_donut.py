raw_infrastructure_data = """
{
  "project": "GLOBAL_CLOUD_MIGRATION",
  "nodes": [
    {
      "region": "US-EAST-1 (N. Virginia)",
      "services": {
        "compute": "Cost: 1200.50 USD / month",
        "storage": "Cost: 450.75 $",
        "database": "ERROR: data_leak_test"
      }
    },
    {
      "region": "EU-CENTRAL-1 (Frankfurt)",
      "services": {
        "compute": " 850.20_USD ",
        "storage": "310.00 USD",
        "network": " 125.50_USD "
      }
    },
    {
      "region": "AP-NORTHEAST-1 (Tokyo)",
      "services": {
        "compute": "JPY_equiv: 950.00 $",
        "storage": "null",
        "AI_models": "1500.80 !!! "
      }
    }
  ]
}
"""
converted_data = json.loads(raw_infrastructure_data)
important_keys = []
for department in converted_data['nodes']:
    important_keys.append(department['services'])

def sort_out_costs(given_list):
    totals = {}
    for kind in given_list:
        for field , cost in kind.items():
            if re.findall(r'\s?([\d.]+)\s?',cost):
                sorted_cost = float(re.findall(r'\s?([\d.]+)',cost)[0])
            else:
                 sorted_cost = 0.0
            if sorted_cost > 0:
                if field in totals:
                    totals[field] += sorted_cost
                else:
                    totals[field] = sorted_cost
    return totals
final_sorted_values = sort_out_costs(important_keys)
total_names = list(final_sorted_values.keys())
total_costs = list(final_sorted_values.values())

def render_analytical_donut(names,costs):
    arr_costs = np.array(costs)
    sum_costs = sum(arr_costs)
    figure , axis = plt.subplots(figsize=(10,6))
    axis.pie(arr_costs,labels=names,colors=['#7bdff2','#b2f7ef','#eff7f6','#f7d6e0'],shadow=True,explode=(0.1,0,0,0),
             textprops=dict(color='#7bdff2',weight='bold',fontsize=6),wedgeprops=dict(width=0.6,edgecolor='white'))
    axis.annotate(text = f'Total amount: {sum_costs}$',xy=(0,0),xytext=(-0.35,0),color='#7bdff2',weight='bold',fontsize=8)
    plt.tight_layout()
    plt.show()
render_analytical_donut(total_names,total_costs)
