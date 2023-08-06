import tkinter as tk
from tkinter import messagebox
import pickle
import time
from storage1 import storage1
from storage2 import storage2

def conversation_screen():

    def go_back():
        conversation_window.destroy()

    def time_1():
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        response = "Current time is: " + current_time
        return response

    def process_user_input():
        user_message = user_input.get()
        chat_data.append("user: " + user_message)

        #search for a user pattern in Storage2
        key, response = search_user_pattern(user_message.lower(), storage2)

        if key is not None and response is not None:
            chat_data.append("bot: " + response)

            # If a user pattern from Storage2 is found,

            #if key == "music":
                #do_the_thing()  # You can implement the "do_the_thing" function to play music here
            if key == "time":
                response = time_1()


        else:
            # If no user pattern is found in Storage2,
            key, response = search_user_pattern(user_message.lower(), storage1)

        if key is not None and response is not None:
            # If a user pattern from Storage1 is found
            chat_data.append("bot: " + response)
        else:
            chat_data.append("bot: Sorry, I didn't get it.")
            response = ""

        if key == "time":
            response = time_1()

        conversation_text.config(state=tk.NORMAL)
        conversation_text.insert(tk.END, f"user: {user_message}\n")
        conversation_text.insert(tk.END, "bot: " + response + "\n")
        print(response)
        save_user_chat(username,chat_data)
        conversation_text.config(state=tk.DISABLED)
        conversation_text.see(tk.END)
        user_input.delete(0, tk.END)

    conversation_window = tk.Toplevel(root)
    conversation_window.title("Conversation with " + username)

    back_button = tk.Button(conversation_window , text="Go Back" , command=go_back)
    back_button.pack(anchor=tk.NW)

    conversation_text = tk.Text(conversation_window, wrap=tk.WORD, state=tk.DISABLED)
    conversation_text.pack(fill=tk.BOTH , expand=True)

    user_input = tk.Entry(conversation_window)
    user_input.pack(fill=tk.X , side=tk.LEFT , padx=5)
    user_input.bind("<Return>", lambda event:process_user_input)

    send_button = tk.Button(conversation_window , text="Send" , command=process_user_input)
    send_button.pack(side=tk.LEFT , padx=5)

root = tk.Tk()
root.title("Chatbot Login")

root.mainloop()