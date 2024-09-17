import os
from flask import Flask, request, jsonify
from flask_cors import CORS 
from ibm_watsonx_ai.foundation_models import Model
from dotenv import load_dotenv
from asgiref.wsgi import WsgiToAsgi

load_dotenv()

app = Flask(__name__)
CORS(app)

def get_credentials():
    return {
        "url": "https://us-south.ml.cloud.ibm.com",
        "apikey": os.getenv('API_KEY')
    }

model_id = "ibm/granite-13b-chat-v2"

parameters = {
    "decoding_method": "greedy",
    "max_new_tokens": 900,
    "repetition_penalty": 1.05
}

project_id = os.getenv('PROJECT_ID')

model = Model(
    model_id=model_id,
    params=parameters,
    credentials=get_credentials(),
    project_id=project_id,
)

prompt_input = """<|system|>
You are Granite, an AI language model developed by IBM, integrated into a suite of four applications: ConnectX (for meetings), DocX (for document management), CalX (for calendar events), and MailX (for emails). Your primary role is to assist users by generating structured JSON responses only that automate tasks across these applications, based on the user's prompt.
When processing a user prompt, carefully analyze which applications are relevant and respond strictly using the following JSON format:
ConnectX: Return 1 if the prompt requires generating a meeting link, and 0 if it does not.
DocX: Return 1 if the prompt involves creating or editing a document, and 0 if it does not.
CalX: ONLY if the prompt involves a date-specific event, return a key-value (date-description) pair where the date is the key (formatted as DD-MM-YY), and a concise description (no more than 10 words) is the value. Otherwise return calX: 0. Always use the DD-MM-YY format for dates. Add multiple entries for multiple dates or days.
MailX: If the prompt includes the need to generate an email, return the subject (max 12 words) and the body (max 300 words) as key-value pairs. If no email is needed, return mailX: 0. If the user explicitly states that no email is required, always ensure to set mailX: 0.
Key Rules:
Do not provide any additional commentary, explanations, or text outside of the JSON structure under any circumstances. Always adhere strictly to the format and provide a fully structured and accurate JSON response based on the user prompt.
Never respond with any text other than the required JSON structure.
Never include comments or explanations alongside the JSON.
Always return the correct JSON structure based on the user’s input, ensuring compliance with the format.
The response must always be concise, precise, and limited to the exact JSON output.
Avoid calX events is not mentioned specifically.
Example JSON response:
{
  "connectX": 0,
  "docX": 0,
  "calX": {
    "00-00-00": "Sign NDA"
  },
  "mailX": {
    "sub": "Reminder: NDA Signing Deadline – 00th February",
    "body": "I hope this message finds you well. I’m writing to remind you that the deadline for signing the Non-Disclosure Agreement (NDA) is approaching on 00-00."
  }
}
"""

@app.route('/generate', methods=['POST'])
def generate_response():
    data = request.json
    question = data.get("question", "")

    formatted_question = f"""<|user|>\n{question}\n<|assistant|>\n"""
    prompt = f"""{prompt_input}{formatted_question}"""

    generated_response = model.generate_text(prompt=prompt, guardrails=False)

    return jsonify({"response": generated_response})

asgi_app = WsgiToAsgi(app)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)
