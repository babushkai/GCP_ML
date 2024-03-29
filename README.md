# Babushka

## Workflow [Tips](https://github.com/kwdaisuke/GCP_ML/blob/main/tips.md)


### Pre-requiste

This project will use [**Google Cloud Platform**](https://cloud.google.com/) as the mainframe. Free trial $300 up to 90 days are [offered](https://cloud.google.com/free). Once creating your account, follow the instructions below

 1. Install and initialize the [gcloud CLI](https://cloud.google.com/sdk/docs/install), if you haven't already.
2. Create your credential file ```gcloud auth application-default login```

Refer to the [GCP official document](https://cloud.google.com/docs/authentication/provide-credentials-adc#local-dev
) on local developlment environment

### GCP Framework for End to End ML Deployment

[Project Description](https://github.com/kwdaisuke/GCP_ML/blob/main/description.md)

1. Initiallizing the environment: set up pi
```
python3 -m venv env
source env/bin/activate
python3 -m pip install --upgrade pip setuptools wheel
python3 -m pip install -e ".[test]"
```

We are going to use `babuska` as the entry point of our command

2. Prepare Dataset: Extract, Load, Transform
```
babushka elt-data
```
> **Note: keep your dataset ID here**

3. Train the model
```
babushka trainer
```



## End note

The structure of this repository
```bash
├── AutoMLframework.ipynb
├── Makefile
├── README.md
├── app
│   ├── app.py
│   ├── config.py
│   ├── gunicorn.py
│   └── schema.py
├── babushka
│   ├── data.py
│   ├── evaluate.py
│   ├── main.py
│   ├── models.py
│   ├── predict.py
│   ├── train.py
│   └── utils.py
├── config
│   └── config.py
├── description.md
├── dk.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   ├── entry_points.txt
│   ├── requires.txt
│   └── top_level.txt
├── feature
│   └── feature.py
├── features
│   ├── feature_store.yaml
│   └── features.py
├── orchestrator
│   ├── dag1.py
│   └── workflow.py
├── pyproject.toml
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── app
    │   ├── __init__.py
    │   └── test_app.py
    ├── babushka
    │   ├── __init__.py
    │   ├── test_main.py
    │   ├── test_models.py
    │   ├── test_predict.py
    │   ├── test_train.py
    │   └── test_utils.py
    └── orchestrator
        ├── __init__.py
        └── test_dag1.py
```

## Contributing
We welcome contributions to this project! Please follow these guidelines when contributing:

- Follow the Google Cloud Platform style guide for Python code.
- Write unit tests for any new code you add.
- Document any new features or changes in the README.

## License
This project is licensed under the Apache 2.0 License - see the LICENSE file for details.

## Acknowledgments
Thank you to the Google Cloud team for providing the tools and services used in this project.
