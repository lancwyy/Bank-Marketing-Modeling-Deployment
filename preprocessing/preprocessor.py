# preprocessing/preprocessor.py

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, FunctionTransformer, OrdinalEncoder
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd

def cyclic_encode(df, col, max_val):
    """
    Applies cyclic encoding to a column.
    Returns a DataFrame with two new columns: col_sin and col_cos
    """
    sin_col = np.sin(2 * np.pi * df[col] / max_val)
    cos_col = np.cos(2 * np.pi * df[col] / max_val)
    return pd.DataFrame({f"{col}_sin": sin_col, f"{col}_cos": cos_col})

def prepare_data(df):
    """
    Applies raw data preparation:
    - Maps 'yes'/'no' to 1/0 for boolean columns
    - Drops 'pdays' column
    Returns cleaned DataFrame
    """
    bool_cols = ['deposit', 'default', 'housing', 'loan']
    for col in bool_cols:
        if col in df.columns:
            df[col] = df[col].map({'yes': 1, 'no': 0})
    
    if 'pdays' in df.columns:
        df = df.drop(columns=['pdays'])
    
    return df

def build_preprocessor():
    """
    Constructs a ColumnTransformer that applies:
    - Cyclic encoding to 'month' and 'day_of_month'
    - OneHotEncoding to selected categorical features
    - Median imputation to numeric features
    Returns:
        sklearn ColumnTransformer object
    """
    # Define feature groups
    categorical_features = ['poutcome', 'contact', 'job', 'marital']
    numeric_features = ['age', 'balance', 'duration', 'campaign', 'previous', 'default', 'housing', 'loan']
    cyclic_features = ['month', 'date']
    ordinal_feature = ['education']
        
    #Cyclic encoding transformer
    def encode_cyclic(X):
        df = pd.DataFrame(X, columns=cyclic_features)
        month_enc = cyclic_encode(df, 'month', 12)
        day_enc = cyclic_encode(df, 'date', 31)
        return pd.concat([month_enc, day_enc], axis=1).values

    cyclic_pipe = Pipeline([
        ('transformer', FunctionTransformer(encode_cyclic, validate=False))
    ])

    # Categorical pipeline
    cat_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
    ])

    # Ordinal pipeline
    education_order = ["unknown", "primary", "secondary", "tertiary"]
    edu_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('ordinal', OrdinalEncoder(categories=[education_order]))
    ])

    # Numeric pipeline
    num_pipe = Pipeline([
        ('imputer', SimpleImputer(strategy='median'))
    ])

    # Combine into ColumnTransformer
    preprocessor = ColumnTransformer([
        # ('cyclic', cyclic_pipe, cyclic_features),
        ('cat', cat_pipe, categorical_features),
        ('ordinal', edu_pipe, ordinal_feature),
        ('num', num_pipe, numeric_features)
    ])

    return preprocessor
