import math
from argparse import Namespace
from typing import List, Dict
#import google.cloud.aiplatform as aip
import tensorflow as tf
import tensorflow_hub as hub

from google.cloud import aiplatform
project="project-daisuke318420"
location="us-central1"
display_name="AutoML"

def load_model():
    """
    TODO: Build sklearn classification model
    """
    CONCRETE_INPUT = "numpy_inputs"

    ```Image classification Model```

    # Download the pretrained model from Tensorflow Hub

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
