from babushka import models
from google.cloud import aiplatform

def test_is_model():
    isinstance(models.load_automl(), aiplatform.AutoMLTabularTrainingJob)

def test_initialize_model():
    assert(models.initialize_model() == True)
