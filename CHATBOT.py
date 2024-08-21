import tkinter as tk
from tkinter import scrolledtext, messagebox

# List of questions and responses in English
faq = {
    "Your name?": "I am an AI chatbot here to assist you. What can I help you with today?",
    "Contact?": "You can reach me right here! I'm always available for a chat.",
    "What do you do?": "I help answer questions and provide information. Ask away!",
    "Time?": "I can't check the time, but you can use your device's clock.",
    "Get help?": "Type your question, and I'll do my best to assist you.",
    "Hours?": "I'm available 24/7 for your questions.",
    "Advice?": "Sure! Let me know what you need advice on.",
    "More info?": "Check our website or help center for details.",
    "Privacy policy?": "Your privacy is important. View our policy on our website.",
    "Complaint?": "Please email support@ourwebsite.com for assistance.",
    "Services?": "We offer various services, from answering questions to detailed info.",
    "Data security?": "Your data is secure with us using advanced encryption.",
    "Account help?": "Tell me your issue, and I'll guide you.",
    "Languages?": "I currently support English. Let me know if you need another language."
}

# Function to send a message
def send_message():
    user_input = user_entry.get().strip().capitalize()
    if user_input:
        chat_display.config(state=tk.NORMAL)
        chat_display.insert(tk.END, f"You: {user_input}\n")
        
        # Check if the question is in the FAQ (case-insensitive)
        response = faq.get(user_input, "Sorry, I don't understand the question.")
        
        chat_display.insert(tk.END, f"Bot: {response}\n")
        chat_display.config(state=tk.DISABLED)
        user_entry.delete(0, tk.END)

# Function to delete the last message
def delete_message():
    chat_display.config(state=tk.NORMAL)
    content = chat_display.get("1.0", tk.END).strip().split('\n')
    if len(content) > 2:
        chat_display.delete(f"{len(content)-2}.0", tk.END)
    chat_display.config(state=tk.DISABLED)

# Function to edit the last message (placeholder for now)
def edit_message():
    messagebox.showinfo("Edit", "Editing is not supported in this version.")

# Function to toggle mode (day/night)
def toggle_mode():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.config(bg='black')
        chat_display.config(bg='grey', fg='white')
        user_entry.config(bg='lightgrey', fg='black')
    else:
        root.config(bg='white')
        chat_display.config(bg='white', fg='black')
        user_entry.config(bg='white', fg='black')

# Function to save chat history
def save_history():
    with open('chat_history.txt', 'w') as file:
        file.write(chat_display.get("1.0", tk.END))

# Function to open chat history
def open_history():
    try:
        with open('chat_history.txt', 'r') as file:
            chat_display.config(state=tk.NORMAL)
            chat_display.delete("1.0", tk.END)
            chat_display.insert(tk.END, file.read())
            chat_display.config(state=tk.DISABLED)
    except FileNotFoundError:
        messagebox.showerror("Error", "History not found.")

# Function to share a message (placeholder for now)
def share_message():
    messagebox.showinfo("Share", "Sharing feature not implemented.")

# Creating the main window
root = tk.Tk()
root.title("Chatbot")
root.geometry("600x700")  # Enlarge window size

dark_mode = False

# Text area to display messages
chat_display = scrolledtext.ScrolledText(root, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 12))
chat_display.pack(expand=True, fill=tk.BOTH, padx=10, pady=(10, 0))

# Text entry area for typing messages
user_entry = tk.Entry(root, font=("Arial", 14))  # Increase the input area font size
user_entry.pack(fill=tk.X, padx=10, pady=(0, 10))

# Frame for buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=5)

# Creating buttons with individual colors
buttons = [
    tk.Button(button_frame, text="Send", command=send_message, bg='lightgreen', fg='black'),
    tk.Button(button_frame, text="Delete", command=delete_message, bg='lightcoral', fg='white'),
    tk.Button(button_frame, text="Edit", command=edit_message, bg='lightyellow', fg='black'),
    tk.Button(button_frame, text="Save History", command=save_history, bg='lightblue', fg='black'),
    tk.Button(button_frame, text="Open History", command=open_history, bg='lightpink', fg='black'),
    tk.Button(button_frame, text="Share", command=share_message, bg='lightcyan', fg='black'),
    tk.Button(button_frame, text="Night Mode", command=toggle_mode, bg='lightslategray', fg='white')
]

# Arranging buttons in a grid
for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i%3, padx=5, pady=5, sticky='ew')

# Adjust the width of the columns
button_frame.columnconfigure(0, weight=1)
button_frame.columnconfigure(1, weight=1)
button_frame.columnconfigure(2, weight=1)

# Initialize button styles
toggle_mode()  # Apply initial style based on mode

root.mainloop()
