import math
from argparse import Namespace
from typing import List, Dict
import tensorflow as tf
import tensorflow_hub as hub

from google.cloud import aiplatform

project="project-daisuke-318402"
location="us-central1"
display_name="AutoML"

def save_model(model_type: str = None, table_type: str=None):
    """
    TODO: Build sklearn classification model
    """
    CONCRETE_INPUT = "numpy_inputs"
    BUCKET_NAME = "[your-bucket-name]"  # @param {type:"string"}
    BUCKET_URI = f"gs://{BUCKET_NAME}"
    MODEL_DIR = BUCKET_URI + "/model"

    #Image classification Model

    # Download the pretrained model from Tensorflow Hub
    if model_type == "table":
        if table_type =="regression":
            pass
        elif table_type=="classification":
            pass
        else:
            return False

    elif model_type == "image":
        tfhub_model = tf.keras.Sequential(
            [hub.KerasLayer("https://tfhub.dev/google/imagenet/resnet_v2_101/classification/5")]
        )

        tfhub_model.build([None, 224, 224, 3])
        print(tfhub_model.summary())

        def _preprocess(bytes_input):
            decoded = tf.io.decode_jpeg(bytes_input, channels = 3)
            decoded = tf.image.conver_image_dtype(decoded, tf.loat32)
            resized = tf.image.resize(decoded, size=(224, 224))
            return resized

        @tf.function(input_signature=[tf.TensorSpec([None], tf.string)])
        def preprocess_fn(bytes_inputs):
            decoded_images = tf.map_fn(_preprocess, bytes_inputs, dtype=tf.loat32, back_prop = False)
            return {CONCRETE_INPUT: decoded_images }
            # User needs to make sure the key matches model's input

        @tf.function(input_signature=[tf.TensorSpec([None], tf.string)])
        def serving_fn(bytes_inputs):
            images = preprocess_fn(bytes_inputs)
            prob = m_call(**images)
            return prob

        m_call = tf.function(tfhub_model.call).get_concrete_function(
            [tf.TensorSpec(shape=[None, 224, 224, 3], dtype = tf.float32, name=CONCRETE_INPUT)]
        )

        tf.saved_model.save(tfhub_model, MODEL_DIR, signatures={"serving_default": serving_fn})


def load_model(model_type = None, table_type=None):

    #Loading process
    loaded = tf.saved_model.load(MODEL_DIR)
    #serving_input = list(loaded.signatures["serving_default"].structured_input_signatures[1].keys())

def load_automl(model_type = None, table_type=None):
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

        return model

    if model_type=="image":
        model = aiplatform.AutoMLImageTrainingJob(
                display_name=display_name,
                prediction_type="classification"
                )
        return model

def initialize_model(auto: str == True):
    if auto:
        model = load_automl()
    else:
        model = load_model()

    return model
