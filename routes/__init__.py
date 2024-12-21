from fastapi import APIRouter
from .upload_doc import router as uploadDoc
from .completion import router as completion

routes = [
    (uploadDoc, ""),
    (completion, ""),
]

router = APIRouter()

for route, prefix in routes:
    router.include_router(route, prefix=prefix)
