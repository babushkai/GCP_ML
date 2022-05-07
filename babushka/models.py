import math
from argparse import Namespace
from typing import List, Dict

from google.cloud import aiplatform
project="project-daisuke318420"
location="us-central1"
display_name="AutoML"

def load_model():
    """
    TODO: Build sklearn classification model
    """
    pass

def load_automl():
    aiplatform.init(project=project, location=location)
    model = aiplatform.AutoMLTabularTrainingJob(
            display_name=display_name,
            optimization_prediction_type="classification"
            )
    return model

def initialize_model(auto: False):
    if auto:
        model = load_automl()
    else:
        model = load_model()

    return model
