import pandas as pd
import numpy as np
from scipy.stats import norm
from sklearn.model_selection import train_test_split

data = pd.read_excel("EXP8.xlsx")

cols = ["id","name","developer","genre","release_year","metacritic_score","sales_millions","peak_players"]
df = pd.DataFrame(data, columns=cols)

df = df[df["sales_millions"] > 0]

train_df, test_df = train_test_split(df, test_size=0.25, random_state=42)

print("H0: Mean sales of Action-Adventure games = Overall mean sales")
print("H1: Mean sales of Action-Adventure games > Overall mean sales\n")

population_mean = train_df["sales_millions"].mean()

sample = train_df[train_df["genre"] == "Action-Adventure"]["sales_millions"]

sample_mean = sample.mean()
sample_std = sample.std(ddof=1)
n = len(sample)

z_score = (sample_mean - population_mean) / (sample_std / np.sqrt(n))
p_value = 1 - norm.cdf(z_score)

alpha = 0.05

print("===== TRAINING SET RESULTS =====")
print(f"Sample size (n): {n}")
print(f"Sample mean: {sample_mean:.2f}")
print(f"Population mean: {population_mean:.2f}")
print(f"Z-score: {z_score:.4f}")
print(f"P-value: {p_value:.6f}\n")

output_table = pd.DataFrame({
    "value1": [round(sample_mean, 6)],
    "value2": [round(population_mean, 6)],
    "score": [round(z_score, 6)],
    "p_value": [round(p_value, 6)],
    "Hypothesis_accepted": [
        "Yes" if p_value >= alpha else "No"
    ]
})

print(output_table.to_string(index=False))

if p_value < alpha:
    print("\nDecision: Reject H0")
else:
    print("\nDecision: Fail to Reject H0")

test_population_mean = test_df["sales_millions"].mean()
test_sample = test_df[test_df["genre"] == "Action-Adventure"]["sales_millions"]

if len(test_sample) > 0:
    test_mean = test_sample.mean()
    print("\n===== TEST SET CHECK =====")
    print(f"Test sample mean: {test_mean:.2f}")
    print(f"Test population mean: {test_population_mean:.2f}")


import matplotlib.pyplot as plt

train_size = len(train_df)
test_size = len(test_df)

labels = ["Training (75%)", "Testing (25%)"]
sizes = [train_size, test_size]

plt.figure()
plt.bar(labels, sizes)

plt.title("Train-Test Split (75% - 25%)")
plt.xlabel("Dataset Split")
plt.ylabel("Number of Samples")

for i, v in enumerate(sizes):
    plt.text(i, v, str(v), ha='center', va='bottom')

plt.show()