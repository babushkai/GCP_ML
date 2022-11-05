# Main operations with Command line interface (CLI).
# CLI application

import json
import tempfile
import warnings
import subprocess

import inquirer
from argparse import Namespace
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional

import pandas as pd
import typer
#from feast import FeatureStore
#from numpyencoder import NumpyEncoder
#from optuna.integration.mlflow import MLflowCallback

from config import config
from config.config import logger
from babushka import data, models, predict, train, utils, evaluate

warnings.filterwarnings("ignore")

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
    logger.info(f"Your Dataset ID is: {dataset.name}")

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
    # Get model id as string
    out = subprocess.check_output(['gcloud ai models list --region us-central1'], shell=True)
    id_list = [id_.decode('utf-8')[:19] for id_ in out.splitlines()[1:]]
    # Turn string into id list by decoding and trimming

    questions = [inquirer.Text("project", message="Your GCP Project"),
                inquirer.Text("location", message="Location of your data"),
                inquirer.List("model_id",
                                message="Choose your model ID",
                                choices=id_list)]


    logger.info(subprocess.run(["gcloud ai models list --region us-central1)"]))
    questions.add(inquirer.List("model_id",
                                message="Choose your model ID",
                choices=[id_.decode('utf-8')[:19] for id_ in out.splitlines()[1:]],))

    answers = inquirer.prompt(questions)

    evaluation_id, metrics = evaluate.get_model_evaluation(project=answers["project"],
            location=answers["location"],
            model_id=answers["model_id"])

    logger.info(evaluation_id)
    logger.info(metrics)

    return evaluation_id

@app.command()
def deploy_model():
    pass

if __name__ == "__main__":
    app()