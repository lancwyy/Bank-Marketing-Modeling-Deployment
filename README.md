# Bank Marketing Dataset - Term Deposit Prediction

## Project Overview
This project analyzes the Bank Marketing dataset to explore customer behavior and predict whether a client will subscribe to a term deposit. This project is the second one of the series and focuses on modeling and deployment. You can find the EDA work here: <a href="https://github.com/lancwyy/Bank-Marketing-EDA.git">https://github.com/lancwyy/Bank-Marketing-EDA.git</a>

## Dataset Description
- **Source:** [Kaggle Bank Marketing Dataset](https://www.kaggle.com/datasets/janiobachmann/bank-marketing-dataset/data)
- **File:** [data/raw/bank.csv](data/raw/bank.csv)
- **Description:** The dataset contains information about direct marketing campaigns (phone calls) of a Portuguese banking institution. Features include client attributes (age, job, marital status, etc.), campaign details, and the target variable (`y`), indicating if the client subscribed to a term deposit.
- For more details, see [data/raw/bank_description.md](data/raw/bank_description.md).

## Folder Structure
- **preprocessing:** Based on EDA result, conducting encodings and drop problematic column.
- **modeling:**
  - **models.py:** List of candidate models for performance evaluation
  - **param_grid.py:** Parameter configuration for each candidate model
  - **run_modeling.py:** Conduct 6 repeatedly stratified 5-fold cross-validation for each candidate model under ROC/AUC and save averaging results. 
  - **deployed_model_v1.py:** Build and seriealize the best-performed model with full dataset.
- **reporting:** Run report_models.py to visualize each model's averaging performance.
- **deployment:** 
  - **requirements.txt:** Necessary lib list for running the model
  - **xgb_pipeline_v1.joblib:** Seriealized pipeline
  - **app.py:** RESTful wrapper of prediction model with FastAPI framework
- **docker:** Docker file for prediction model and API

## How to Run
1. **Option 1: Run as Python Module**
    - `pip install -r requirements.txt`
    - `uvicorn deployment.app:app --reload`

2. **Option 2: Run by Docker**
	- `docker build -t bank-model-api ./deployment`

3. **Test the prediction model**
    - Note: the value of cloumn `month` should be numeric
```
  curl -X POST http://localhost:8000/predict \
  -H "Content-Type: application/json" \
  -d '{
    "age": 42,
    "balance": 1500.75,
    "duration": 320.0,
    "campaign": 2.0,
    "previous": 1.0,
    "date": 15,
    "month": 6,
    "poutcome": "success",
    "contact": "cellular",
    "housing": true,
    "loan": false,
    "default": false,
    "job": "technician",
    "education": "tertiary",
    "marital": "married"
  }'
  ```

## License
- Project License: See [LICENSE](LICENSE)
