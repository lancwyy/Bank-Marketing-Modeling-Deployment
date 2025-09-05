# run_modeling.py

import pandas as pd
from sklearn.model_selection import GridSearchCV, RepeatedStratifiedKFold
from sklearn.pipeline import Pipeline
from preprocessing.preprocessor import build_preprocessor
from .models import get_models
from .param_grid import param_grids
from sklearn.metrics import roc_auc_score

from sklearn.base import is_classifier, is_regressor

# Load and prepare data
df = pd.read_csv("data/bank.csv")
df['deposit'] = df['deposit'].map({'yes': 1, 'no': 0})
df['default'] = df['default'].map({'yes': 1, 'no': 0})
df['housing'] = df['housing'].map({'yes': 1, 'no': 0})
df['loan'] = df['loan'].map({'yes': 1, 'no': 0})

month_map = {'jan':1, 'feb':2, 'mar':3, 'apr':4, 'may':5, 'jun':6, 'jul':7, 'aug':8, 'sep':9, 'oct':10, 'nov':11, 'dec':12}
df['month'] = df['month'].map(month_map)

X = df.drop(columns=["deposit", "pdays"], axis=1)
y = df["deposit"]

# Cross-validation setup: 30 trials
cv = RepeatedStratifiedKFold(n_splits=5, n_repeats=6, random_state=42)

# Run modeling
results = []

for name, model in get_models().items():
    print(f"\n🔍 Tuning model: {name}")
    
    print(f"\nModel name: {name}")
    print(f"Model object: {model}")
    print(f"Is a classifier? {is_classifier(model)}")
    print(f"Is a regressor? {is_regressor(model)}")
    print(f"Type of model: {type(model)}\n\n")

    pipe = Pipeline([
        ("preprocessor", build_preprocessor()),
        ("classifier", model)
    ])
    
    preprocessor = build_preprocessor()    
    X_processed = preprocessor.fit_transform(X)

    grid = param_grids.get(name, {})
    
    search = GridSearchCV(
        estimator=pipe,
        param_grid=grid,
        cv=cv,
        scoring="roc_auc",
        return_train_score=False,
        n_jobs=-1,
        verbose=1, 
        error_score='raise'
    )
    
    search.fit(X, y)
    
    # Extract fold-level scores
    fold_scores = search.cv_results_['mean_test_score']
    mean_auc = round(search.best_score_, 4)
    std_auc = round(search.cv_results_['std_test_score'][search.best_index_], 4)
    
    results.append({
        "model": name,
        "mean_auc": mean_auc,
        "std_auc": std_auc,
        "best_params": search.best_params_
    })

# Display summary
print("\n📊 Model Comparison (30-trial CV):")
for res in results:
    print(f"{res['model']:10s} | AUC: {res['mean_auc']:.4f} ± {res['std_auc']:.4f} | Params: {res['best_params']}")

# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("modeling/results.csv", index=False)
print("\n✅ Results saved to modeling/results.csv")
