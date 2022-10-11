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
from babushka import data, models, predict, train, utils 

# Ignore warning
#warnings.filterwarnings("ignore")

# Typer CLI app
app = typer.Typer()

@app.command()
def ELT_data():
    questions = [inquirer.List("model_type", message="Which model to be used?",
                choices=['Table', 'Image', 'Language']),
                inquirer.List("table_type", message="Which table type to be used?",
                choices =['Regression', "Classification", "Time Series"])]
    # Extract, Load, Transform
    from google.cloud import aiplatform
    aiplatform.TabularDataset.create(
        display_name=display_name,
        gcs_source=gcs_source

    )
    dataset.wait()
    print(f"Your dataset ID is: {dataset.name}")

    
    

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
    """
    Args:
    bq_source = "bq://project.dataset.table_name"
    """
    
    # Retrieve existing dataset
    from google.cloud import aiplatform
    dataset = aiplatform.TabularDataset.(dataset_id)
    train.train(dataset)


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