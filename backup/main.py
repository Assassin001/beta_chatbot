import tkinter as tk
from tkinter import messagebox
import pickle
import json
import random
from function import time_1



def search_user_pattern(user_input, storage):
    for key, value in storage.items():
        user_patterns = value["user_pattern"]
        for pattern in user_patterns:
            if pattern in user_input:
                return key, value["response"]
    return None, None

def load_user_chat(username):
    try:
        with open(f"{username}.data", "rb") as file:
            return pickle.load(file)
    except FileNotFoundError:
        return []

def save_user_chat(username, chat_data):
    with open(f"{username}.data", "wb") as file:
        pickle.dump(chat_data, file)

def handle_login():
    username = username_entry.get()
    if not username:
        messagebox.showerror("Error", "Please Enter a Username.")
        return

    chat_data = load_user_chat(username)

    if check_username(username):
        messagebox.showinfo("Success", "Welcome Back, " + username + "!")
    else:
        messagebox.showinfo("New User", "Welcome " + username + "!")

    root.withdraw()
    conversation_screen(username, chat_data)
    root.deiconify()

def check_username(username):
    existing_usernames = ["user1", "user2", "user3"]
    return username in existing_usernames



def conversation_screen(username, chat_data):
    def go_back():
        conversation_window.destroy()

    def process_user_input():
        user_message = user_input.get()
        chat_data.append("user: " + user_message)

        # Define keyword actions in keyword.json
        with open("keyword.json") as file:
            keyword_actions = json.load(file)

        cleaned_input = user_message.replace(" ", "").lower()

        for keyword, action in keyword_actions.items():
            if keyword in cleaned_input:
                action_function = globals().get(action)
                if action_function:
                    response = action_function()
                else:
                    response = "Sorry, I didn't get it."
                break
        else:
            response = fallback_response(user_message)

        chat_data.append("bot: " + response)

        # Update the conversation text widget to display the new response
        conversation_text.config(state=tk.NORMAL)
        conversation_text.insert(tk.END, f"user: {user_message}\n")
        conversation_text.insert(tk.END, "bot: " + response + "\n")
        save_user_chat(username, chat_data)
        conversation_text.config(state=tk.DISABLED)
        conversation_text.see(tk.END)
        user_input.delete(0, tk.END)

    def fallback_response(user_message):
        with open('intents.json') as file:
            intents = json.load(file)

        cleaned_input = user_message.replace(" ", "").lower()

        for intent in intents:
            patterns = intent.get("patterns", [])
            responses = intent.get("responses", [])
            for pattern in patterns:
                if pattern in cleaned_input:
                    return random.choice(responses)

        return "Sorry, I don't have an appropriate response for that."

        chat_data.append("bot: " + response)

        # Update the conversation text widget to display the new response
        conversation_text.config(state=tk.NORMAL)
        conversation_text.insert(tk.END, f"user: {user_message}\n")
        conversation_text.insert(tk.END, "bot: " + response + "\n")
        save_user_chat(username, chat_data)
        conversation_text.config(state=tk.DISABLED)
        conversation_text.see(tk.END)
        user_input.delete(0, tk.END)

    conversation_window = tk.Toplevel(root)
    conversation_window.title("Conversation with " + username)

    back_button = tk.Button(conversation_window, text="Go Back", command=go_back)
    back_button.pack(anchor=tk.NW)

    conversation_text = tk.Text(conversation_window, wrap=tk.WORD, state=tk.DISABLED)
    conversation_text.pack(fill=tk.BOTH, expand=True)

    user_input = tk.Entry(conversation_window)
    user_input.pack(fill=tk.X, side=tk.LEFT, padx=5)
    user_input.bind("<Return>", lambda event: process_user_input())

    send_button = tk.Button(conversation_window, text="Send", command=process_user_input)
    send_button.pack(side=tk.LEFT, padx=5)


root = tk.Tk()
root.title("Chatbot Login")

username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

login_button = tk.Button(root, text="Login", command=handle_login)
login_button.pack()

root.mainloop()