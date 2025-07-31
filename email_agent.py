from typing import Dict, Any
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langgraph.graph import Graph, START, END
from dotenv import load_dotenv
import os

# Initialize Groq model with LLaMA 3 70B
model = ChatGroq(
    model="llama3-70b-8192",  
    temperature=0.7,
    api_key=os.environ["GROQ_API_KEY"]
)

# Email prompt template
EMAIL_PROMPT = """You are a professional email writer crafting a personalized cold email.

Context:
- Recipient Name: {name}
- Company: {company}
- Industry: {industry}

Write a concise, persuasive, and friendly cold email that:
1. Opens with a personalized greeting
2. Shows understanding of their industry
3. Provides value proposition
4. Ends with a clear call to action
5. Includes a professional signature

Keep the tone professional yet conversational, and the length to 4–5 sentences maximum.
"""

# Compile the prompt
prompt = ChatPromptTemplate.from_template(EMAIL_PROMPT)

def format_prompt(inputs: Dict[str, Any]) -> Dict[str, Any]:
    return {"prompt": prompt.format_messages(**inputs)}

def generate_email(inputs: Dict[str, Any]) -> Dict[str, Any]:
    messages = inputs["prompt"]
    response = model.invoke(messages)
    return {"email": response.content}

def create_email_graph() -> Graph:
    workflow = Graph()
    workflow.add_node("format_prompt", format_prompt)
    workflow.add_node("generate_email", generate_email)
    workflow.add_edge(START, "format_prompt")
    workflow.add_edge("format_prompt", "generate_email")
    workflow.add_edge("generate_email", END)
    return workflow

def generate_personalized_email(name: str, company: str, industry: str) -> str:
    graph = create_email_graph()
    compiled_graph = graph.compile()
    inputs = {
        "name": name,
        "company": company,
        "industry": industry
    }
    result = compiled_graph.invoke(inputs)
    return result["email"]
