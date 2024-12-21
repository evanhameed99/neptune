from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import router as AppRouter
from utils.logger import Logger

logger = Logger().logger

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
async def root():
    return {"message": f"Neptune v1.0"}


logger.info("Neptune is running...")


app.include_router(AppRouter)
