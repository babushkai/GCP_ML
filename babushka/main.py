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
from babushka import data, models, predict, train, utils, evaluate, deploy

warnings.filterwarnings("ignore")

# Typer CLI app
app = typer.Typer()

@app.command()
def elt_data():
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
    """Retrieve Evaluation of model

    Returns:
        str: string of evaluation id path
    """

    questions = [inquirer.Text("project", message="Your GCP Project"),
                inquirer.Text("location", message="Location of your data"),
                inquirer.List("model_id",
                                message="Choose your model ID",
                                choices=utils.get_id('gcloud ai models list --region us-central1'))]

    answers = inquirer.prompt(questions)

    evaluation_id, metrics = evaluate.get_model_evaluation(project=answers["project"],
            location=answers["location"],
            model_id=answers["model_id"])

    logger.info(f"Evaluation ID: {evaluation_id}")
    logger.info(f"Performance Metrics: \n {json.dumps(metrics, indent=2)}")

    return evaluation_id

@app.command()
def endpoint():
    questions = [inquirer.Text("project", message="Your GCP Project"),
                inquirer.Text("location", message="Location of your data"),
                inquirer.Text("display_name", message="What is the name of endpoint?"),]

    answers = inquirer.prompt(questions)

    deploy.create_endpoint(answers["project"],
                            answers["display_name"],
                            answers["location"])

@app.command()
def deploy_model():

    questions = [inquirer.Text("project", message="Your GCP Project"),
                inquirer.Text("location", message="Location of your data"),
                inquirer.List("model_id",
                                message="Choose your model ID",
                                choices=utils.get_id('gcloud ai models list --region=us-central1')),
                inquirer.List("endpoint_id",
                                message="Choose your model ID",
                                choices=utils.get_id('gcloud ai endpoints list --region=us-central1'))]
    answers = inquirer.prompt(questions)

    deploy.deploy_model_with_dedicated_resources(
    #TODO
    project=answers["project"],
    location = answers["locaion"], 
    model_name= answers["model_id"],
    machine_type= answers["locaion"],
    endpoint = answers["endpoint_id"],
    deployed_model_display_name= answers["locaion"],
    traffic_percentage= answers["locaion"],
    traffic_split= answers["locaion"])

@app.command()
def download_auxiliary_data():
    print("test")

@app.command()
def trigger_orchestrator():
    pass

@app.command()
def compute_feature():
    pass

if __name__ == "__main__":
    app()