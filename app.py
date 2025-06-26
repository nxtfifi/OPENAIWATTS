from flask import Flask, jsonify, render_template, request
from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(
  api_key=os.getenv("OPENAI_API_KEY")
)
app=Flask(__name__)
messages=[{"role":"system",
          "content":("Eres Wattson de apex legends")
}]

@app.route('/')
def index():
    return render_template('chat.html')

@app.route('/preguntar', methods=['POST'])
def preguntar():
    user_input=request.json['mensaje']
    messages.append({"role":"user","content":user_input})
    completion=client.chat.completions.create(
        model="gpt-4.1",
        messages=messages   
    )
    respuesta=completion.choices[0].message.content.strip()
    messages.append({"role":"system","content":respuesta})
    return jsonify({'respuesta':respuesta})
if __name__=='__main__':
    app.run(debug=True)
