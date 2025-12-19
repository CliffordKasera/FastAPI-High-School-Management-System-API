from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import PostCreate, PostUpdate, PostResponse
from app.database import db

router = APIRouter(prefix="/posts", tags=["Posts"])

@router.get("/", response_model=List[dict])
def get_all_posts():
    posts = db.get_all_posts()
    return posts

@router.get("/{post_id}")
def get_single_post(post_id: int):
    post = db.get_post_by_id(post_id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found"
        )
    return post

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_new_post(post: PostCreate):
    post_data = post.model_dump()
    new_post = db.create_post(post_data)
    return {
        "message": "Post created successfully",
        "post": new_post
    }

@router.put("/{post_id}")
def update_existing_post(post_id: int, post: PostUpdate):
    post_data = post.model_dump(exclude_unset=True)
    updated_post = db.update_post(post_id, post_data)
    if not updated_post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found"
        )
    return {
        "message": "Post updated successfully",
        "post": updated_post
    }

@router.delete("/{post_id}", status_code=status.HTTP_200_OK)
def delete_existing_post(post_id: int):
    success = db.delete_post(post_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Post with id {post_id} not found"
        )
    return {"message": "Post deleted successfully"}