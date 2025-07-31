# AI-Powered Email Personalizer

An AI-powered email personalization tool that generates customized cold emails based on recipient information. Built with Streamlit, LangChain, and Groq's LLaMA 3 70B model.

## Features

- Generate personalized cold emails
- Customizable recipient information
- Professional and friendly tone
- Copy to clipboard functionality
- Email regeneration option

## Deployment on Hugging Face Spaces

1. Create a new Space on Hugging Face:
   - Go to https://huggingface.co/spaces
   - Click "Create new Space"
   - Choose "Streamlit" as the SDK
   - Set the Python version to 3.9 or higher

2. Add your Groq API key:
   - Go to your Space's Settings
   - Under "Repository secrets"
   - Add a new secret with name `GROQ_API_KEY`
   - Paste your Groq API key as the value

3. Upload the project files:
   - Use the Hugging Face web interface or Git to upload:
     - app.py
     - email_agent.py
     - requirements.txt
     - README.md

4. The Space will automatically deploy your application

## Local Development

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file with your Groq API key:
   ```
   GROQ_API_KEY=your_api_key_here
   ```
4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter the recipient's name
2. Provide the company name
3. Specify the industry
4. Click "Generate Email"
5. Use the copy button to copy the generated email
6. Click regenerate if you want a different version

## Credits

Created by Haroon Sajid using LangChain, LangGraph, and Groq's LLaMA 3 70B model.



