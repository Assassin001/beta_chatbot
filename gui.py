import tkinter as tk
from tkinter import ttk
from tkinter import *
import sys
import json
import random
from function import *

# this is the function called when the button is clicked



from tkinter import *



def send_message():
    user_input = entry.get()
    print(user_input)
    conversation_text.config(state=tk.NORMAL)
    conversation_text.insert(tk.END, "You: " + user_input + "\n")
    conversation_text.config(state=tk.DISABLED)

    def process_message(user_input):

        user_message = user_input

        with open("keyword.json") as file:
            keyword_actions = json.load(file)
        cleaned_input = user_message.replace(" ", "").lower()

        keyword_matched = False

        for keyword, action in keyword_actions.items():
            if keyword in cleaned_input:
                action_function = globals().get(action)
                if action_function:
                    response = action_function()
                else:
                    response = "Sorry, I didn't get it."
                keyword_matched = True
                break

        if not keyword_matched:
            response = fallback_response(user_message)

        return response

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

    res = process_message(user_input)

    if res is not None:
        bot_response = "Bot: " + res + "\n"
    else:
        bot_response = "Bot: Sorry, I didn't get it.\n"

    print(res)
    bot_response = "Bot:" + res + "\n"
    conversation_text.config(state=tk.NORMAL)
    conversation_text.insert(tk.END, bot_response)
    conversation_text.config(state=tk.DISABLED)
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def scroll_text(*args):
    conversation_text.yview(*args)




root = tk.Tk()
root.geometry('1357x351')
menubar = Menu(root)


button1 = Button(text="Do nothing button")

m1 = PanedWindow()
m1.pack(fill = BOTH , expand=1)

input_var = tk.StringVar()

frame_screen1 = tk.Frame(m1, bg="lightgray" , )
m1.add(frame_screen1)

#img = PhotoImage(file= "i.png")
#Button(root, image=img , compound=LEFT).pack(side = TOP)
#img_label = tk.Label(frame_screen1,image=img)
#img_label.pack(side=tk.TOP)



entry_up = tk.Label(frame_screen1, text="Send")
entry_up.pack(fill="x")
entry = tk.Entry(frame_screen1, bd=1, width=80)
entry.pack(side=tk.LEFT)

input_var.trace("w", send_message)

b1 = tk.Button(frame_screen1, text="Send", width=18, command=send_message)
b1.pack(side=tk.LEFT,fill="x")

frame_screen2 = tk.Frame(m1, bg="lightblue")
m1.add(frame_screen2)

conversation_text = tk.Text(frame_screen2, wrap=tk.WORD, state=tk.DISABLED)
conversation_text.pack(fill=tk.BOTH, expand=True)
#user_entry = tk.Entry(frame_screen2, bd=1)
#user_entry.pack(fill=tk.X)

scrollbar_x = tk.Scrollbar(frame_screen2, orient=tk.HORIZONTAL, command=conversation_text.xview)
scrollbar_x.pack(fill=tk.X)

conversation_text.config(xscrollcommand=scrollbar_x.set)

filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Close", command=donothing)
filemenu.add_command(label="Change Responsive", command=donothing)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)



root.config(menu=menubar)
root.mainloop()
