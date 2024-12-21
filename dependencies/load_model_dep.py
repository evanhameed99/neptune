from fastapi import Depends, HTTPException, Request
from configuration.config import config
from typing import Any
from models.model_loader import ModelLoader


async def load_model_dep(request: Request) -> Any:
    try:
        request.state.model = ModelLoader(config.get("model_name"))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error initializing Model: {e}")
