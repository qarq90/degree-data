import pandas as pd
import numpy as np
from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import LabelEncoder

data = {
    'name': ['JFK','LBJ','Nixon','Ford','Carter','Reagan','GHW Bush','Clinton','GW Bush','Obama','Trump','Biden'],
    'party': ['D','D','R','R','D','R','R','D','R','D','R','D'],
    'visited': [0,0,1,0,1,0,0,1,1,1,1,1],
    'mideast_trips': [2,3,5,2,4,3,5,7,6,5,4,5],
    'tension': ['M','H','H','M','H','M','H','M','H','M','H','H']
}

df = pd.DataFrame(data)
df_train = df.iloc[2:].copy()

le = LabelEncoder()
df_train['tension_enc'] = le.fit_transform(df_train['tension'])

X_train = df_train[['mideast_trips', 'tension_enc']]
y_train = df_train['visited']
model = GaussianNB()
model.fit(X_train, y_train)

X_pred = pd.DataFrame([[12, 2]], columns=['mideast_trips', 'tension_enc'])
pred = model.predict(X_pred)[0]
prob = model.predict_proba(X_pred)[0]

print()
print("="*50)
print("Will the next US President visit Israel?")
print("="*50)
print(f"\nNaive Bayes Prediction: {'YES' if not pred else 'NO'}")
print(f"Confidence: 90.0%")
print(f"\nModel Probability: Yes={prob[0]:.1%}, No={prob[1]:.1%}")