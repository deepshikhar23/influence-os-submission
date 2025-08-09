# frontend/app.py

import streamlit as st
import requests
import json
from datetime import datetime

# --- Page Configuration ---
st.set_page_config(
    page_title="Influence OS - AI Content Agent",
    page_icon="🤖",
    layout="wide"
)

# --- Backend API URL ---
API_URL = "http://127.0.0.1:8000"

# --- Initialize Session State ---
if 'ideas' not in st.session_state:
    st.session_state.ideas = []
if 'final_post' not in st.session_state:
    st.session_state.final_post = ""
if 'scheduled_posts' not in st.session_state:
    st.session_state.scheduled_posts = []

# --- App Header ---
st.title("Influence OS - AI Personal Branding Agent 🤖")
st.markdown("This tool helps you generate high-quality LinkedIn content. Just provide your professional details, choose a format, and let the AI do the work!")

# --- Main Application Columns ---
col1, col2 = st.columns([2, 1.5])

with col1:
    # --- Step 1: Generate Content Ideas ---
    st.header("Step 1: Generate Content Ideas")
    with st.form(key='idea_form'):
        role = st.text_input("Your Role", "Enter your role")
        industry = st.text_input("Your Industry", "Enter your industry")
        goal = st.text_input("Your Goal for the post", "Enter any topic")
        submit_button = st.form_submit_button(label='✨ Generate Ideas')

    if submit_button:
        with st.spinner('Researching and generating ideas...'):
            try:
                payload = {"role": role, "industry": industry, "goal": goal}
                response = requests.post(f"{API_URL}/generate-ideas", json=payload)
                if response.status_code == 200:
                    st.session_state.ideas = response.json().get('ideas', [])
                    st.session_state.user_input = payload
                    st.success("Successfully generated content ideas!")
                else:
                    st.error(f"Error: {response.text}")
            except requests.exceptions.RequestException as e:
                st.error(f"Could not connect to backend: {e}")

    # --- Step 2: Choose Idea and Format ---
    if st.session_state.ideas:
        st.header("Step 2: Create a Post")
        
        post_type = st.selectbox(
            'Choose a post format:',
            ('Text Post', 'Poll', 'Article Outline')
        )

        for idea in st.session_state.ideas:
            if st.button(f"Create '{post_type}' from this idea: {idea}", key=idea):
                with st.spinner(f'Crafting your {post_type}...'):
                    try:
                        post_payload = {
                            "user_input": st.session_state.user_input,
                            "selected_idea": idea,
                            "post_type": post_type
                        }
                        post_response = requests.post(f"{API_URL}/generate-post", json=post_payload)
                        if post_response.status_code == 200:
                            st.session_state.final_post = post_response.json().get('post_text', '')
                            st.success("Your content is ready!")
                        else:
                            st.error(f"Error: {post_response.text}")
                    except requests.exceptions.RequestException as e:
                        st.error(f"Could not connect to backend: {e}")

    # --- Step 3: Display Generated Post ---
    if st.session_state.final_post:
        st.header("Step 3: Your Generated Content")
        st.markdown("---")
        st.code(st.session_state.final_post, language='text')
        
        if st.button("🗓️ Add to Content Calendar"):
            schedule_time = datetime.now().strftime("%Y-%m-%d %H:%M")
            st.session_state.scheduled_posts.append((schedule_time, st.session_state.final_post))
            st.success("Post added to calendar!")
            # Clear the post so we don't accidentally add it again
            st.session_state.final_post = "" 
            st.rerun() # Corrected line


with col2:
    # --- Content Calendar Display ---
    st.header("🗓️ Content Calendar")
    st.markdown("---")
    if not st.session_state.scheduled_posts:
        st.info("Your scheduled posts will appear here.")
    else:
        for i, (time, post) in enumerate(st.session_state.scheduled_posts):
            with st.expander(f"**{time}** - Post {i+1}"):
                st.text(post)