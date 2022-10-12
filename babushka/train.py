
import itertools
import json
from argparse import Namespace
from pathlib import Path
from typing import Dict, Tuple

import numpy as np

import optuna
import pandas as pd
from numpyencoder import NumpyEncoder
from sklearn.metrics import precision_recall_curve
from babushka import data, models, utils


def train(dataset: str):
    job = models.initialize_model(auto=False)
    model = job.run(
        dataset=dataset,
        budget_milli_node_hours=8000,
        model_display_name="automl",
        disable_early_stopping=False,
        sync=True,
    )
    model.wait()
