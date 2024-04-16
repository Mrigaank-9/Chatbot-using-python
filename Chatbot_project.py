import tkinter as tk
from tkinter import scrolledtext, messagebox
from datetime import datetime
import requests

class ChatBot:
    def __init__(self, master):
        self.master = master
        master.title("Enhanced Chatbot")

        # Configure the fonts and colors
        self.font = ('Arial', 12)
        self.background_color = '#f0f0f0'
        self.chat_history_color = '#ffffff'
        self.user_input_color = '#e0e0e0'

        self.master.configure(bg=self.background_color)

        self.chat_history = scrolledtext.ScrolledText(master, state='disabled', width=60, height=20,
                                                      font=self.font, bg=self.chat_history_color)
        self.chat_history.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.user_input = tk.Entry(master, width=60, font=self.font, bg=self.user_input_color)
        self.user_input.grid(row=1, column=0, padx=10, pady=10)

        self.send_button = tk.Button(master, text="Send", command=self.send_message, font=self.font,
                                     bg=self.user_input_color)
        self.send_button.grid(row=1, column=1, padx=10, pady=10)

        self.greet()

    def greet(self):
        self.display_message("Bot: Hello! I'm an enhanced chatbot. How can I assist you today?")

    def send_message(self):
        user_message = self.user_input.get().strip()
        if user_message:
            self.display_message("You: " + user_message)
            self.user_input.delete(0, 'end')
            self.respond_to_message(user_message)

    def display_message(self, message):
        self.chat_history.configure(state='normal')
        self.chat_history.insert('end', message + '\n')
        self.chat_history.configure(state='disabled')
        self.chat_history.yview('end')

    def respond_to_message(self, message):
        # Simple responses based on keywords
        if 'hello' in message.lower():
            self.display_message("Bot: Hello there!")
        elif 'how are you' in message.lower():
            self.display_message("Bot: I'm just a bot, but thanks for asking!")
        elif 'bye' in message.lower():
            self.display_message("Bot: Goodbye! Have a great day.")
            self.master.after(2000, self.master.destroy)  # Auto-close after 2 seconds
        elif 'time' in message.lower():
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            self.display_message("Bot: The current time is " + current_time)
        elif 'date' in message.lower():
            now = datetime.now()
            current_date = now.strftime("%d/%m/%Y")
            self.display_message("Bot: Today's date is " + current_date)
        elif 'joke' in message.lower():
            self.tell_joke()
        elif 'fact' in message.lower():
            self.tell_fact()
        elif 'weather' in message.lower():
            self.get_weather(message)
        else:
            self.display_message("Bot: I'm sorry, I didn't understand that.")

    def tell_joke(self):
        # A list of jokes
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call fake spaghetti? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Did you hear about the mathematician who’s afraid of negative numbers? He’ll stop at nothing to avoid them!",
            "I'm reading a book on anti-gravity. It's impossible to put down!",
            "Parallel lines have so much in common. It’s a shame they’ll never meet.",
            "I told my wife she was drawing her eyebrows too high. She looked surprised!",
        ]
        import random
        joke = random.choice(jokes)
        self.display_message("Bot: " + joke)

    def tell_fact(self):
        # A list of interesting facts
        facts = [
            "The Eiffel Tower can be 15 cm taller during the summer due to thermal expansion of the metal.",
            "The shortest war in history was between Zanzibar and England in 1896. Zanzibar surrendered after 38 minutes.",
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible.",
            "Coca-Cola would be green if coloring weren’t added to it.",
            "The unicorn is the national animal of Scotland.",
            "The shortest war in history was between Zanzibar and England in 1896. Zanzibar surrendered after 38 minutes.",
            "Octopuses have three hearts.",
        ]
        import random
        fact = random.choice(facts)
        self.display_message("Bot: Did you know? " + fact)
        
    def get_weather(self, message):
        # Extract the location from the user's message
        location = message.split('weather')[1].strip()
        if location:
            # Replace 'YOUR_API_KEY' with your own OpenWeatherMap API key
            API_KEY = '6f99a92120d6daafdc06de831c3454d6'
            url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={API_KEY}&units=metric'
            response = requests.get(url)
            data = response.json()
            if data['cod'] == 200:
                temperature = data['main']['temp']
                description = data['weather'][0]['description']
                self.display_message(f"Bot: The weather in {location} is {temperature}°C with {description}.")
            else:
                self.display_message("Bot: Sorry, I couldn't fetch the weather information for that location.")
        else:
            self.display_message("Bot: Please specify the location for which you want the weather information.")

def main():
    root = tk.Tk()
    chatbot = ChatBot(root)
    root.mainloop()

if __name__ == "__main__":
    main()
