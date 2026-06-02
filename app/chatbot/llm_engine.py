import ollama
from openai import OpenAI
import os

from chatbot.locality_extractor import LocalityExtractor
from chatbot.data_engine import DataEngine


class LLMEngine:

    def __init__(self):

        self.model_name = "phi3"

        self.extractor = LocalityExtractor()

        self.data_engine = DataEngine()

        self.data_engine.load_data()

    def ask_locality_question(
        self,
        locality,
        question
    ):

        details = self.data_engine.get_locality_details(
            locality
        )

        if details is None:

            return f"No data found for {locality}"

        prompt = f"""
You are a Mumbai Real Estate Expert.

Locality: {locality}

Average Price:
₹{details['average_price']:,.0f}

Investment Score:
{details['average_investment_score']}

Luxury Score:
{details['average_luxury_score']}

Connectivity Score:
{details['average_connectivity_score']}

Number of Properties:
{details['properties']}

Question:

{question}

Provide a detailed investment recommendation.
"""

        response = self.client.chat.completions.create(
            model=self.model_name,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]
    

    def answer_question(self, question):

        locality = self.extractor.extract_locality(
            question
        )

        if locality is None:

            return "Could not identify locality."

        details = self.data_engine.get_locality_details(
            locality
        )

        prompt = f"""
You are a Mumbai Real Estate Expert.

Locality:
{locality}

Average Price:
₹{details['average_price']:,.0f}

Luxury Score:
{details['average_luxury_score']}

Investment Score:
{details['average_investment_score']}

Connectivity Score:
{details['average_connectivity_score']}

Properties:
{details['properties']}

Question:
{question}

Answer in a professional manner.
"""

        response = ollama.chat(
            model=self.model_name,
            messages=[
            {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]