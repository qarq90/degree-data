import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('games_data.csv')

num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
X = df[[num_cols[0]]].values
y = df[num_cols[1]].values

X_b = np.c_[np.ones((len(X),1)), X]
lam = 1.0
I = np.eye(X_b.shape[1]); I[0,0] = 0
theta = np.linalg.pinv(X_b.T @ X_b + lam*I) @ X_b.T @ y
y_pred = X_b @ theta

plt.figure()
plt.scatter(X, y)
plt.plot(X, y_pred)
plt.title('Ridge Regression')
plt.xlabel(num_cols[0])
plt.ylabel(num_cols[1])
plt.show()

R = np.corrcoef(X.flatten(), y)[0,1]
print("R =", R)