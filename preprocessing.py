import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import pickle


base = pd.read_csv('./transactions.csv')
base = base.drop('transaction_date', axis=1)
base = base.drop('card_number', axis=1)
# print(base['device_id'][2])
print(base[base['device_id'].isnull()])

base.loc[base['device_id'].isnull(), 'device_id'] = 0


# print(base.isnull().sum())

## Predictors and Classifiers ##
x, y = base.iloc[:, 1:5].values, base.iloc[:, 5].values

# # # ## Encoder ##
# card_number_label_encoder = LabelEncoder()
# x[:, 2] = card_number_label_encoder.fit_transform(x[:, 2])


## Scaler ## 
scaler_base = StandardScaler()
x_base = scaler_base.fit_transform(x)

## Train split ## 
x_training, x_testing, y_training, y_testing = train_test_split(x, y, test_size=0.15, random_state=0)

with open('base.pkl', mode='wb') as f:
  pickle.dump([x_training, y_training, x_testing, y_testing], f)