from fastapi import APIRouter, HTTPException, Request, Depends
from dependencies import load_model_dep
from fastapi.responses import StreamingResponse
from services.completion_service import CompletionService
from interfaces import CompletionPayload

router = APIRouter()


@router.post("/completion", dependencies=[Depends(load_model_dep)])
async def completion(request: Request, payload: CompletionPayload):
    try:
        session_id, prompt = payload.session_id, payload.prompt

        if not session_id or not prompt:
            raise ValueError("Both session_id and prompt are required.")

        completion_service = CompletionService(
            session_id=str(session_id), model=request.state.model
        )

        return StreamingResponse(
            completion_service.process_completion(prompt),
            media_type="text/event-stream",
        )
    except ValueError as ve:
        raise HTTPException(status_code=422, detail=str(ve))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Internal Server Error: {str(e)}")
