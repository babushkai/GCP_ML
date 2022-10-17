from babushka import models

def test_is_model():
    assert(models.load_automl("table", "regression") == True)

def test_initialize_model():
    assert(models.initialize_model() == True)
