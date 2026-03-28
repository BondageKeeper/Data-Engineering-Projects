import pandas as pd
import re
df = pd.read_csv('global_freelancers_raw.csv',sep=',')
df['gender'] = df['gender'].apply(lambda gender: 'Female' if gender.lower().startswith('f') else 'Male')
df['country'] = df['country'].apply(lambda country: country.strip(' ').capitalize())
df['language'] = df['language'].apply(lambda language: language.strip(' ').capitalize())
df['hourly_rate'] = df['hourly_rate (USD)'].apply(lambda shift: float(re.findall(r'([\d.]+)',str(shift))[0])
    if re.findall(r'[\d.]+',str(shift)) else None)
df['hourly_rate'] = df['hourly_rate'].fillna(df.groupby('primary_skill')['hourly_rate'].mean())
df['client_satisfaction'] = df['client_satisfaction'].apply(lambda estimation: float(str(estimation).strip('%')) * 0.01)
df['is_active'] = df['is_active'].apply(lambda status: True if re.findall(r'Y|yes|1',str(status)) else False)
df['rank'] = df['years_of_experience'].apply(lambda years: 'Junior' if years < 3
   else('Middle' if 3 < years < 7 else('Senior' if 7 <= years < 15 else 'Expert')))
average_stakes = df.groupby('primary_skill').agg({'hourly_rate': 'mean' ,'client_satisfaction': 'mean'})
analysis_df = df.loc[(df['primary_skill'] == 'Data Analysis')]
country_salaries = analysis_df.groupby('country')['hourly_rate'].mean()
sorted_countries = country_salaries.sort_values(ascending=True)
top_3_countries = sorted_countries.head(3)
print(top_3_countries)
print(df['rank'])
print(df.info())
df.to_csv('freelance_gold_standard.csv',index=True,sep=',')
