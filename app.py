from flask import Flask, request
from flask_cors import CORS
import os
import json
import openai

app = Flask(__name__)
CORS(app, origins="*")

openai.organization = "org-mQhI2HrRBAIiqQb4sqvMmRmk"
openai.Model.list()

@app.route("/")
def index():
    # print(openai.Model.list())
    return "Index"

@app.route("/get-response", methods=['POST'])
def get_response():
    data = json.loads(request.data)
    openai.api_key = data['apiKey']
    messages = data['messages']
    chat_completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    return {
        "role": "assistant",
        "content": chat_completion['choices'][0]['message']['content']
    }