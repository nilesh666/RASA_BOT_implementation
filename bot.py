from langdetect import detect
from rasa.core.agent import Agent
import asyncio
from googletrans import Translator

async def handle_message(message):
    # Load your trained Rasa model
    agent = Agent.load('models/20250310-123025-obtuse-lifer.tar.gz')
    
    # Initialize the translator
    translator = Translator()

    # Detect the language of the input message
    language = detect(message)
    
    # Respond based on the detected language
    response = await agent.handle_text(message)
    english_response = response[0]['text']
    
    # Translate English response to Arabic
    translated_response = translator.translate(english_response, dest='ar').text
    
    # Print both responses
    print("English Response:", english_response)
    print("Arabic Response:", translated_response)

# Example usage
if __name__ == "__main__":
    while True:
        message = input("Enter your message: ")
        if message.lower() == "bye":
            print("Goodbye!")
            break
        asyncio.run(handle_message(message))