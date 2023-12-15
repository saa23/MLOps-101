# API Development
# 1. ML Model Serialization
## 1.1. Serialization and De-serialization
Serialization (saving) is the process of translating a data structure (object) into a format that can be transmitted/ stored in a database or a file.

De-serialization (loading) is the reverse process in which stored objects are loaded from a database or a file.

## 1.2. Pickle
A standard way of serializing objects in python into format of byte stream.

Pickle can be used for any object data type.

Often used to serialize machine learning algorithm and save it to a file.

Example of code snippet of using Pickle:

```
import pickle

# serialize the trained model object
with open ('model.pkl', 'wb') as f:
    pickle.dump(clf, f)

# load the serialized model object from file
with open('model.pkl', 'rb') as f:
    clf = pickle.load(f)
```

## 1.3. Joblib
Part of Scipy ecosystem and provides utilities for pipelining python jobs. Including saving and loading python objects into numerical data format such as numpy arrays.

Joblib only can used for numerical/ scientific computing data format such as numpy arrays, scikit-learn models.

Joblib is faster than pickle for serializing objects since able to use multi-core processors to perfom the operations in parallel.

Example of code snippet of using Joblib:
```
import joblib

# save the model
filename = 'finalized_model.pkl'
joblib.dump(model, filename)

# load the model
filename = 'finalized_model.pkl'
loaded_model = joblib.load(filename)
```


# 2. API & CRUD
API allows an application to communicate/ interact with other appications.

Four API methods most frequently used as below:
- Create
- Read
- Update
- Delete

Some of response code variations:
- 2xx	🡪 successfully done
- 3xx	🡪 redirection of the request
- 4xx	🡪 error from client-side
- 5xx	🡪 error from server-side

## 2.1. Python API Framework - Flask
A lightweight python web application.

It comes with built-in Werkzeug for the WSGI and Jinja2 for web templating.

As the documentation says, Werkzeug only ideal for development environment.  Thus to deploy the API Flask to production environment need to use alternative WSGI such as gunicorn or waitress.

## 2.2. Postman
API development tool that allows developers to easily design, test, and document APIs.

The developers able to send request from Postman UI, and check the response.
