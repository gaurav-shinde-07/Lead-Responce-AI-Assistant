from google import genai
import os
from dotenv import load_dotenv
import json

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def classify_intent(message, prompt):
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=prompt + message
    )
    return json.loads(response.text)
