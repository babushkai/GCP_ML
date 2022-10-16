from fastapi import FastAPI, Request
from http import HTTPStatus
from functools import wraps
from typing import Union, Dict, List, Type

from babushka import main

JSON = Union[Dict[str, 'JSON'], List['JSON'], int, str, float, bool, Type[None]]

# Define application
app = FastAPI(
    title="Babushka",
    description="Testing",
    version="0.1",
)

def wrapper(f):
    @wraps(f)
    def wrap(request: Request, *args, **kwargs) -> Dict:
        results = f(request, *args, **kwargs)
        response = {
            "message": results["message"],
            "method": request.method,
            "status-code": results["status-code"],
            "timestamp": datetime.now.isoformat(),
            "url": request.url._url,
        }
        if "data" in results:
            response["data"] = results["data"]
        return response
    return wrap


@app.get("/")
@wrapper
def _index() -> Dict:
    """Health check."""
    response = {
        "message": HTTPStatus.OK.phrase,
        "status-code": HTTPStatus.OK,
        "data": {"This is the correct"},
    }
    return response


def load_artifacts():
    pass


def response():
    # https://stackoverflow.com/questions/308999/what-does-functools-wraps-do
    @wraps(f) 
    def wrap():
        pass
    
    return wrap

#@response
def predict():
    pass

#@response
def _params():
    pass

#@response
def peformance():
    pass