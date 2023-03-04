# Import dependencies
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import joblib

# Load the titanic dataset 
df = pd.read_csv('titanic.csv')
include = ['Age', 'Sex', 'Embarked', 'Survived'] # Only four features
df_ = df[include].copy()      # to avoid SettingWithCopyWarning

# Data Preprocessing
categoricals = []

# for col, col_type in df_.dtypes.iteritems():
for col, col_type in df_.dtypes.items():
     if col_type == 'O':
          categoricals.append(col)
     else:
          df_[col].fillna(0, inplace=True)

df_ohe = pd.get_dummies(df_, columns=categoricals, dummy_na=True)

# Logistic Regression classifier
dependent_variable = 'Survived'
x = df_ohe[df_ohe.columns.difference([dependent_variable])]
y = df_ohe[dependent_variable]
lr = LogisticRegression()
lr.fit(x, y)

# # Save your model
# joblib.dump(lr, 'model.pkl')

# # Saving the data columns from training
# model_columns = list(x.columns)
# joblib.dump(model_columns, 'model_columns.pkl')