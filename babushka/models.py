import math
from argparse import Namespace
from typing import List, Dict
import tensorflow as tf
import tensorflow_hub as hub

from google.cloud import aiplatform

project="project-daisuke-318402"
location="us-central1"
display_name="AutoML"


def load_model(model_type = None, table_type=None):

    #Loading process
    loaded = tf.saved_model.load(MODEL_DIR)
    #serving_input = list(loaded.signatures["serving_default"].structured_input_signatures[1].keys())

def load_automl(model_type: str = "table", table_type: str="regression"):
    aiplatform.init(project=project, location=location)
    if model_type == "table":
        if table_type=="regression":
            model = aiplatform.AutoMLTabularTrainingJob(
                display_name="table regression model",
                optimization_prediction_type="regression"
                )

        elif table_type=="classification":
            model = aiplatform.AutoMLTabularTrainingJob(
                display_name="table classification model",
                optimization_prediction_type="classification"
                )
        elif table_type=="time":
            model = aiplatform.AutoMLForecastingTrainingJob(
                dispaly_name="table time model",
            )
        else:
            return False

    if model_type=="image":
        model = aiplatform.AutoMLImageTrainingJob(
                display_name=display_name,
                prediction_type="classification"
                )
    return model

def initialize_model(auto: str = True):
    if auto:
        model = load_automl()
    else:
        model = load_model()

    return model
