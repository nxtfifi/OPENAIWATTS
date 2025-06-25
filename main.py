from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()
client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)
messages=[
    {"role": "system", "content":("Eres wattson de apex legends")}
]
while True:
    user_input=input("Tu: ")
    if user_input.lower() in ["salir", "exit", "quit"]:
        print("Wattson: Bonne journée y que todos tus sistemas funcionen a la perfección. ⚡🔋 ¡Hasta la próxima misión, Watts desconectando… pero nunca muy lejos!")
        break
    messages.append({"role": "system", "content": user_input})
    completion=client.chat.completions.create(
        model="gpt-4.1",
        messages=messages
    )
    response=completion.choices[0].message.content
    print(f"Wattson: {response}")
    print("\n")
    messages.append({"role": "assistant", "content": response})
