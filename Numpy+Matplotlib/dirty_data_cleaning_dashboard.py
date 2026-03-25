import json , re
import matplotlib.pyplot as plt
import numpy as np
raw_json = """
{
  "turbine_telemetry": {
    "T-01": ["RPM: 3000", "3050_rev", "3100!!", "ERROR_999", "2980 rpm", "null_value", "3200"],
    "T-02": ["450.5 Celsius", "452.0 C", "448.2", "NONE_DATA", "455.1 C*", "460.0", "300.0_anomaly"],
    "T-03": ["Press: 12.5 bar", "12.8", "12.4 b", "NULL", "13.0", "15.5_HIGH", "5.0_LOW"]
  }
}
"""
converted_python_data = json.loads(raw_json)

def sort_out_measurements(given_data):
    total_measurements = []
    for sensor_name , sensor_values in given_data.items():
        each_sensor_list = []
        for item_measure in sensor_values:
            pattern = r'(\d+\.\d+|\d+)'
            if re.findall(pattern,item_measure):
                cleaned_item_measure = re.findall(pattern,item_measure)
                each_sensor_list.append(float(cleaned_item_measure[0]))
            else:
                each_sensor_list.append(np.nan)
        new_array = np.array(each_sensor_list)
        mask = np.isnan(new_array)
        new_array[mask] = np.nanmedian(np.round(new_array,2))
        total_measurements.append(new_array)
    return total_measurements
sorted_list = sort_out_measurements(converted_python_data['turbine_telemetry'])

def render_graphics(given_list):
    figure , axis = plt.subplots(nrows=1 , ncols = 2 , figsize=(10,6))
    glued_data = np.concatenate(given_list)
    axis[0].hist(glued_data,bins=5,rwidth=0.95,color='violet',edgecolor='black')
    axis[0].set_xlabel('Spread of numbers included in measurements',color='violet')
    axis[1].boxplot(given_list,vert=True,patch_artist=True,showmeans=True,labels=['RPM','Temperature','Pressure(bars)'],boxprops=dict(facecolor='ivory',edgecolor='black'),
                    flierprops=dict(markerfacecolor='red',marker='o'))
    axis[1].grid(axis='x')
    axis[1].set_xlabel('Graphic for tracking deviations',color='orange')
    axis[1].tick_params(axis='x',labelcolor='orange',labelsize=10)
    plt.tight_layout()
    plt.show()
render_graphics(sorted_list)

