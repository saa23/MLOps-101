## 0 - About MLFLow
MLFlow is an open source platform to manage the ML lifecycle, includes following:
- experimentation
- reproducibility
- deployment
- central model registry

MLFLow is focus on Model Development phase of ML Project. Based on model performance monitoring we able to know the right time to re-training model.


## 1 - MLFlow Components
1. MLFlow Tracking
2. MLFlow Projects
3. MLFlow Models
4. MLFlow Registry

### 1.1 - Tracking
API and UI for logging aprameters, code versions, metrics, and output files when running your machine learning code and for later visualizing the results.

Each run in the tracking records following information:
1. code version
2. start & end time
3. source
4. parameters
5. metrics
6. artifacts

### 1.2 - Projects
A standard format for packaging reusable data science code.

### 1.3 - Model
A standard format for packaging machine learning models used in a variety of downstream tools. <br/>
The format defines a convention that lets you save a model in different *"flavors"*. <br/>
It allows model to  be saved and loaded as `.sav` or `.pkl`.

It compatible with various cloud based tools, such as:
- Azure
- AWS Sage Maker
- Docker
- Airflow

### 1.4 - Registry
This component aid the management of the MLFlow lifecycle.
It offers a centralized model store,  set of APIs, and UI, to collaboratively manage the full lifecycle of an MLFLow Model.
It provides 
- model lineage:
    - MLFLow experiment
    - MLFLow run
- Model versioning
- stage transitions
- annotations

## Appendix: ML Workflow
ML Workflow in general:
- raw data
- data preprocessing
- feature engineering
- model development
- model deployment


## Script Used
The file `predict.py` is classifier model without MLFlow functionality. While `predict_with_mlflow.py` is using MLFlow functionality.

Here are some functiality used:
- mlflow.start_run $\rightarrow$ indicating the new run starts
- mlflow.log_metric $\rightarrow$ log metrics under the current active run
- mlflow.log_param $\rightarrow$ log paremters under the current active run
- mlflow.sklearn.log_model $\rightarrow$ log an sklearn model under the current active run (since the example script using sklearn model)

By running the script, will generate `mlruns/` folder which hold the logged values, models, etc for each run.


To  access the MLFLow UI, run command `mlflow ui` then in the browser go to `http://127.0.0.1:5000`

## reference: 
- https://medium.com/towards-data-science/comprehensive-guide-to-mlflow-b84086b002ae
- https://github.com/Isaac4real/MLflow_Experiment
- https://www.youtube.com/watch?v=x3cxvsUFVZA&list=RDCMUC3q8O3Bh2Le8Rj1-Q-_UUbA&index=10