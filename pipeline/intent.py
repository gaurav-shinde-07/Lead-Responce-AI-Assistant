import google.generativeai as genai
import json
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-pro")

def classify_intent(message, prompt):
    response = model.generate_content(prompt + message)
    return json.loads(response.text)
