# Main operations with Command line interface (CLI).
# CLI application

import json
import tempfile
import warnings
import inquirer
from argparse import Namespace
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

import pandas as pd
#import tensorflow 
import typer
from feast import FeatureStore
from numpyencoder import NumpyEncoder
from optuna.integration.mlflow import MLflowCallback

from orchestrator import dag1
from babushka import data, models, predict, train, utils, evaluate

# Ignore warning
#warnings.filterwarnings("ignore")

# Typer CLI app
app = typer.Typer()

@app.command()
def ELT_data():
    questions = [inquirer.List("project", message="Which project to be used?",
                choices=['project-daisuke-318402', 'Image', 'Language']),
                inquirer.List("location", message="Which table type to be used?",
                choices =['us-central1', "Classification", "Time Series"])]
    # Extract, Load, Transform
    data = data.load_data(project=questions["project"], 
            location=questions["project"],
            display_name=questions["project"],
            bq_source=questions["project"]))

    print(data.name)

@app.command()
def download_auxiliary_data():
    print("test")

@app.command()
def trigger_orchestrator():
    pass

@app.command()
def compute_feature():
    pass

@app.command()
def trainer(dataset_id: str,):
    """Training the model

    Args:
        dataset_id (str): dataset id where to be obtained in the elt phase
    """
    # Retrieve existing dataset
    from google.cloud import aiplatform
    dataset = aiplatform.TabularDataset(dataset_id)
    train.train(dataset)

@app.command()
def evaluate_model():
    evaluate.get_model_evaluation_tabular_classification()

def save_artifacts():
    questions = [inquirer.List("model_type", message="Which model to be used?",
                choices=['Table', 'Image', 'Language']),
                inquirer.List("table_type", message="Which table type to be used?",
                choices =['Regression', "Classification", "Time Series"])]

    models.save_model(questions["model_type"], questions="table_type")

@app.command()
def load_artifacts():
    questions = [inquirer.List("model_type", message="Which model to be used?",
                choices=['Table', 'Image', 'Language']),
                inquirer.List("table_type", message="Which table type to be used?",
                choices =['Regression', "Classification", "Time Series"])]

    model = models.load_model()