# Influence OS - AI Personal Branding Agent

This project is a submission for the AI Intern assessment at Influence OS. It's a full-stack application that acts as an autonomous AI agent to research and create high-quality, post-ready LinkedIn content for personal branding.

**Live Demo URL:** [PASTE YOUR HUGGING FACE SPACES LINK HERE]

**GitHub Repository URL:** [PASTE YOUR GITHUB REPO LINK HERE]

## Key Features

* **AI-Powered Idea Generation:** Leverages the Tavily search API and Google Gemini to research current trends and brainstorm relevant content ideas based on the user's professional profile.
* **Multi-Format Content Creation:** A specialized "Writer Agent" crafts various content types, including engaging text posts, polls, and detailed article outlines.
* **Simple Content Scheduling:** Features a content calendar view to help users organize their generated content.
* **Interactive UI:** A user-friendly interface built with Streamlit allows for a seamless, multi-step content creation process.

## Tech Stack & Architecture

* **Backend:** Python, FastAPI
* **Frontend:** Streamlit
* **AI/Orchestration:** LangChain, Google Gemini, Tavily Search API
* **Deployment:** A live demo is deployed on Hugging Face Spaces.

### Architecture Decisions

* **Agentic Workflow:** The application uses a multi-agent approach. A "Research Agent" first gathers and synthesizes real-time information, whose output is then used by a specialized "Writer Agent" to ensure content is both relevant and well-written.
* **Streamlit for Rapid Prototyping:** Streamlit was chosen for the frontend to enable rapid development and create a functional, clean UI that communicates effectively with the FastAPI backend, all within the project's tight timeline.
* **Strategic API Simulation:** The functionality to post directly to LinkedIn is currently simulated. This was a deliberate architectural decision made to accommodate the project's timeline, as obtaining production-level API permissions from LinkedIn requires a multi-day review process. The backend is fully prepared with a dedicated endpoint to integrate the live API, ensuring the application is scalable and ready for production once credentials are secured.

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd [your-repo-folder-name]
    ```
2.  **Create a `.env` file** in the root directory with your API keys:
    ```
    GOOGLE_API_KEY="your_google_api_key"
    TAVILY_API_KEY="your_tavily_api_key"
    ```
3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Run the backend server** in one terminal:
    ```bash
    python -m uvicorn backend.main:app --reload
    ```
5.  **Run the frontend app** in a second terminal:
    ```bash
    streamlit run frontend/app.py
    ```
