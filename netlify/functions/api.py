import json
import base64
from backend.app import run_generate, run_upload

def handler(event, context):
    try:
        if event["path"].endswith("/generate"):
            body = json.loads(event["body"])
            description = body.get("description", "")
            result = run_generate(description)
            return {"statusCode": 200, "body": json.dumps(result)}

        elif event["path"].endswith("/upload"):
            # Example assumes base64 upload from frontend
            body = json.loads(event["body"])
            app_bytes = base64.b64decode(body["app_py"])
            req_bytes = base64.b64decode(body["requirements_txt"])
            result = run_upload(app_bytes, req_bytes)
            return {"statusCode": 200, "body": json.dumps(result)}

        return {"statusCode": 404, "body": "Invalid endpoint."}

    except Exception as e:
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
