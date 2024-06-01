import nltk
from nltk.chat.util import Chat, reflections
import tkinter as tk
from tkinter import scrolledtext, END

# Pairs is a list of patterns and responses.
pairs = [
    [
        r"(.*)my name is (.*)",
        ["Hello %2, How are you today?",]
    ],
    [
        r"(.*)help(.*)",
        ["I can help you.",]
    ],
    [
        r"(.*) your name ?",
        ["My name is AIbot, but you can just call me robot and I'm a chatbot.",]
    ],
    [
        r"how are you (.*) ?",
        ["I'm doing very well.", "I am great!"]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "It's OK, never mind that.",]
    ],
    [
        r"i'm (.*) (good|well|okay|ok)",
        ["Nice to hear that.", "Alright, great!"]
    ],
    [
        r"(hi|hey|hello|hola|holla)(.*)",
        ["Hello.", "Hey there.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse.",]
    ],
    [
        r"(.*)created(.*)",
        ["MD ADIL created me using Python's NLTK library.", "Top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['New Delhi, India.',]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain in the past 4 days here in %2.", "In %2, there is a 50% chance of rain.",]
    ],
    [
        r"how (.*) health (.*)",
        ["Health is very important, but I am a computer, so I don't need to worry about my health.",]
    ],
    [
        r"(.*)(sports|game|sport)(.*)",
        ["I'm a very big fan of Cricket.",]
    ],
    [
        r"who (.*) (Cricketer|Batsman) ?",
        ["Virat Kohli.",]
    ],
    [
        r"quit",
        ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]
    ],
    [
        r"(.*)",
        ["That is nice to hear."]
    ],
]

# Reflections is a dictionary of input and corresponding outputs.
reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

# Create a chatbot instance with pairs and reflections
chatbot = Chat(pairs, reflections)

# Function to handle sending messages
def send_message(event=None):
    user_input = user_entry.get()
    if user_input.strip():
        chat_window.config(state=tk.NORMAL)
        chat_window.insert(tk.END, "You: " + user_input + "\n", "user")
        response = chatbot.respond(user_input)
        chat_window.insert(tk.END, "Chatbot: " + response + "\n\n", "bot")
        chat_window.config(state=tk.DISABLED)
        chat_window.yview(END)
        user_entry.delete(0, tk.END)

# Function to handle the GUI
def run_gui():
    global user_entry, chat_window

    # Initialize the main window
    root = tk.Tk()
    root.title("Chatbot")

    # Create a frame for the chat window
    chat_frame = tk.Frame(root, bd=1, bg="lightgray", width=600, height=400)
    chat_frame.pack(padx=10, pady=10)

    # Create a chat window
    chat_window = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, state=tk.DISABLED, width=80, height=20, bg="white", fg="black")
    chat_window.pack(padx=10, pady=10)

    # Configure tag styles
    chat_window.tag_config("user", foreground="blue")
    chat_window.tag_config("bot", foreground="green")

    # Create an entry box for user input
    user_entry = tk.Entry(root, width=80, bg="white", fg="black", bd=1)
    user_entry.pack(padx=10, pady=10)
    user_entry.bind("<Return>", send_message)

    # Create a send button
    send_button = tk.Button(root, text="Send", width=10, bg="lightblue", command=send_message)
    send_button.pack(pady=10)

    # Run the main event loop
    root.mainloop()

# Run the GUI
run_gui()
