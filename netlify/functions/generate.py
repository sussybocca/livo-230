import json

def handler(event, context):
    """
    Receives a description via POST and returns app.py + requirements.txt content.
    """
    body = json.loads(event['body'])
    description = body.get("description", "")

    if "web" in description.lower():
        app_content = """from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Livo on Netlify!"
"""
        req_content = "flask"
    else:
        app_content = "print('Hello from Livo!')"
        req_content = ""

    return {
        "statusCode": 200,
        "body": json.dumps({
            "app_py": app_content,
            "requirements_txt": req_content
        })
    }
