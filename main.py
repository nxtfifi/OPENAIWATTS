from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)

completion = client.chat.completions.create(
  model="gpt-4.1",
  store=True,
  messages=[
    {"role": "system", "content": "Eres un buen asistente"}
  ]
)
role=completion.choices[0].message.role
content=completion.choices[0].message.content.strip()

print(f"{role.upper()}: {content}")
