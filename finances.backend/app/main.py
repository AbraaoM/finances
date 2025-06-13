from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.controllers.root_controller import router as root_router

app = FastAPI(
    title="Finances AI API",
    description="Backend API for Finances AI System",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(root_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)