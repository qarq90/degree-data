import scipy.stats as stats

group1 = [21, 24, 22, 23, 25]
group2 = [28, 27, 30, 29, 31]
group3 = [18, 20, 19, 22, 21]

f_stat, p_value = stats.f_oneway(group1, group2, group3)

print(f"F-statistic: {f_stat:.4f}")
print(f"P-value: {p_value:.4f}")

alpha = 0.05
if p_value < alpha:
    print("Reject H0: At least one group mean is different.")
else:
    print("Fail to reject H0: No significant difference between group means.")