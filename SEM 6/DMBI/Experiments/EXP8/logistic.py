import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('games_data.csv')

num_cols = df.select_dtypes(include=[np.number]).columns.tolist()
X = df[[num_cols[0]]].values
y = df[num_cols[1]].values

y_bin = (y > np.median(y)).astype(int)

X_b = np.c_[np.ones((len(X),1)), X]
w = np.zeros(X_b.shape[1])
lr = 0.01

for _ in range(500):
    z = X_b @ w
    h = 1/(1+np.exp(-z))
    grad = X_b.T @ (h - y_bin) / len(y_bin)
    w -= lr * grad

y_pred = 1/(1+np.exp(-(X_b @ w)))

plt.figure()
plt.scatter(X, y_bin)
plt.plot(X, y_pred)
plt.title('Logistic Regression')
plt.xlabel(num_cols[0])
plt.ylabel('Binary Target')
plt.show()

R = np.corrcoef(X.flatten(), y)[0,1]
print("R =", R)