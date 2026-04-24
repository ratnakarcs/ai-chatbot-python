import tkinter as tk
from tkinter import scrolledtext
import random
import datetime

def get_response(user):
    user = user.lower()

    if "hello" in user or "hi" in user:
        return "Hello! 😊"
    elif "time" in user:
        return datetime.datetime.now().strftime("%H:%M:%S")
    elif "ai" in user:
        return "AI means Artificial Intelligence 🤖"
    elif "name" in user:
        return "I am your AI assistant 😄"
    elif "internship" in user:
        return "Internships give real-world experience 🚀"
    elif "python" in user:
        return "Python is a powerful programming language 🐍"
    elif "bye" in user:
        return "Goodbye! 👋"
    else:
        return random.choice([
            "That's interesting!",
            "Tell me more 😄",
            "I didn’t understand that clearly 🤔",
            "Can you explain again?"
        ])

def send_message():
    user_input = entry.get()
    if user_input.strip() == "":
        return

    chat_area.insert(tk.END, "You: " + user_input + "\n")
    chat_area.yview(tk.END)

    bot_response = get_response(user_input)

    chat_area.insert(tk.END, "Bot: " + bot_response + "\n\n")
    chat_area.yview(tk.END)

    entry.delete(0, tk.END)

window = tk.Tk()
window.title("AI Chatbot")
window.geometry("500x600")
window.configure(bg="#1e1e1e")

chat_area = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=("Arial", 12),
    bg="#2b2b2b",
    fg="white"
)
chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

entry = tk.Entry(
    window,
    font=("Arial", 12),
    bg="#333333",
    fg="white",
    insertbackground="white"
)
entry.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.X, expand=True)

send_btn = tk.Button(
    window,
    text="Send",
    command=send_message,
    bg="#4CAF50",
    fg="white"
)
send_btn.pack(side=tk.RIGHT, padx=10, pady=10)

window.mainloop()