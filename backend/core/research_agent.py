# backend/core/research_agent.py

import os
import ast
import json # Import the JSON library
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.prompts import ChatPromptTemplate
from ..schemas import UserInput

def generate_research_ideas(user_input: UserInput) -> list[str]:
    print("Research Agent (Robust): Initializing...")
    search_tool = TavilySearchResults(max_results=4)
    search_query = f"latest trends and topics in {user_input.industry} for a {user_input.role}"
    print(f"Research Agent (Robust): Performing search for: '{search_query}'")
    search_results = search_tool.invoke(search_query)
    
    context = ""
    for result in search_results:
        context += f"URL: {result['url']}\nContent: {result['content']}\n\n"

    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-lite", temperature=0.7)
    
    # Updated prompt to request JSON output
    prompt = ChatPromptTemplate.from_template(
        """
        You are an expert market researcher and content strategist for LinkedIn.
        Based on the following research context, generate 5 engaging and specific LinkedIn post ideas
        for a user with this profile:
        - Role: {role}
        - Industry: {industry}
        - Goal: {goal}

        **Research Context:**
        ---
        {context}
        ---

        The ideas should be tailored to the user's profile and the provided context.
        **Return ONLY a valid JSON array of strings.**
        Example: ["Idea 1", "Idea 2", "Idea 3", "Idea 4", "Idea 5"]
        """
    )

    chain = prompt | llm
    print("Research Agent (Robust): Invoking LLM to generate ideas from context...")
    response = chain.invoke({
        "role": user_input.role,
        "industry": user_input.industry,
        "goal": user_input.goal,
        "context": context
    })

    # Updated parsing logic to use JSON
    output_string = str(response.content)
    print(f"Research Agent (Robust): Raw output received: {output_string}")
    
    try:
        start_index = output_string.find('[')
        end_index = output_string.rfind(']')
        if start_index != -1 and end_index != -1:
            json_string = output_string[start_index : end_index + 1]
            ideas_list = json.loads(json_string) # Use json.loads()
            if isinstance(ideas_list, list):
                print(f"Research Agent (Robust): Successfully parsed ideas: {ideas_list}")
                return ideas_list
    except (ValueError, json.JSONDecodeError) as e:
        print(f"Research Agent (Robust): Failed to parse JSON string. Error: {e}")
        
    return []