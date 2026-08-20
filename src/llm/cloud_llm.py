import os

from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()


class CloudLLM:

    def __init__(self):

        api_key = os.getenv("OPENROUTER_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENROUTER_API_KEY is not set in .env"
            )

        self.client = OpenAI(
            api_key=api_key,
            base_url="https://openrouter.ai/api/v1"
        )

    def generate(self, prompt):

        response = self.client.chat.completions.create(
            model="openrouter/free",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0
        )

        return response.choices[0].message.content