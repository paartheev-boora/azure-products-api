import json
import azure.functions as func
from azure.cosmos import CosmosClient, exceptions
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    product_id = req.route_params.get("id")

    try:
        new_data = req.get_json()
    except:
        return func.HttpResponse("Invalid JSON", status_code=400)

    client = CosmosClient.from_connection_string(os.getenv("COSMOS_CONN_STRING"))
    db = client.get_database_client(os.getenv("COSMOS_DB"))
    container = db.get_container_client(os.getenv("COSMOS_CONTAINER"))

    try:
        existing = container.read_item(item=product_id, partition_key=product_id)
    except exceptions.CosmosResourceNotFoundError:
        return func.HttpResponse("Not Found", status_code=404)

    existing.update(new_data)

    container.replace_item(item=product_id, body=existing)

    return func.HttpResponse(json.dumps(existing), status_code=200, mimetype="application/json")
