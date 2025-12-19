from fastapi import FastAPI
from app.routes import post

app = FastAPI(
    title="Blog Post API",
    description="A simple REST API for managing blog posts",
    version="1.0.0"
)

app.include_router(post.router)

@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Blog Post API",
        "documentation": "/docs",
        "endpoints": {
            "posts": "/posts"
        }
    }

@app.get("/health")
def health_check():
    return {"status": "healthy"}