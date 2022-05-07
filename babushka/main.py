# Main operations with Command line interface (CLI).
# CLI application

import json
import tempfile
import warnings
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
def download_auxiliary_data():
    print("test")

@app.command()
def trigger_orchestrator():
    pass

@app.command()
def compute_feature():
    pass

@app.command()
def trainer(display_name: str, bq_source: str):
    """
    Args:
    bq_source = "bq://project.dataset.table_name"
    """
    from google.cloud import aiplatform
    dataset = aiplatform.TabularDataset.create(
        display_name=display_name,
        bq_source = bq_source)
    
    dataset.wait()
    train.train(dataset)

@app.command()
def load_artifacts():
    model = models.load_model()
    pass