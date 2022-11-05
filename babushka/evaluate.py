from google.cloud import aiplatform


def get_model_evaluation(
    project: str= "project-daisuke-318402",
    model_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",):
    model_client = aiplatform.gapic.ModelServiceClient(
        client_options={
            'api_endpoint':f'{location}-aiplatform.googleapis.com'
            }
        )
    evaluations = model_client.list_model_evaluations(parent=f'projects/{project}/locations/{location}/models/{model_id}}')
    evaluation_id = evaluations.model_evaluations[0].name
    metrics = dict(evaluations.model_evaluations[0].metrics)
    return evaluation_id, metrics

