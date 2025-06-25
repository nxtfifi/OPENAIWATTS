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

