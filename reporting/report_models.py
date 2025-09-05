# reporting/report_models.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load results
df = pd.read_csv("modeling/results.csv")

# Sort by performance
df = df.sort_values(by="mean_auc", ascending=False)

# Barplot of AUC scores
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x="model", y="mean_auc", palette="viridis")
plt.title("Model Performance (30-Trial ROC-AUC)")
plt.ylabel("Mean ROC-AUC")
plt.xlabel("Model")
plt.ylim(0.5, 1.0)
plt.tight_layout()
plt.show()

# Optional: print best params
print("\n🔍 Best Parameters per Model:")
for _, row in df.iterrows():
    print(f"{row['model']:10s} | AUC: {row['mean_auc']:.4f} ± {row['std_auc']:.4f}")
    print(f"  Params: {row['best_params']}")
