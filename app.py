from pipeline.mock_llm import mock_intent, mock_extraction, mock_questions, mock_response
import streamlit as st
from dotenv import load_dotenv
import os
from openai import OpenAI

from pipeline.intent import classify_intent
from pipeline.extractor import extract_info
from pipeline.questions import generate_questions
from pipeline.response import generate_response

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.title("AI Lead Response Assistant")

message = st.text_area("Enter Customer Enquiry")

if st.button("Generate Reply"):

    # Load prompts
    with open("prompts/intent_prompt.txt") as f:
        intent_prompt = f.read()

    with open("prompts/extraction_prompt.txt") as f:
        extraction_prompt = f.read()

    with open("prompts/question_prompt.txt") as f:
        question_prompt = f.read()

    with open("prompts/response_prompt.txt") as f:
        response_prompt = f.read()

    # AI Workflow Pipeline
    intent = mock_intent()
    extracted = mock_extraction()
    questions = mock_questions()
    final = mock_response()


    st.subheader("Generated Client Response:")
    st.write(final)
