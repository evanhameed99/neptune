from fastapi import HTTPException, UploadFile, File, Depends


async def ensure_pdf_file_upload_dep(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only PDF files are allowed for now :)",
        )
    return file
