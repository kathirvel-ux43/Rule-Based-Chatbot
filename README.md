# Rule-Based-Chatbot

# Advanced Python Chatbot with Multiple Features

A sophisticated rule-based chatbot built in Python that can handle conversations, perform calculations, play games, tell jokes, and provide time/date information.

## 🚀 Features

- 💬 Chat with the bot
- 🧮 Do calculations
- 🎮 Play games
- ⏰ Check time and date
- 😄 Tell jokes

## How to Run
```bash
python chatbot.py
```
Overall Architecture
```
chatbot.py
├── MAIN CHATBOT FUNCTION
├── HELPER FUNCTIONS
├── GAME FUNCTIONS
└── UTILITY FUNCTIONS
```
## 📋 Requirements

- Python 3.x
- No external dependencies - uses only built-in modules

## 🛠️ Installation

1. **Clone the repository**:
```bash
git clone https://github.com/your-username/Rule-Based-Chatbot.git
cd Rule-Based-Chatbot
```

2.Run the chatbot:
```bash
python chatbot.py
```
Starting the Chatbot
```
========================================
WELCOME TO CHATBOT
========================================
I can help with: Greetings, Time/Date, Calculations, Games
Type 'help' for commands or 'bye' to exit
You:
```

Conversation 
```
You: hello
Bot: Hello! How can I help you?

You: what time is it?
Bot: Current time is 03:45 PM

You: calculate 15 + 27
Bot: Let me calculate that for you!
Bot: 15.0 + 27.0 = 42.0

You: play game
Bot: Which game would you like to play?
1. Guessing Game
2. Rock Paper Scissors
```
Guessing Game:
```
play_game()
    │
    ├── guessing_game()
    │   ├── Number generation
    │   ├── Guess validation
    │   ├── Hint system
    │   └── Attempt tracking
    │
    └── rock_paper_scissors()
        ├── Input validation loop
        ├── Random choice generation
        └── Win condition checking
```

--- NUMBER GUESSING GAME ---
```
I'm thinking of a number between 1 and 20
Guess the number (1/5): 10
Too low! Try higher.
Guess the number (2/5): 15
Correct! You guessed it in 2 attempts!
```
Rock Paper Scissors:
```
--- ROCK PAPER SCISSORS ---
Enter your choice (rock/paper/scissors): rock
Bot chose: scissors
You chose: rock
You win!
```
##Available Commands
###Basic Interaction
```
hello, hi - Greet the bot
how are you - Check bot status
bye - Exit
```

###Information
```
time - Current time
date, today - Current date
what can you do - Bot capabilities
who are you - Bot introduction
help - Command list
```

###Functions
```
calculate [expression] - Math calculations
add/subtract/multiply/divide - Specific math operations
game, play - Start games menu
guessing game - Start number guessing
rock/paper/scissors - Start RPS game
joke - Tell a random joke
weather - Get weather prediction
```
###Data Flow
```
User Input → Input Processing → Command Recognition → Function Call → Output
     ↓
   (text)       (lowercase, strip)   (if-elif chain)   (specific function)  (print response)
###Response Handling Structure
```

## Priority-based command matching:
1. Exit commands
2. Empty input
3. Help
4. Greetings
5. Time/Date
6. Calculations
7. Games
8. Jokes/Weather
9. Default responses
Module Dependencies
```
import random      # Games, random responses
import datetime   # Time/date functions
```
###Error Handling
Empty input: Prompt user to type something
Invalid math: "Sorry, I didn't understand that calculation"
Invalid game input: Retry prompts
Division by zero: Specific error message


