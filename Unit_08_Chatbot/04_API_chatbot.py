import os
from dotenv import load_dotenv
import google.generativeai as genai

# get your API key at: "https://aistudio.google.com/app/apikey"
load_dotenv(override=True) 
API_KEY = os.getenv("API_KEY")
print(API_KEY)

# configure genai
genai.configure(api_key=API_KEY)

# set up the model
model = genai.GenerativeModel(model_name="gemini-2.0-flash")

# start a conversation
chat = model.start_chat(history=[])

print("Welcome to the Gemini Chatbot! Type 'quit' or 'exit' to end the conversation.")

while True: 
    try:
        user_input = input("You: ").lower()
        if user_input in ["quit", "exit"]:
            break
        
        response = chat.send_message(user_input)
        print(f"Chatbot: {response.text}")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        break

print("Chatbot: Goodbye!")