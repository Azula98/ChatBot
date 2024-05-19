import nltk

def setup_nltk():
    nltk.download('punkt')
    # Weitere Downloads und Setups können hier hinzugefügt werden

def process_message(message):
    tokens = nltk.word_tokenize(message)
    # Weitere NLP-Verarbeitungen können hier hinzugefügt werden
    return tokens
