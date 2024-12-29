from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate an English word to Telugu
def translate_to_telugu(word):
    translation = translator.translate(word, src='en', dest='te')
    return translation.text

# Example usage
english_word = "hello"
telugu_word = translate_to_telugu(english_word)
print(f"The Telugu translation of '{english_word}' is: {telugu_word}")
#==4.0.0-rc1