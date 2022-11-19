from typing import Dict, List, Tuple
from google.cloud import aiplatform


def get_model_evaluation(
    project: str = "project-daisuke-318402",
    model_id: str = None,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",) ->Tuple[str, Dict]:
    """Retrieve the evaluation of model

    Args:
        project (str, optional): Project ID. Defaults to "project-daisuke-318402".
        model_id (str, optional): Model ID . Defaults to None.
        location (str, optional): Model Lovation. Defaults to "us-central1".
        api_endpoint (str, optional): API endpoint. Defaults to "us-central1-aiplatform.googleapis.com".

    Returns:
        Tuple: string to evaluation path,
                dictionary of metrics
    """
    model_client = aiplatform.gapic.ModelServiceClient(
        client_options={
            'api_endpoint':f'{location}-aiplatform.googleapis.com'
            }
        )
    evaluations = model_client.list_model_evaluations(parent=f'projects/{project}/locations/{location}/models/{model_id}')
    evaluation_id = evaluations.model_evaluations[0].name
    metrics = dict(evaluations.model_evaluations[0].metrics)
    return evaluation_id, metrics

