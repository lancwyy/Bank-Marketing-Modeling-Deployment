# deployed-model-v1.py

import pandas as pd
import joblib
from xgboost import XGBClassifier
from sklearn.pipeline import Pipeline
from preprocessing.preprocessor import build_preprocessor, prepare_data

# 1. Load and prepare full dataset
df = pd.read_csv("data/bank.csv")
df = prepare_data(df)

X = df.drop("deposit", axis=1)
y = df["deposit"]

# 2. Build preprocessing pipeline
preprocessor = build_preprocessor()

# 3. Define final XGBoost model with optimal parameters
xgb_model = XGBClassifier(
    learning_rate=0.1,
    max_depth=3,
    n_estimators=100,
    eval_metric='logloss'
)

# 4. Combine into full pipeline
final_pipeline = Pipeline([
    ("preprocessor", preprocessor),
    ("classifier", xgb_model)
])

# 5. Fit on full data
print("🔧 Training final pipeline on full dataset...")
final_pipeline.fit(X, y)

# 6. Serialize pipeline
joblib.dump(final_pipeline, "deployment/xgb_pipeline_v1.joblib")
print("✅ Pipeline saved to deployment/xgb_pipeline_v1.joblib")
