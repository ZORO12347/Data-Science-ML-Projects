# -*- coding: utf-8 -*-
"""MINOR PROJECT 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1qqDYIk2SCYcxtg7H8w6tfM65PEAQVyIj

# ***MINOR PROJECT 1 (TAKE ANY DATASET OF YOUR CHOICE AND PERFORM EXPLORATORY DATA ANALYSIS)***

---
"""

import pandas as pd
df=pd.read_csv('/content/heart_failure_clinical_records.csv')
df

df.info()

df.shape #299 rows and 13 cols

df.size #Total number of elements in the dataframe

#Finding number of unique elements/values in each and every column
df.nunique()

#VISUALISATION - SEABORN
#How many patients are suffering from anaemia
import seaborn as sns
sns.countplot(x='anaemia',data=df)

#The exact count of patients suffering from anaemia
df.groupby('anaemia').size()

#distribution plot for age
import seaborn as sns
sns.distplot(df['age'])

#to find out the exact count of number of males and no of females
df.groupby('sex').size()

import numpy as np
#np.sum will tell the sum of number of elements in the specific range
young=np.sum((df['age']>=0)&(df['age']<20))
adult=np.sum((df['age']>=20)&(df['age']<40))
midage=np.sum((df['age']>=40)&(df['age']<60))
old=np.sum((df['age']>=60))
print(young)
print(adult)
print(midage)
print(old)

#to find out the youngest person in the records
np.min(df['age'])

#to find out the oldest person in the records
np.max(df['age'])

#How many males and females smoke
male=np.sum((df['sex']==1)&df['smoking']==1)
female=np.sum((df['sex']==0)&df['smoking']==1)
print(male)
print(female)

#How many patients have died
np.sum(df['DEATH_EVENT']==1)

#How many patients have died by only smoking
np.sum((df['smoking']==1)&(df['diabetes']==0)&(df['high_blood_pressure']==0)&(df['anaemia']==0)&df['DEATH_EVENT']==1)

#How many patients who died have high blood pressure
np.sum((df['high_blood_pressure']==0)&df['DEATH_EVENT']==1)

#How many patients who have diabetes and anaemia are dead
np.sum((df['diabetes']==0)&(df['anaemia']==0)&df['DEATH_EVENT']==1)

#to find out the highest value of serum_creatinine
np.max(df['serum_creatinine'])

#Plotting the configuration of serum_creatinine in the graph
df['serum_creatinine'].value_counts().plot(kind='bar')
plt.title('CONFIGURATION OF SERUM CREATININE')

#To find out patients of what age have more number of platelets
import seaborn as sns
import matplotlib.pyplot as plt

sns.barplot(x=df['age'],y=df['platelets'])
plt.title('NO. OF PLATELETS ACCORDING TO AGE')
plt.xticks(rotation='vertical',fontsize=7)
# Show the plot
plt.show()

#Plotting the count of ejection fraction
sns.displot(df['ejection_fraction'])
plt.title('COUNT OF EJECTION FRACTION')

#The configuration of serum sodium as per age for both males and females
import seaborn as sns
import matplotlib.pyplot as plt

sns.swarmplot(data=df, x="serum_sodium", y="age", hue="sex")
plt.xticks(rotation='vertical')

plt.show()

#to find out the most common value of creatinine_phosphokinase of the laptop
df['creatinine_phosphokinase'].value_counts()

#To find out the highest and least value of serum sodium
max=np.max(df['serum_sodium'])
min=np.min(df['serum_sodium'])
print(max)
print(min)