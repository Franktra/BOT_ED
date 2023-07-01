from flask import Flask, render_template, request, jsonify, abort
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.filters import RepetitiveResponseFilter
import re
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

# Create a ChatBot
chatbot = ChatBot(
    'ResponsibleChatbot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    filters=[RepetitiveResponseFilter()],
    read_only=False  # Allow the chatbot to learn from feedback
)

trainer = ChatterBotCorpusTrainer(chatbot)
trainer.train('chatterbot.corpus.english')

restricted_words = ['example1', 'example2']
knowledge_base = {
    "domain_term1": "Explanation and details about domain_term1",
    "domain_term2": "Explanation and details about domain_term2"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-response', methods=['POST'])
def get_response():
    try:
        user_input = request.json.get('user_input')
        response = chatbot.get_response(user_input).text
    
        # Content filtering for ethical guidelines
        if any(word in response for word in restricted_words):
            response = 'Apologies, I cannot provide the information you are looking for.'
    
        # Contextualized Prompt Generation (Example)
        if "customer support" in user_input.lower():
            response += "\n\nWould you like assistance with billing or technical support?"
    
        # Check if user input has domain-specific terms
        for term, explanation in knowledge_base.items():
            if term in user_input:
                response += f'\n\nAdditional information: {explanation}'
    
        return jsonify({'response': response})

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        abort(500, description="Internal Server Error")

@app.route('/feedback', methods=['POST'])
def feedback():
    try:
        user_input = request.json.get('user_input')
        user_feedback = request.json.get('feedback')
    
        # Store the user's feedback for later analysis
        # ...
    
        # Real-time Adaptability (Example): Simplifying language if user found it too technical
        if "too technical" in user_feedback.lower():
            chatbot.logic_adapters[0]['maximum_similarity_threshold'] = 0.75
    
        return jsonify({'status': 'feedback received'})

    except Exception as e:
        logging.error(f"An error occurred: {e}")
        abort(500, description="Internal Server Error")

if __name__ == "__main__":
    app.run()
