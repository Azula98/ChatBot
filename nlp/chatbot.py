from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Erstelle einen neuen ChatBot
chatbot = ChatBot(
    'Ailisa',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3'
)

def get_response(message):
    return chatbot.get_response(message)

# Erstelle einen Trainer für den ChatBot
trainer = ChatterBotCorpusTrainer(chatbot)

# Trainiere den ChatBot mit dem englischen Corpus-Daten
trainer.train('chatterbot.corpus.english')

exit_conditions = (":q", "quit", "exit")
while True:
    query = input("> ")
    if query in exit_conditions:
        break
    else:
        print(f"{chatbot.get_response(query)}")
