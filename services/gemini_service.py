import google.generativeai as genai
from config import GOOGLE_API_KEY, LLM_MODEL

genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel(LLM_MODEL)

def ask_gemini(prompt):
    try:
        return model.generate_content(prompt).text
    except Exception as e:
        return str(e)