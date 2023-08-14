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

# remove extraneous stuff from response
def parse_output(response):
    if '```' in response:
        op_lines = []
        lines = str(response).split('\n')
        begun = False

        for line in lines:

            if begun  and '```' not in line:
                op_lines.append(line)

            if '```' in line:
                begun = True

        code_op = '\n'.join(op_lines)
        return code_op
    else:
        return response



# endpoint for generating responses
@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    prompt = data.get('prompt', '')

    completions = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant who writes code. Your responses will contain code and only code, and nothing else. Do not give an introduction or explanation. Do not show any outputs. Give one and only one code block."},
            {"role": "user", "content": "You are a helpful assistant who writes code. Your responses will contain code and only code, and nothing else. Do not give an introduction or explanation. Do not show any outputs. Give one and only one code block."},
            {"role": "user", "content": prompt},
        ]
    )

    response = completions['choices'][0]['message']['content']
    processed = parse_output(response)

    return jsonify({'response': processed})

if __name__ == '__main__':
    app.run(debug=True)
