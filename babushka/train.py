
import itertools
import json
from argparse import Namespace
from pathlib import Path
from typing import Dict, Tuple

import numpy as np
import pandas as pd
import optuna
from numpyencoder import NumpyEncoder
from sklearn.metrics import precision_recall_curve

from babushka import data, models, utils


def train(dataset: str= None, target_column: str = None):
    job = models.initialize_model()
    model = job.run(
        dataset=dataset,
        budget_milli_node_hours=8000,
        model_display_name="automl",
        disable_early_stopping=False,
        sync=True,
        target_column = target_column
    )
    model.wait()
