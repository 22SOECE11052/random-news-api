from fastapi import FastAPI
from app.routes.news import router

app = FastAPI(title="Random News Generator API")

app.include_router(router)
