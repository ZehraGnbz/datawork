
#import csv
#with open('country_vaccination_stats.csv') as csvfile:
# reader = csv.reader(csvfile)
import pandas as pd

df = pd.read_csv('country_vaccination_stats.csv')
#to make nan to zero
df['daily_vaccinations'] = df['daily_vaccinations'].fillna(0)
print(df.to_string())

#too find medians and sort by
listOfMedians = df.groupby(['country'])['daily_vaccinations'].median().sort_values(ascending=False)
print(listOfMedians)

#to find june 1st
listOfDates = df.sort_values(by=['date'])
print(listOfDates)
print(df[df['date']>'1/6/2021']['daily_vaccinations'].sum())
