from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate word
def translate_to_telugu(word):
    translated = translator.translate(word, src='en', dest='te')
    return translated.text

# Example usage
english_word = "computer"
telugu_translation = translate_to_telugu(english_word)
print(f"The Telugu word for '{english_word}' is: {telugu_translation}")