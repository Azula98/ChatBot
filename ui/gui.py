import tkinter as tk
from nlp.chatbot import get_response

def send_message():
    message = user_input.get()
    chat_history.insert(tk.END, "You: " + message + "\n")
    response = get_response(message)
    chat_history.insert(tk.END, "Bot: " + str(response) + "\n")
    user_input.delete(0, tk.END)

def run_gui():
    global user_input, chat_history

    root = tk.Tk()
    root.title("ChatBot GUI")

    chat_frame = tk.Frame(root)
    scrollbar = tk.Scrollbar(chat_frame)
    chat_history = tk.Listbox(chat_frame, yscrollcommand=scrollbar.set, width=50, height=20)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    chat_history.pack(side=tk.LEFT, fill=tk.BOTH)
    chat_history.pack()
    chat_frame.pack()

    user_input = tk.Entry(root, width=50)
    user_input.pack()
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    root.mainloop()
