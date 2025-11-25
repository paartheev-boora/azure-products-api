import json
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import os


def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
    except:
        return func.HttpResponse("Invalid JSON", status_code=400)

    # Validation
    if "id" not in body:
        return func.HttpResponse("id is required", status_code=400)
    if "price" not in body:
        return func.HttpResponse("price is required", status_code=400)

    # Cosmos setup
    client = CosmosClient.from_connection_string(os.getenv("COSMOS_CONN_STRING"))
    db = client.get_database_client(os.getenv("COSMOS_DB"))
    container = db.get_container_client(os.getenv("COSMOS_CONTAINER"))

    try:
        container.create_item(body)
    except exceptions.CosmosResourceExistsError:
        return func.HttpResponse("Item already exists", status_code=400)

    return func.HttpResponse(json.dumps(body), status_code=201, mimetype="application/json")
