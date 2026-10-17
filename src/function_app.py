import json, os
import azure.functions as func
from logic import make_greeting

app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="health", auth_level=func.AuthLevel.ANONYMOUS)
def health(req: func.HttpRequest) -> func.HttpResponse:
    body = {"status": "ok", "env": os.environ.get("APP_ENV"), "version": os.environ.get("APP_VERSION")}
    return func.HttpResponse(json.dumps(body), mimetype="application/json")

@app.route(route="greet")
def greet(req: func.HttpRequest) -> func.HttpResponse:
    text = make_greeting(req.params.get("name"), os.environ.get("GREETING", "Hello"))
    return func.HttpResponse(text)