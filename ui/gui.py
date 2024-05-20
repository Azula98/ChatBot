import tkinter as tk
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout
from tkinter import ttk
from tkinter import messagebox
from nlp.chatbot import get_response

def run_gui():
    root = tk.Tk()
    root.title("Chatbot")
    root.iconbitmap("./assets/icon.ico")

    chat_log = tk.Text(root, state='disabled')
    chat_log.pack()

    entry_box = tk.Entry(root)
    entry_box.pack()

    def send_message(event=None):
        message = entry_box.get()
        chat_log.configure(state='normal')
        chat_log.insert(tk.END, "You: " + message + "\n")
        respons = get_response(message)
        chat_log.inset(tk.END, "Ailisa: " + str(respons) + "\n")
        chat_log.configure(state='disabled')
        entry_box.delete(0, tk.END)

    entry_box.bind("<Return>", send_message)
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack()

    root.mainloop()
