# modeling/models.py

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.neural_network import MLPClassifier

def get_models():
    return {
        "logreg": LogisticRegression(max_iter=1000),
        "rf": RandomForestClassifier(),
        "xgb": XGBClassifier(eval_metric='logloss'),
        "mlp": MLPClassifier(max_iter=500)
    }
