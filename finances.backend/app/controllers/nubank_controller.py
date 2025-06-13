from fastapi import APIRouter, UploadFile, File

router = APIRouter(
    prefix="/nubank",
    tags=["nubank"]
)

@router.post("/upload")
async def upload_nubank_file(file: UploadFile = File(...)):
    content = await file.read()
    # Converting bytes to string and printing
    print(content.decode())
    return {"filename": file.filename, "message": "File content printed to console"}