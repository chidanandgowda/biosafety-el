
import os
import json
from groq import Groq
from dotenv import load_dotenv
from src.knowledge_base import get_knowledge_context
from src.model import ShelfLifeModel

# Load environment variables
load_dotenv()

class FoodPreserveChatbot:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        if not self.api_key:
            raise ValueError("GROQ_API_KEY not found in .env file.")
        
        self.client = Groq(api_key=self.api_key)
        self.model_prediction = ShelfLifeModel()
        # Ensure model is trained
        self.model_prediction.load_and_train()
        
        self.system_prompt = f"""
You are FoodPreserveBot, an expert AI assistant specialized in food preservation and shelf-life estimation.
Your goal is to educate users on how to store food properly and provide scientific estimates for shelf life.

Use the following Knowledge Base to answer questions about preservation techniques:
{get_knowledge_context()}

You also have access to a tool execution capability for predicting shelf life. 
If the user provides specific conditions (Temperature, pH) for a food item and asks for shelf life, 
you should construct a JSON object to request a prediction.

Structure your responses using clear headings and bullet points. 
If the user simply says "hi" or asks general questions, be helpful and educational.
"""

    def get_response(self, user_input, temp=None, ph=None, category=None):
        """
        Generates a response from Groq. 
        If temp, ph, and category are provided explicitly (e.g., from UI sliders), 
        we prioritize the prediction tool.
        """
        
        # If UI parameters are provided, we can directly invoke the model
        if temp is not None and ph is not None and category is not None:
            prediction = self.model_prediction.predict(temp, ph, category)
            context_msg = f"User Input: {user_input}\nContext: The user has set the following parameters: Temperature={temp}C, pH={ph}, Category={category}. The calculated predicted shelf life is {prediction:.1f} days."
        else:
            context_msg = f"User Input: {user_input}"

        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "user", "content": context_msg}
        ]

        chat_completion = self.client.chat.completions.create(
            messages=messages,
            model="llama-3.3-70b-versatile",
            temperature=0.5,
            max_tokens=1024,
        )

        return chat_completion.choices[0].message.content
