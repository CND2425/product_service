from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(
    title="Product Service",
    description="A microservice using FastAPI for CRUD operations",
    version="1.0.0",
    docs_url='/docs',
    redoc_url='/docs',
    openapi_url='/openapi.json',
    root_path='/api/product',
)

# CORS-Middleware hinzufügen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Routen registrieren
app.include_router(router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)
