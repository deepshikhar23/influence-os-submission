# backend/core/writer_agent.py

import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from ..schemas import UserInput

def generate_linkedin_post(user_input: UserInput, selected_idea: str, post_type: str) -> str:
    """
    Generates a LinkedIn post from a selected idea, user profile, and specified post type.
    """
    print(f"Writer Agent: Initializing for post type: {post_type}")

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.7)
    
    # Base prompt shared by all formats
    base_prompt_template = """
    You are an expert-level LinkedIn ghostwriter and personal branding strategist.
    You are writing for a client with the following professional profile:
    - Role: {role}
    - Industry: {industry}
    - Stated Goal: {goal}

    You have been given the following topic to write about:
    - Selected Idea: {selected_idea}
    """

    # --- Dynamic Prompting Based on Post Type ---
    if post_type == "Text Post":
        specific_prompt = base_prompt_template + """
        Your task is to write a complete, engaging, and professional LinkedIn text post.

        **CRITICAL INSTRUCTIONS:**
        1.  **Hook:** Start with a strong, scroll-stopping hook (a question, bold statement, or statistic).
        2.  **Body:** Provide value clearly. Use 2-3 emojis. Use short paragraphs.
        3.  **CTA:** End with a question to encourage comments.
        4.  **Hashtags:** Include 3-5 relevant, specific hashtags.

        **OUTPUT FORMAT:**
        Return ONLY the text of the post. Do not use any headers.
        """
        prompt = ChatPromptTemplate.from_template(specific_prompt)
    
    elif post_type == "Poll":
        specific_prompt = base_prompt_template + """
        Your task is to create an engaging LinkedIn Poll based on the selected idea.

        **CRITICAL INSTRUCTIONS:**
        1.  **Poll Question:** Write a clear and concise question that sparks discussion.
        2.  **Poll Options:** Provide 4 distinct and relevant options for the poll.
        
        **OUTPUT FORMAT:**
        Return ONLY the text, structured exactly like this:
        Poll Question: [Your Question Here]
        Option 1: [Text for Option 1]
        Option 2: [Text for Option 2]
        Option 3: [Text for Option 3]
        Option 4: [Text for Option 4]
        """
        prompt = ChatPromptTemplate.from_template(specific_prompt)

    elif post_type == "Article Outline":
        specific_prompt = base_prompt_template + """
        Your task is to create a well-structured outline for a LinkedIn article.

        **CRITICAL INSTRUCTIONS:**
        1.  **Catchy Title:** Generate a compelling title for the article.
        2.  **Introduction:** Briefly describe the article's hook and main point.
        3.  **Main Body Points:** List 3-5 main sections with brief descriptions of what each will cover.
        4.  **Conclusion:** Summarize the key takeaways and provide a closing thought or question.

        **OUTPUT FORMAT:**
        Return ONLY the text, structured with clear headings (e.g., "Title:", "Introduction:", "Body:", "Conclusion:").
        """
        prompt = ChatPromptTemplate.from_template(specific_prompt)
    
    else:
        return "Error: Invalid post type specified."

    chain = prompt | llm

    print(f"Writer Agent: Invoking with idea: '{selected_idea}'")
    response = chain.invoke({
        "role": user_input.role,
        "industry": user_input.industry,
        "goal": user_input.goal,
        "selected_idea": selected_idea
    })
    
    post_text = str(response.content)
    print(f"Writer Agent: Successfully generated post.")
    
    return post_text