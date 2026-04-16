from fastapi import FastAPI

from app.api.routes import router

app = FastAPI(title="Project Analyst AI")

app.include_router(router)