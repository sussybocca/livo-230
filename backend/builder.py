import os

UPLOAD_FOLDER = "projects"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def handle_upload(app_bytes, req_bytes):
    project_name = "project"
    project_path = os.path.join(UPLOAD_FOLDER, project_name)
    os.makedirs(project_path, exist_ok=True)

    with open(os.path.join(project_path, "app.py"), "wb") as f:
        f.write(app_bytes)
    with open(os.path.join(project_path, "requirements.txt"), "wb") as f:
        f.write(req_bytes)
    return f"Project '{project_name}' uploaded successfully!"

def generate_from_description(description):
    if "web" in description.lower():
        app_py = """from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Livo!"
"""
        reqs = "flask"
    else:
        app_py = "print('Hello from Livo!')"
        reqs = ""
    return app_py, reqs
