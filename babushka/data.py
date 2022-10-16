import itertools
import json
import re
from argparse import Namespace
from collections import Counter
from pathlib import Path
from typing import List, Sequence, Tuple

import numpy as np
import pandas as pd
from nltk.stem import PorterStemmer
from skmultilearn.model_selection import IterativeStratification
from google.cloud import aiplatform

def load_data(project: str = None, 
            location: str = "us-central1",
            display_name: str = None,
            bq_source: str = None):
    """Load data from the source

    Args:
        project (str, optional): PROJECT_ID`. Defaults to None.
        location (str, optional): location where data is. Defaults to "us-central1".
        display_name (str, optional): display name of dataset. Defaults to None.
        bq_source (str, optional): bigquery source ex: "bq://project.dataset.table". Defaults to None.
    """
    aiplatform.init(project=project, location=location)

    dataset = aiplatform.TabularDataset.create(
        display_name=display_name,
        bq_source=bq_source,
    )

    dataset.wait()

    print(f'\tDataset: "{dataset.display_name}"')
    print(f'\tname: "{dataset.resource_name}"')

    return dataset

def filter_name():
    pass

def prepare():
    pass

def preprocess():
    pass

class Sample:
    pass

class Sample2:
    pass