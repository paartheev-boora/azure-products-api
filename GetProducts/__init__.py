import json
import azure.functions as func
from azure.cosmos import CosmosClient
import os


def main(req: func.HttpRequest) -> func.HttpResponse:

    client = CosmosClient.from_connection_string(os.getenv("COSMOS_CONN_STRING"))
    db = client.get_database_client(os.getenv("COSMOS_DB"))
    container = db.get_container_client(os.getenv("COSMOS_CONTAINER"))

    items = list(container.read_all_items())

    return func.HttpResponse(
        json.dumps(items, indent=2),
        status_code=200,
        mimetype="application/json"
    )
