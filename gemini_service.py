import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")

print("🤖 Gemini Chatbot (type 'exit' to quit)\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot ended 👋")
        break

    try:
        response = model.generate_content(user_input)
        print("Gemini:", response.text, "\n")
    except Exception as e:
        print("Error:", e)
