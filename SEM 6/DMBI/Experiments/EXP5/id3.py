import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.preprocessing import LabelEncoder

# Define the dataset
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
print("Dataset:")
print(df)
print("\n" + "="*50)

# Features and target
features = ['Outlook', 'Temperature', 'Humidity', 'Windy']
target = 'PlayTennis'

# Prepare data for sklearn
X = df[features]
y = df[target]

# Encode categorical variables
le = LabelEncoder()
X_encoded = X.copy()
for col in X.columns:
    X_encoded[col] = le.fit_transform(X[col])

y_encoded = le.fit_transform(y)

print("\nEncoded Features:")
print(X_encoded.head())
print(f"\nEncoded Target (0=No, 1=Yes): {y_encoded}")

# Build decision tree with entropy criterion (similar to ID3)
dt_clf = DecisionTreeClassifier(
    criterion='entropy',  # This makes it similar to ID3
    max_depth=3,
    random_state=42
)

dt_clf.fit(X_encoded, y_encoded)

# Visualize the tree
plt.figure(figsize=(15, 10))
plot_tree(
    dt_clf,
    feature_names=features,
    class_names=['No', 'Yes'],
    filled=True,
    rounded=True,
    fontsize=10
)
plt.title("ID3-like Decision Tree (using scikit-learn)", fontsize=16)
plt.tight_layout()
plt.show()

# Print tree rules
print("\n" + "="*50)
print("Decision Tree Rules:")
print("="*50)
tree_rules = export_text(
    dt_clf,
    feature_names=features,
    spacing=3,
    decimals=2
)
print(tree_rules)

# Feature importance
print("\n" + "="*50)
print("Feature Importance:")
print("="*50)
for feature, importance in zip(features, dt_clf.feature_importances_):
    print(f"{feature}: {importance:.3f}")

# Make predictions
print("\n" + "="*50)
print("Making Predictions:")
print("="*50)

# Example test cases
test_cases = [
    {'Outlook': 'Sunny', 'Temperature': 'Hot', 'Humidity': 'High', 'Windy': 'Weak'},
    {'Outlook': 'Rain', 'Temperature': 'Cool', 'Humidity': 'Normal', 'Windy': 'Strong'},
    {'Outlook': 'Overcast', 'Temperature': 'Mild', 'Humidity': 'Normal', 'Windy': 'Weak'}
]

# Convert test cases to encoded format
for i, test_case in enumerate(test_cases):
    # Encode the test case
    encoded_case = []
    for feature in features:
        # Get the label encoder for this feature
        le = LabelEncoder()
        le.fit(df[feature])  # Fit with original data
        encoded_value = le.transform([test_case[feature]])[0]
        encoded_case.append(encoded_value)
    
    # Make prediction
    prediction = dt_clf.predict([encoded_case])[0]
    probability = dt_clf.predict_proba([encoded_case])[0]
    
    print(f"\nTest Case {i+1}:")
    print(f"  Features: {test_case}")
    print(f"  Prediction: {'Yes (Play Tennis)' if prediction == 1 else 'No (Don\'t Play Tennis)'}")
    print(f"  Confidence: {probability[prediction]*100:.1f}%")
    print(f"  Probabilities: [No: {probability[0]:.2%}, Yes: {probability[1]:.2%}]")