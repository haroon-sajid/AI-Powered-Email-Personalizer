import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables from a local .env file, if present
load_dotenv()

# Ensure the GROQ_API_KEY is available before importing email_agent
if "GROQ_API_KEY" not in os.environ:
    st.error("Please set GROQ_API_KEY in a .env file or as an environment variable before running the app.")
    st.stop()

# Import after the API key is guaranteed to be set
from email_agent import generate_personalized_email


# Set page config
st.set_page_config(
    page_title="AI Email Personalizer",
    page_icon="✉️",
    layout="centered"
)

# Add custom CSS
st.markdown("""
    <style>
    .stTextInput > label {
        font-size: 18px;
        font-weight: bold;
    }
    .main {
        padding: 2rem;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("✉️ AI Email Personalizer")
st.markdown("Generate personalized cold emails powered by AI")

# Input form
with st.form("email_form"):
    name = st.text_input("Recipient's Name", placeholder="Haroon Sajid")
    company = st.text_input("Company Name", placeholder="Star Hadi")
    industry = st.text_input("Industry", placeholder="Technology")
    
    generate_button = st.form_submit_button("Generate Email", use_container_width=True)

# Generate email when button is clicked
if generate_button:
    if not all([name, company, industry]):
        st.error("Please fill in all fields!")
    else:
        with st.spinner("Generating your personalized email..."):
            try:
                email_text = generate_personalized_email(name, company, industry)
                
                # Store the generated email in session state
                st.session_state.email_text = email_text
                
                # Display success message
                st.success("Email generated successfully!")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

# Display generated email if it exists
if hasattr(st.session_state, 'email_text'):
    st.markdown("### Generated Email")
    
    # Email display area
    st.text_area("", st.session_state.email_text, height=300, key="email_display")
    
    # Buttons row
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📋 Copy to Clipboard", use_container_width=True):
            st.write("Email copied to clipboard!")
            st.toast("Email copied to clipboard! ✨")
    
    with col2:
        if st.button("🔄 Regenerate", use_container_width=True):
            with st.spinner("Regenerating email..."):
                try:
                    new_email = generate_personalized_email(name, company, industry)
                    st.session_state.email_text = new_email
                    st.experimental_rerun()
                except Exception as e:
                    st.error(f"An error occurred: {str(e)}")

# Footer
st.markdown("---")
st.markdown("Created by **Haroon Sajid** using ❤️ LangChain, LangGraph, and OpenAI")