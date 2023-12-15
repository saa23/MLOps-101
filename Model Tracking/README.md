## 0 - About MLFLow
MLFlow is an open source platform to manage the ML lifecycle, includes following:
- experimentation
- reproducibility
- deployment
- central model registry

MLFLow is focus on Model Development phase of ML Project. Based on model performance monitoring we able to know the right time to re-training model.

Some important terms in MLFlow:
- **ML Experiment**: Process ML model building
- **Experiment run**: Each trial of ML experimentation
- **Run artifact**: Any files associated with ML run
- **Experiment metadata**

### 0.1. Background Why MLOps?
**What is experiment tracking?**<br/>
Keep tracking all relevant information from ML experiments.

**Why need experiment tracking?**<br/>
- Reproducibility
- Organization
- Optimization
All those factors cannot be achieved through spreadsheet data monitoring.

**What benefits by using MLFLow?**<br/>
- Share experiments with other DS
- Collaborate with others to build and deploy model
- Give more visibility of the DS efforts

**What limitations of MLFLow?**<br/>
- Authentication & users
    - The open-source version of MLFlow does not provide any sort authentication
- Data Versioning
    - No built-in solution for data versioning, but there are alternatives for that.
- Model/ Data Monitoring & Alerting
    - Out of scope of MLFlow

## 1 - MLFlow Components
1. MLFlow Tracking
2. MLFlow Projects
3. MLFlow Models
4. MLFlow Registry

### 1.1 - Tracking
API and UI for logging aprameters, code versions, metrics, and output files when running your machine learning code and for later visualizing the results.

Each run in the tracking records following information:
1. Parameters
2. Metrics
3. Metadata
4. Artifacts
5. Models
Also, some additional data such as:
1. Source code
2. Version of the code
3. Start and end time
4. Author

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

## 2. Getting started with MLFlow
Example of code snippet of using MLFlow
```
mlflow ui --backend-store-uri sqlite:///mlflow.db
```
By default accessing: *http://localhost:5000* 


## 3. Model Registry
Model registry: list down models that ready to production.

Later will be use as labelling in CI CD process.

After registered the models and versioning them, we can assign each model into environment *staging, production, or archieved*.

There are three ways to select which models ready to production:
1. Manually selected
2. using MlflowClient (programmatically selected)
3. using filter in MLFlow UI


## 4. MLFLow Case Practices
We provide three scenarios:
1. A single data scientist participating in an ML competition
    - Tracking server: NO
    - Backend store: LOCAL
    - Artifacts store: LOCAL
2. A cross-functional team with one data scientist working on an ML model
    - Tracking server: YES (LOCAL) 🡪 using SQlite DB for backend store
    - Backend store: SQLITE DB
    - Artifacts store: LOCAL
3. Multiple data scientist working on multiple ML models
    - Tracking server: YES (REMOTE SERVER/ EC2)
    - Backend store: Postgresql DB	🡪 backend store RDS
    - Artifacts store: S3 Bucket 	🡪 artifact store 

Configuring MLFlow 
- Backend store
    - Local filesystem
     -SQLAlchemy compatible DB (e.g. SQlite)
- Artifact store 
    - Local filesystem
    - Remote (e.g. S3 bucket)
- Tracking server
    - No tracking server
    - Localhost
    - Remote



## 5. Appendices

### 5.1. ML Workflow
ML Workflow in general:
- raw data
- data preprocessing
- feature engineering
- model development
- model deployment


### 5.2. Script Used
The file `predict.py` is classifier model without MLFlow functionality. While `predict_with_mlflow.py` is using MLFlow functionality.

Here are some functiality used:
- mlflow.start_run $\rightarrow$ indicating the new run starts
- mlflow.log_metric $\rightarrow$ log metrics under the current active run
- mlflow.log_param $\rightarrow$ log paremters under the current active run
- mlflow.sklearn.log_model $\rightarrow$ log an sklearn model under the current active run (since the example script using sklearn model)

By running the script, will generate `mlruns/` folder which hold the logged values, models, etc for each run.


To  access the MLFLow UI, run command `mlflow ui` then in the browser go to `http://127.0.0.1:5000`

### 5.3. Alternatives
Some recommended alternatives of MLFlow are following:
- Neptune
- Comet
- Weigths & Biases
- TensorBoard

## References: 
- https://medium.com/towards-data-science/comprehensive-guide-to-mlflow-b84086b002ae
- https://github.com/Isaac4real/MLflow_Experiment
- https://www.youtube.com/watch?v=x3cxvsUFVZA&list=RDCMUC3q8O3Bh2Le8Rj1-Q-_UUbA&index=10
- [MLOps ZoomCamp 2023 by DataTalksClub](https://github.com/DataTalksClub/mlops-zoomcamp)