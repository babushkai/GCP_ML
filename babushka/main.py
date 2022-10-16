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
                inquirer.Text("bigquery_source", message="Path to the bigquery source, ex: bq://project.dataset.table")]
    answers = inquirer.prompt(questions)

    # Extract, Load, Transform
    dataset = data.load_data(project=answers["project"],
            location=answers["location"],
            display_name=answers["display_name"],
            bq_source=answers["bigquery_source"])

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
def trainer():
    """Training the model

    Args:
        dataset_id (str): dataset id where to be obtained in the elt phase
    """
    # Retrieve existing dataset
    from google.cloud import aiplatform
    dataset = aiplatform.TabularDataset(input("Enter Dataset ID: ", ))
    target_var=input("Target Column: ", )
    train.train(dataset=dataset, target_column=target_var)

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


if __name__ == "__main__":
    app()