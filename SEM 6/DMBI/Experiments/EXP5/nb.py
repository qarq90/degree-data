import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import LabelEncoder

# Dataset
data = {
    'Outlook': ['Sunny', 'Sunny', 'Overcast', 'Rain', 'Rain', 'Rain', 'Overcast', 
                'Sunny', 'Sunny', 'Rain', 'Sunny', 'Overcast', 'Overcast', 'Rain'],
    'Temperature': ['Hot', 'Hot', 'Hot', 'Mild', 'Cool', 'Cool', 'Cool', 
                   'Mild', 'Cool', 'Mild', 'Mild', 'Mild', 'Hot', 'Mild'],
    'Humidity': ['High', 'High', 'High', 'High', 'Normal', 'Normal', 'Normal',
                'High', 'Normal', 'Normal', 'Normal', 'High', 'Normal', 'High'],
    'Windy': ['Weak', 'Strong', 'Weak', 'Weak', 'Weak', 'Strong', 'Strong',
             'Weak', 'Weak', 'Weak', 'Strong', 'Strong', 'Weak', 'Strong'],
    'PlayTennis': ['No', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 
                  'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

# Create DataFrame
df = pd.DataFrame(data)

# Features and target
features = ['Outlook', 'Temperature', 'Humidity', 'Windy']
target = 'PlayTennis'

# Encode categorical variables
le = LabelEncoder()
X_encoded = df[features].copy()
for col in features:
    le.fit(df[col])
    X_encoded[col] = le.transform(df[col])

y_encoded = le.fit_transform(df[target])

# Build decision tree
dt_clf = DecisionTreeClassifier(
    criterion='entropy',  # Similar to ID3
    max_depth=3,
    random_state=42
)

dt_clf.fit(X_encoded, y_encoded)

# Create large figure for the tree
plt.figure(figsize=(20, 12))

# Plot the decision tree
plot_tree(
    dt_clf,
    feature_names=features,
    class_names=['No', 'Yes'],
    filled=True,
    rounded=True,
    fontsize=12,
    proportion=True,
    impurity=True,
    node_ids=True,
    precision=2
)

plt.title("Decision Tree - Tennis Play Prediction\n(Using ID3-like Algorithm with Entropy)", 
          fontsize=16, fontweight='bold', pad=20)
plt.tight_layout()
plt.show()