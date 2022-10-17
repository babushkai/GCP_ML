from google.cloud import aiplatform


def get_model_evaluation_tabular_classification(
    project: str,
    model_id: str,
    location: str = "us-central1",
    api_endpoint: str = "us-central1-aiplatform.googleapis.com",
):
    """
    To obtain evaluation_id run the following commands where LOCATION
    is the region where the model is stored, PROJECT is the project ID,
    and MODEL_ID is the ID of your model.
    """
    model_client = aiplatform.gapic.ModelServiceClient(
        client_options={
            'api_endpoint':f'{location}-aiplatform.googleapis.com'
            }
        )
    evaluation_id = model_client.list_model_evaluations(parent=f'projects/{project}/locations/{location}/models/{model_id}')

    # The AI Platform services require regional API endpoints.
    client_options = {"api_endpoint": api_endpoint}
    # Initialize client that will be used to create and send requests.
    # This client only needs to be created once, and can be reused for multiple requests.
    client = aiplatform.gapic.ModelServiceClient(client_options=client_options)
    name = client.model_evaluation_path(
        project=project, location=location, model=model_id, evaluation=evaluation_id
    )
    response = client.get_model_evaluation(name=name)

    return response