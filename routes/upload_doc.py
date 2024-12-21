import os
import uuid
from fastapi import APIRouter, HTTPException, UploadFile, File, Depends, BackgroundTasks
from dependencies import ensure_pdf_file_upload_dep
from services import DocTextExtractor, MarkdownSplitter
from configuration.config import config

router = APIRouter()

PDF_DIR = config["dirs"]["pdf_dir"]  # Move paths to constants or config


@router.post("/upload_doc")
async def upload_doc(
    background_tasks: BackgroundTasks,
    file: UploadFile = Depends(ensure_pdf_file_upload_dep),
):
    try:

        upload_id = str(uuid.uuid4())
        os.makedirs(PDF_DIR, exist_ok=True)
        file_path = os.path.join(PDF_DIR, f"{upload_id}.pdf")

        with open(file_path, "wb") as f:
            while chunk := await file.read(1024 * 1024):
                f.write(chunk)

        background_tasks.add_task(DocTextExtractor.save_doc_markdown, upload_id)
        background_tasks.add_task(MarkdownSplitter.locate_and_split_markdown, upload_id)

        return {"filename": file.filename, "success": True, "upload_id": upload_id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error uploading file: {str(e)}")
