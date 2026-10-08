import os

from dotenv import load_dotenv
from huggingface_hub import InferenceClient


load_dotenv()

HF_TOKEN = os.getenv("HF_TOKEN")

MODEL_NAME = "openai/gpt-oss-120b"


def get_llm():

    if not HF_TOKEN:
        raise ValueError(
            "HF_TOKEN is missing. Please add your Hugging Face token in .env"
        )

    client = InferenceClient(
        api_key=HF_TOKEN
    )

    return client


def generate_response(client, prompt, temperature=0.7, max_tokens=1000):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=temperature,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content
