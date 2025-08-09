# backend/schemas.py

from pydantic import BaseModel, Field
from typing import List

class UserInput(BaseModel):
    """Defines the data structure for the user's initial input."""
    role: str
    industry: str
    goal: str

class ContentIdeas(BaseModel):
    """Defines the data structure for the list of generated content ideas."""
    ideas: List[str]

class PostRequest(BaseModel):
    """Defines the data structure for requesting a full post from a selected idea."""
    user_input: UserInput
    selected_idea: str
    post_type: str = Field(..., description="Type of post to generate, e.g., 'Text Post', 'Poll', 'Article Outline'")

class GeneratedPost(BaseModel):
    """Defines the data structure for the final generated LinkedIn post."""
    post_text: str