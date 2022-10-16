# Babushka

GCP Framework for End to End ML Deployment 

[Project Description](https://github.com/kwdaisuke/GCP_ML/blob/main/description.md)

1. Initiallizing the environment: set up pi
```
python3 -m venv env
source env/bin/activate
python -m pip install --upgrade pip setuptools wheel
python -m pip install -e ".[test]"
```

We are going to use `babuska` as the entry point of our command

2. Prepare Dataset: Extract, Load, Transform
```
babushka elt-data
```

3. Train the model
```
babuska trainer
```