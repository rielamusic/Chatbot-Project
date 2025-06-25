import tkinter as tk
from tkinter import scrolledtext
import cohere # type: ignore

# 🔑 Replace with your actual Cohere API key
API_KEY = "TgbaivHsXofKADQkPnuyezEdUR6T033a3jrxeGMM"

# Initialize Cohere client
co = cohere.Client(API_KEY)
response = co.chat(
    message="Hello!",
    model="command-r",  # ✅ this works with `chat()`, not `generate()`
)
print(response.text)

# 🧠 Chat function
def get_bot_response(user_input):
    try:
        response = co.chat(
            model='command-r',
            message=user_input  # ✅ plain string
        )
        return response.text.strip()
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 💬 Send message from GUI
def send_message():
    user_msg = user_input.get()
    if not user_msg.strip():
        return

    chat_box.insert(tk.END, f"You: {user_msg}\n")
    user_input.delete(0, tk.END)

    chat_box.insert(tk.END, "Bot: Thinking...\n")
    chat_box.update()

    bot_reply = get_bot_response(user_msg)

    chat_box.delete("end-2l", "end-1l")  # remove "Thinking..." line
    chat_box.insert(tk.END, f"Bot: {bot_reply}\n")
    chat_box.see(tk.END)

# 🎨 GUI Setup
root = tk.Tk()
root.title("Nagul's Cohere Chatbot")
root.geometry("500x600")

chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
chat_box.insert(tk.END, "🤖 Welcome to Nagul's Chatbot! Type a message below.\n")

user_input = tk.Entry(root, font=("Arial", 14))
user_input.pack(padx=10, pady=10, fill=tk.X)
user_input.focus()

send_btn = tk.Button(root, text="Send", command=send_message, font=("Arial", 12))
send_btn.pack(pady=(0, 10))

root.bind('<Return>', lambda event: send_message())

root.mainloop()
