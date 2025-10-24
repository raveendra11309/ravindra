# secure_chatbot.py
from cryptography.fernet import Fernet

# Step 1: Generate or load a shared secret key
key = Fernet.generate_key()  # In real apps, share this key securely
fernet = Fernet(key)

print(" Secure ChatBot initialized.")
print(f"Shared key (keep secret!): {key.decode()}")
print("Type 'bye' to end the chat.\n")

# Step 2: Dictionary of chatbot responses
responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! How are you doing?",
    "how are you": "I'm just a bot, but I'm doing great! Thanks for asking.",
    "name": "I'm SecureChatBot, your encrypted Python chatbot!",
    "bye": "Goodbye! Have a secure day!",
    "thanks": "You're welcome!",
    "time": "I don't have a watch, but you can check your device for the time!"
}

# Step 3: Function to get chatbot response
def get_response(message):
    message = message.lower()
    for key in responses:
        if key in message:
            return responses[key]
    return "Sorry, I didn't understand that. Can you repeat?"

# Step 4: Encrypted chat loop
while True:
    # User input
    user_input = input("You: ")

    # Encrypt user message
    encrypted_input = fernet.encrypt(user_input.encode())

    # Decrypt for chatbot to read
    decrypted_message = fernet.decrypt(encrypted_input).decode()

    # Get chatbot response
    reply = get_response(decrypted_message)

    # Encrypt the chatbot response
    encrypted_reply = fernet.encrypt(reply.encode())

    # Decrypt before showing to user
    decrypted_reply = fernet.decrypt(encrypted_reply).decode()

    print(f"ChatBot: {decrypted_reply}")

    if decrypted_message.lower() == "bye":
        break     