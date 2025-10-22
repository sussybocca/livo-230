import os

UPLOAD_FOLDER = "projects"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def handle_upload(app_file, req_file):
    project_name = app_file.filename.replace(".py", "")
    project_path = os.path.join(UPLOAD_FOLDER, project_name)
    os.makedirs(project_path, exist_ok=True)

    app_path = os.path.join(project_path, "app.py")
    req_path = os.path.join(project_path, "requirements.txt")

    with open(app_path, "wb") as f:
        f.write(app_file.file.read())
    with open(req_path, "wb") as f:
        f.write(req_file.file.read())

    # Here you could implement auto-fix or auto-run later
    return f"Project '{project_name}' uploaded successfully!"

def generate_from_description(description):
    """
    Very basic example: generates a Flask "Hello World" app if description contains "web".
    """
    if "web" in description.lower():
        app_content = """from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Livo!"
"""
        req_content = "flask"
    else:
        # Default example script
        app_content = "print('Hello from Livo!')"
        req_content = ""

    return app_content, req_content
