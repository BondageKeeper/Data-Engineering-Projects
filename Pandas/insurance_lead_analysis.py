import pandas as pd
import re
import matplotlib.pyplot as plt
def sort_out_csv():
    df = pd.read_csv('Health Insurance Lead Prediction Raw Data.csv',sep=',')
    df['Accomodation_Type'] = df['Accomodation_Type'].apply(lambda el: el.strip(' ').lower())
    df['Is_Spouse'] = df['Is_Spouse'].apply(lambda el: True if el == 'Yes' else False)
    df['City_Code'] = df['City_Code'].apply(lambda code: int(re.findall(r'\w+(\d+)',code)[0]))
    df['Health Indicator'] = df['Health Indicator'].mode()[0]
    df['Holding_Policy_Duration'] = df['Holding_Policy_Duration'].fillna(0)
    ages = df['Upper_Age']
    average_age = df['Upper_Age'].mean()
    counts = df['Accomodation_Type'].value_counts()
    df.to_csv('Cleaned_Insurance_Health_Lead',index=True,sep=',')
    return counts , ages , average_age
type_amount = sort_out_csv()[0]
type_ages = sort_out_csv()[1]
type_average = sort_out_csv()[2]

COLORS = ['#ff70a6','#ff9770']
def render_donut(counts,ages,average_age):
    figure , axis = plt.subplots(nrows=1,ncols=2,figsize=(9,6))
    axis[0].pie(counts,labels=counts.index,colors=COLORS,autopct='%1.1f%%',wedgeprops=dict(width=0.5,edgecolor='white'),shadow=True,explode=(0.1,0),
            pctdistance=0.75,textprops=dict(color='#70d6ff',weight='bold'))
    axis[0].set_title('Distribution of the types of accomodation',color='#70d6ff',weight='bold')
    axis[1].hist(ages,bins=20,color='#ff70a6',edgecolor='black',width=0.95)
    axis[1].set_title('Distribution of different ages',color='#ff70a6',weight='bold')
    axis[1].axvline(average_age,color='red',linestyle='dashed',label='Average age')
    axis[1].legend()
    plt.tight_layout()
    plt.show()

render_donut(type_amount,type_ages,type_average)
