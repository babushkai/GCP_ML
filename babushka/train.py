
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


def train():
    model = models.initialize_model(auto=False)
