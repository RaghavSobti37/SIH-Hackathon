from googletrans import Translator

# Function to translate a given text to the target language
def translate(text, target_language):
    try:
        # Create a Translator object
        translator = Translator()

        # Use the translate method to perform translation
        translated_text = translator.translate(text, dest=target_language)

        # Return the translated text
        return translated_text.text

    except Exception as e:
        # Handle translation errors (e.g., API rate limiting, language not supported)
        return str(e)
