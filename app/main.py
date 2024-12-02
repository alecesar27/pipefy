from fastapi import FastAPI
from routes.routes import router as pipefy_router

app = FastAPI()

# Inclui as rotas do produtor
app.include_router(pipefy_router)