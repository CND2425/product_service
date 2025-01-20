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
    allow_origins=["http://localhost:3000", "http://localhost:8080"],  # Erlaube Anfragen von deinem Frontend
    allow_credentials=True,  # Erlaube das Setzen von Cookies
    allow_methods=["*"],  # Erlaube alle HTTP-Methoden (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Erlaube alle Header
)

# Routen registrieren
app.include_router(router)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8001)