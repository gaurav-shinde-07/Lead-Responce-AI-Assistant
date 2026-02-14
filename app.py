import streamlit as st
from dotenv import load_dotenv
import os
from google import genai

from pipeline.intent import classify_intent
from pipeline.extractor import extract_info
from pipeline.questions import generate_questions
from pipeline.response import generate_response

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

st.title("AI Lead Response Assistant")

message = st.text_area("Enter Customer Enquiry")

if st.button("Generate Reply"):

    with open("prompts/intent_prompt.txt") as f:
        intent_prompt = f.read()

    with open("prompts/extraction_prompt.txt") as f:
        extraction_prompt = f.read()

    with open("prompts/question_prompt.txt") as f:
        question_prompt = f.read()

    with open("prompts/response_prompt.txt") as f:
        response_prompt = f.read()

    intent = classify_intent(message, intent_prompt)
    extracted = extract_info(message, extraction_prompt, client)
    questions = generate_questions(extracted, question_prompt, client)
    final = generate_response(extracted, questions, response_prompt, client)

    st.write(final)
