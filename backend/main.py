# backend/main.py

import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

# Import schemas and agent functions
from .schemas import UserInput, ContentIdeas, PostRequest, GeneratedPost
from .core.research_agent import generate_research_ideas
from .core.writer_agent import generate_linkedin_post

# Load API keys from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Influence OS AI Agent Suite",
    description="API for managing AI agents for content creation.",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows our Streamlit frontend to communicate with this backend.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, restrict this to your frontend's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Status"])
def read_root():
    """A simple endpoint to check if the API is running."""
    return {"status": "API is running"}

@app.post("/generate-ideas", response_model=ContentIdeas, tags=["Content Generation"])
def get_content_ideas(user_input: UserInput):
    """
    Receives user profile info and generates a list of content ideas.
    """
    ideas = generate_research_ideas(user_input)
    return ContentIdeas(ideas=ideas)

@app.post("/generate-post", response_model=GeneratedPost, tags=["Content Generation"])
def get_linkedin_post(request: PostRequest):
    """
    Receives a selected idea and generates a full LinkedIn post.
    """
    post_text = generate_linkedin_post(request.user_input, request.selected_idea, request.post_type)
    return GeneratedPost(post_text=post_text)