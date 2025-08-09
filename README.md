# Influence OS - AI Personal Branding Agent

This project is a submission for the AI Intern assessment at Influence OS. It's a full-stack application that acts as an autonomous AI agent to research, create, and post LinkedIn content for personal branding.

**Live Demo URL:** [Link to your deployed Streamlit App on Hugging Face Spaces]

## Key Features

* **AI-Powered Idea Generation:** Leverages the Tavily search API and Google Gemini to research current trends and brainstorm relevant content ideas based on the user's professional profile.
* **High-Quality Content Creation:** A specialized writer agent crafts complete, engaging, and well-structured LinkedIn posts from a selected idea, complete with hooks, value-driven content, and relevant hashtags.
* **Interactive UI:** A user-friendly interface built with Streamlit allows for a seamless two-step content creation process.

## Tech Stack & Architecture

* **Backend:** Python, FastAPI
* **Frontend:** Streamlit
* **AI/Orchestration:** LangChain, Google Gemini, Tavily Search API
* **Deployment:** The backend and frontend are containerized and deployed on Hugging Face Spaces.

### Architecture Decisions

* **Agentic Workflow:** The application uses a multi-agent approach. A "Research Agent" first gathers and synthesizes real-time information, whose output is then used by a specialized "Writer Agent" to ensure content is both relevant and well-written.
* **Streamlit for Rapid Prototyping:** Streamlit was chosen for the frontend to enable rapid development and create a functional, clean UI within the project's time constraints.
* **Simulated LinkedIn API:** Due to the time required for official LinkedIn API access approval, the "Post to LinkedIn" functionality is currently simulated. The backend is designed to easily integrate the official API once credentials are available.

## How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [your-repo-url]
    cd influence_os_agent
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