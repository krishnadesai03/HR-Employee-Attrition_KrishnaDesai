# -*- coding: utf-8 -*-
"""employee-attrition-random-forest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OtWhIkMuqOjAMMHgoGNiwgc8OzNrgfw6

# **Data Analysis and Visualisation**
"""

#We have taken dataset from Kaggle
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python


import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
df.head()

df.shape

df.describe()

df.isnull().sum()

attrition_count = pd.DataFrame(df['Attrition'].value_counts())
attrition_count

plt.pie(attrition_count['Attrition'] , labels = ['No' , 'Yes'] , explode = (0.2,0))

BusinessTravel_count = pd.DataFrame(df['BusinessTravel'].value_counts())
BusinessTravel_count

plt.pie(BusinessTravel_count['BusinessTravel'] , labels = ['Travel_Rarely' , 'Travel_Frequently' , 'Non-Travel'] , explode = (0.2,0,0))

sns.countplot(df['Attrition'])



sns.countplot(df['OverTime'])

df.drop(['EmployeeCount' , 'EmployeeNumber'] , axis = 1)

attrition_dummies = pd.get_dummies(df['Attrition'])
attrition_dummies.head()

gender_dummies = pd.get_dummies(df['Gender'])
gender_dummies.head()

df = pd.concat([df, attrition_dummies] , axis = 1)
df.head()

df = df.drop(['Attrition' , 'No'] , axis = 1)
df.head()

sns.barplot(x = 'Gender' , y = 'Yes', data = df)

sns.barplot(x = 'Department', y = 'Yes', data = df)

sns.barplot(x = 'BusinessTravel', y = 'Yes', data = df)

plt.figure(figsize = (10,6))
sns.heatmap(df.corr())

df = df.drop(['Age' , 'JobLevel'], axis = 1)

"""# **Data Preprocessing**
Converting String columns into integers
"""

from sklearn.preprocessing import LabelEncoder
for column in df.columns:
    if df[column].dtype==np.number:
        continue
    else:
        df[column]=LabelEncoder().fit_transform(df[column])

"""# **Model Building**"""

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators = 10, criterion = 'entropy', random_state = 0)

x  = df.drop(['Yes'], axis = 1)
y = df['Yes']

x_train, x_test , y_train, y_test = train_test_split(x,y, test_size = 0.3, random_state = 0)

x_train.head()

rf.fit(x_train, y_train)

rf.score(x_train, y_train)

"""# **Predicting for x_test**"""

pred = rf.predict(x_test)

from sklearn.metrics import accuracy_score

accuracy_score(y_test, pred)

"""# **Accuracy for Tested Data = 85.26 %**"""