# Context Information
## The data is related with direct marketing campaigns of a Portuguese banking institution. The marketing campaigns were based on phone calls. Often, more than one contact to the same client was required, in order to access if the product (bank term deposit) would be ('yes') or not ('no') subscribed. 
<br>

# 📋 Variables Table

| Variable Name     | Role    | Type        | Demographic     | Description                                                                                                                                     | Units  | Missing Values |
|------------------|---------|-------------|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|--------|----------------|
| age              | Feature | Integer     | Age              |                                                                                                                                                 |        | no             |
| job              | Feature | Categorical | Occupation       | Type of job (categorical: 'admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician', 'unemployed', 'unknown') |        | no             |
| marital          | Feature | Categorical | Marital Status   | Marital status (categorical: 'divorced', 'married', 'single', 'unknown'; note: 'divorced' means divorced or widowed)                           |        | no             |
| education        | Feature | Categorical | Education Level  | Education level (categorical: 'primary', 'secondary', 'tertiary', 'unknown') |        | no             |
| default          | Feature | Binary      |                  | Has credit in default?                                                                                                                          |        | no             |
| balance          | Feature | Integer     |                  | Average yearly balance                                                                                                                          | euros  | no             |
| housing          | Feature | Binary      |                  | Has housing loan?                                                                                                                                |        | no             |
| loan             | Feature | Binary      |                  | Has personal loan?                                                                                                                               |        | no             |
| contact          | Feature | Categorical |                  | Contact communication type (categorical: 'cellular', 'telephone')                                                                               |        | yes            |
| date      | Feature | Integer        |                  | Last contact date of the month                                                                                                                     |        |                |
| month     | Feature | Categorical       |                  | Last contact month                                                                                                            |        | no             |
| duration         | Feature | Integer     |                  | Last contact duration                                                                                                                            | seconds| no             |
| campaign         | Feature | Integer     |                  | Number of contacts performed during this campaign for this client                                                                                |        | no             |
| pdays            | Feature | Integer     |                  | Number of days since the client was last contacted (999 means client was not previously contacted)                                               | days   | no             |
| previous         | Feature | Integer     |                  | Number of contacts performed before this campaign for this client                                                                                |        | no             |
| poutcome         | Feature | Categorical |                  | Outcome of the previous marketing campaign (categorical: 'failure','nonexistent','success')                                                      |        | no             |
| deposit                | Target  | Binary      |                  | Has the client subscribed to a term deposit?                                                                                                     |        | no             |
