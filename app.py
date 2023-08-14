from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

import openai
import os

# create app
app = Flask(__name__)

# load environment vars
load_dotenv()

# OpenAI API key
api_key = os.environ.get('OPEN_AI_API_KEY')
openai.api_key = api_key

# main page
@app.route('/')
def index():
    return render_template('index.html')

# endpoint for generating responses
@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    prompt = data.get('prompt', '')
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    chatbot_response = response.choices[0].text.strip()

    print(chatbot_response)
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
