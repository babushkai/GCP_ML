from babushka import models
from google.cloud import aiplatform

def test_is_model():
    assert(models.load_automl() == aiplatform.Models)

def test_initialize_model():
    assert(models.initialize_model() == True)
