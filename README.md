# AIDI 2003-02 Final Project
This project uses an LLM to generate helpful scripts.

# Setup
Copy the `.env.sample` file to `.env`.
```bash
cp .env.sample .env
```

Update the API key in the `.env` file with your OpenAI API Key
```bash
OPEN_AI_API_KEY=<YOUR_OPENAI_API_KEY_HERE>
```

Create a python virtual environment
```bash
python -m venv venv
```

Activate the virtual environment (Linux)
```bash
source venv/bin/activate
```

Activate the virtual environment (Windows)
```bash
.\venv\Scripts\activate
```

Install the requirements
```bash
pip install -r requirements.txt
```

# Run
Run the app (make sure the venv is activated)
```bash
python app.py
```

# Example Prompts
Some example prompts
> How to write Hello World in C++?

> How to make a basic flask script?

> How to make a triangle star pattern in Java?