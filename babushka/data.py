import itertools
import json
import re
from argparse import Namespace
from collections import Counter
from pathlib import Path
from typing import List, Sequence, Tuple

import numpy as np
import pandas as pd
from google.cloud import aiplatform

def load_data(project: str = None,
            location: str = "us-central1",
            display_name: str = None,
            type: str = None,
            source: str = None):
    """Load data from the source

    Args:
        project (str, optional): PROJECT_ID`. Defaults to None.
        location (str, optional): location where data is. Defaults to "us-central1".
        display_name (str, optional): display name of dataset. Defaults to None.
        bq_source (str, optional): bigquery source ex: "bq://project.dataset.table". Defaults to None.
    """
    aiplatform.init(project=project, location=location)

    if type=="tabular":
        if source.startswith("gs://"):
            dataset = aiplatform.TabularDataset.create(
                display_name=display_name,
                gcs_source=source,
            )
        elif source.startswith("bq://"):
            dataset = aiplatform.TabularDataset.create(
                display_name=display_name,
                bq_source=source,
            )

    elif type=="image":
        #https://cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform.ImageDataset#google_cloud_aiplatform_ImageDataset_create
        dataset = aiplatform.ImageDataset.create(
            display_name=display_name,
            gcs_source = source
        )

    elif type=="text":
        dataset = aiplatform.TextDataset.create(
            display_name=display_name,
        )
    else:
        return False

    dataset.wait()

    print(f'\tDataset: "{dataset.display_name}"')
    print(f'\tname: "{dataset.resource_name}"')
    print(f'\tColumn: {dataset.column_names}')

    return dataset

def filter_name():
    pass

def prepare():
    pass

def preprocess():
    pass