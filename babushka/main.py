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
#from feast import FeatureStore
#from numpyencoder import NumpyEncoder
#from optuna.integration.mlflow import MLflowCallback

#from orchestrator import dag1
from babushka import data, models, predict, train, utils, evaluate

# Ignore warning
#warnings.filterwarnings("ignore")

# Typer CLI app
app = typer.Typer()

@app.command()
def ELT_data():
    questions = [inquirer.Text("project", message="Your GCP Project"),
                inquirer.Text("location", message="Location of your data"),
                inquirer.Text("display_name", message="What is the name of dataset?"),
                inquirer.Text("type", message="What is the type of dataset? [tabular, image, text]"),
                inquirer.Text("source", message="Path to GCS or Bigquery source, ex: gs://files or bq://project.dataset.table")]
    answers = inquirer.prompt(questions)

    # Extract, Load, Transform
    dataset = data.load_data(project=answers["project"],
            location=answers["location"],
            display_name=answers["display_name"],
            type = answers["type"],
            source=answers["source"])

    print(f"Your Dataset ID is: {dataset.name}")

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
def trainer():
    """Training the model

    Args:
        dataset_id (str): dataset id where to be obtained in the elt phase
    """
    # Retrieve existing dataset
    from google.cloud import aiplatform
    dataset = aiplatform.TabularDataset(input("Enter Dataset ID to be trained: ", ))
    target_var=input("Target Column: ", )
    train.train(dataset=dataset, target_column=target_var)

@app.command()
def get_evaluation():
    return evaluate.get_model_evaluation_tabular_classification()

@app.command()
def deploy_model():
    pass

if __name__ == "__main__":
    app()