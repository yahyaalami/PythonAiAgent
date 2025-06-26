import os
from openai import OpenAI
from dotenv import load_dotenv

# Load .env
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4o-mini",  # or "gpt-4"
    messages=[
        {"role": "user", "content": "Tell me a joke."}
    ]
)

print(response.choices[0].message.content)
