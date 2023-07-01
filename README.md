# 🤖 BOT_ED Project

The BOT_ED project is an interactive chatbot system developed using the Flask framework and the ChatterBot library. The chatbot is designed to provide dynamic and relevant responses to user inputs, incorporating features such as content filtering, contextualized prompt generation, and domain-specific knowledge base.

## Features

✨ **ChatBot:** The project utilizes the ChatterBot library to create a ChatBot instance named 'ResponsibleChatbot'. The chatbot is trained using the ChatterBotCorpusTrainer on English conversational data.

🔒 **Content Filtering:** The system includes content filtering to prevent the chatbot from providing information that includes restricted words.

🎯 **Contextualized Prompt Generation:** The chatbot generates contextual prompts based on user inputs. For example, if the user mentions "customer support," the chatbot asks for clarification on whether the assistance required is for billing or technical support.

📚 **Domain-specific Knowledge Base:** The chatbot can provide additional information on domain-specific terms based on a predefined knowledge base.

## Usage

1. Install the required dependencies mentioned in the `requirements.txt` file.
2. Run the `bot.py` script to start the Flask application.
3. Access the chatbot interface through the provided URL.
4. Enter your queries in the chat interface and receive responses from the chatbot.

## Feedback and Adaptability

The project also includes functionality for receiving user feedback and adapting the chatbot's behavior in real-time. User feedback can be provided through the `/feedback` endpoint, allowing for fine-tuning the chatbot's responses based on user preferences.

🤖 Start interacting with the BOT_ED chatbot and experience its intelligent responses!
