from fastapi import FastAPI, UploadFile, File, Form
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from builder import handle_upload, generate_from_description

app = FastAPI()

# Allow all origins for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_files(app_file: UploadFile = File(...), req_file: UploadFile = File(...)):
    try:
        result = handle_upload(app_file, req_file)
        return JSONResponse({"status": "success", "message": result})
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)})

@app.post("/generate")
async def generate(description: str = Form(...)):
    try:
        app_content, req_content = generate_from_description(description)
        return JSONResponse({
            "status": "success",
            "app_py": app_content,
            "requirements_txt": req_content
        })
    except Exception as e:
        return JSONResponse({"status": "error", "message": str(e)})
