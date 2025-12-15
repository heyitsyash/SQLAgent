import os
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


gemini_model = ChatGoogleGenerativeAI(model = "gemini-2.5-flash-lite")

# response = model.invoke(input="Who is the pm of India")
# print(response.content)