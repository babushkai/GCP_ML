import math
from argparse import Namespace
from typing import List, Dict
import tensorflow as tf
import tensorflow_hub as hub

from google.cloud import aiplatform

display_name="AutoML"


def load_model(model_type = None, table_type=None):
    #Loading process
    #loaded = tf.saved_model.load(MODEL_DIR)
    #serving_input = list(loaded.signatures["serving_default"].structured_input_signatures[1].keys())

def load_automl(project: str ="project-daisuke-318402",
                model_type: str = "table",
                table_type: str="regression"):
    """Instanciate GCP AutoML

    Args:
        project (str, optional): ProjectID. Defaults to "project-daisuke-318402".
        model_type (str, optional): Model Type in each strategy. Defaults to "table".
        table_type (str, optional): Table type. Defaults to "regression".

    Raises:
        ValueError: Unmet format

    Returns:
        _type_: instance of GCP AutoML object
    """

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
            #https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.AutoMLForecastingTrainingJob
            model = aiplatform.AutoMLForecastingTrainingJob(
                dispaly_name="table time model",
                optimization_objective = "minimize-rmse" #default
            )
        else:
            return False

    elif model_type=="image":
        model = aiplatform.AutoMLImageTrainingJob(
                display_name=display_name,
                prediction_type="classification"
                )
    else:
        raise ValueError("Model type value is incorrect")

    return model


def initialize_model(auto: str = True):
    """Rapper for instantiation of model

    Args:
        auto (str, optional): Whether the model is from automl. Defaults to True.

    Returns:
        object: instance of model
    """
    if auto:
        model = load_automl()
    else:
        model = load_model()

    return model
