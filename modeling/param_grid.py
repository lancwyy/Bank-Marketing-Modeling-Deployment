# modeling/param_grid.py

param_grids = {
    "logreg": {
        "classifier__C": [0.01, 0.1, 1.0, 10.0],
        "classifier__penalty": ["l2"],
        "classifier__solver": ["liblinear"]
    },
    "rf": {
        "classifier__n_estimators": [100, 200],
        "classifier__max_depth": [None, 10, 20],
        "classifier__min_samples_split": [2, 5]
    },
    "xgb": {
        "classifier__n_estimators": [100, 200],
        "classifier__max_depth": [3, 6],
        "classifier__learning_rate": [0.01, 0.1]
    },
    "mlp": {
        "classifier__hidden_layer_sizes": [(64,), (64, 32)],
        "classifier__alpha": [0.0001, 0.001]
    }
}
