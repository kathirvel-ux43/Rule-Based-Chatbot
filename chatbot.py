import random
import datetime

def chatbot():
    print("=" * 40)
    print("WELCOME TO CHATBOT")
    print("=" * 40)
    print("I can help with: Greetings, Time/Date, Calculations, Games")
    print("Type 'help' for commands or 'bye' to exit")
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ['bye', 'exit', 'quit', 'goodbye']:
            print("Bot: Goodbye! Thanks for chatting!")
            break
            
        if user_input == "":
            print("Bot: Please type something!")
            continue
            
        elif 'help' in user_input:
            show_help()
        
        elif any(word in user_input for word in ['hello', 'hi', 'hey']):
            greetings = [
                "Hello! How can I help you?",
                "Hi there! What can I do for you?",
                "Hey! Good to see you!",
                "Hello! Ready to chat?"
            ]
            print("Bot: " + random.choice(greetings))
        
        elif 'good morning' in user_input:
            print("Bot: Good morning! Have a nice day!")
        
        elif 'good afternoon' in user_input:
            print("Bot: Good afternoon! How is your day going?")
        
        elif 'good evening' in user_input:
            print("Bot: Good evening! Nice to see you!")
        
        elif 'how are you' in user_input:
            responses = [
                "I'm doing well, thank you!",
                "I'm great! How about you?",
                "I'm good, thanks for asking!",
                "I'm fine! What about you?"
            ]
            print("Bot: " + random.choice(responses))
        
        elif 'time' in user_input:
            current_time = datetime.datetime.now().strftime("%I:%M %p")
            print("Bot: Current time is " + current_time)
        
        elif 'date' in user_input or 'today' in user_input:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            print("Bot: Today is " + current_date)
        
        elif any(word in user_input for word in ['calculate', 'math', 'add', 'subtract', 'multiply', 'divide', 'plus', 'minus']):
            calculate(user_input)
        
        elif any(word in user_input for word in ['game', 'play', 'guess']):
            play_game(user_input)
        
        elif 'weather' in user_input:
            weather_responses = [
                "It's sunny and warm today",
                "Cloudy with chance of rain",
                "Beautiful clear skies",
                "Mild temperature with light breeze"
            ]
            print("Bot: " + random.choice(weather_responses))
        
        elif 'joke' in user_input:
            tell_joke()
        
        elif any(word in user_input for word in ['who are you', 'what are you']):
            print("Bot: I'm a chatbot created with Python using if-else rules.")
        
        elif any(word in user_input for word in ['what can you do', 'capabilities']):
            print("Bot: I can chat, tell time/date, do calculations, play games, tell jokes and more!")
        
        elif any(word in user_input for word in ['thank', 'thanks']):
            print("Bot: You're welcome!")
        
        else:
            default_responses = [
                "That's interesting! Tell me more.",
                "I see. What else can I help with?",
                "Nice! What would you like to know?",
                "Thanks for sharing!",
                "I understand. Feel free to ask me anything."
            ]
            print("Bot: " + random.choice(default_responses))

def show_help():
    print("Bot: Available commands:")
    print("Greetings: hello, hi, good morning/afternoon/evening")
    print("Time/Date: time, date, today")
    print("Calculations: calculate, add, subtract, multiply, divide")
    print("Games: game, play, guessing game, rock paper scissors")
    print("Other: weather, joke, help, bye")

def calculate(user_input):
    print("Bot: Let me calculate that for you!")
    
    try:
        math_expr = user_input
        for word in ['calculate', 'compute', 'what is', 'math', 'add', 'subtract', 'multiply', 'divide']:
            math_expr = math_expr.replace(word, '')
        math_expr = math_expr.strip()
        
        if 'plus' in user_input or 'add' in user_input:
            numbers = get_numbers(user_input)
            if len(numbers) >= 2:
                result = numbers[0] + numbers[1]
                print("Bot: " + str(numbers[0]) + " + " + str(numbers[1]) + " = " + str(result))
                return
        
        elif 'minus' in user_input or 'subtract' in user_input:
            numbers = get_numbers(user_input)
            if len(numbers) >= 2:
                result = numbers[0] - numbers[1]
                print("Bot: " + str(numbers[0]) + " - " + str(numbers[1]) + " = " + str(result))
                return
        
        if '+' in math_expr:
            parts = math_expr.split('+')
            if len(parts) == 2:
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 + num2
                print("Bot: " + str(num1) + " + " + str(num2) + " = " + str(result))
        
        elif '-' in math_expr:
            parts = math_expr.split('-')
            if len(parts) == 2:
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 - num2
                print("Bot: " + str(num1) + " - " + str(num2) + " = " + str(result))
        
        elif '*' in math_expr:
            parts = math_expr.split('*')
            if len(parts) == 2:
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 * num2
                print("Bot: " + str(num1) + " * " + str(num2) + " = " + str(result))
        
        elif 'x' in math_expr:
            parts = math_expr.split('x')
            if len(parts) == 2:
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                result = num1 * num2
                print("Bot: " + str(num1) + " x " + str(num2) + " = " + str(result))
        
        elif '/' in math_expr:
            parts = math_expr.split('/')
            if len(parts) == 2:
                num1 = float(parts[0].strip())
                num2 = float(parts[1].strip())
                if num2 == 0:
                    print("Bot: Error! Cannot divide by zero!")
                else:
                    result = num1 / num2
                    print("Bot: " + str(num1) + " / " + str(num2) + " = " + str(result))
        
        else:
            print("Bot: Please use format like: 5+3 or add 5 and 3")
    
    except:
        print("Bot: Sorry, I didn't understand that calculation.")

def get_numbers(text):
    numbers = []
    for word in text.split():
        try:
            numbers.append(float(word))
        except:
            continue
    return numbers

def play_game(user_input):
    if 'guess' in user_input:
        guessing_game()
    elif any(word in user_input for word in ['rock', 'paper', 'scissor']):
        rock_paper_scissors()
    else:
        print("Bot: Which game would you like to play?")
        print("1. Guessing Game")
        print("2. Rock Paper Scissors")
        choice = input("Enter 1 or 2: ").strip()
        if choice == '1':
            guessing_game()
        elif choice == '2':
            rock_paper_scissors()
        else:
            print("Bot: Maybe next time!")

def guessing_game():
    print("\n--- NUMBER GUESSING GAME ---")
    print("I'm thinking of a number between 1 and 20")
    secret = random.randint(1, 20)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            guess = int(input("Guess the number (" + str(attempts + 1) + "/" + str(max_attempts) + "): "))
            attempts += 1
            
            if guess == secret:
                print("Correct! You guessed it in " + str(attempts) + " attempts!")
                return
            elif guess < secret:
                print("Too low! Try higher.")
            else:
                print("Too high! Try lower.")
                
        except:
            print("Please enter a valid number!")
    
    if attempts == max_attempts:
        print("Game over! The number was " + str(secret))

def rock_paper_scissors():
    print("\n--- ROCK PAPER SCISSORS ---")
    choices = ['rock', 'paper', 'scissors']
    
    while True:
        user_choice = input("Enter your choice (rock/paper/scissors): ").strip().lower()
        if user_choice in choices:
            break
        else:
            print("Invalid choice! Please choose rock, paper, or scissors.")
    
    bot_choice = random.choice(choices)
    
    print("Bot chose: " + bot_choice)
    print("You chose: " + user_choice)
    
    if user_choice == bot_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and bot_choice == 'scissors') or \
         (user_choice == 'paper' and bot_choice == 'rock') or \
         (user_choice == 'scissors' and bot_choice == 'paper'):
        print("You win!")
    else:
        print("I win!")

def tell_joke():
    jokes = [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why did the scarecrow win an award? He was outstanding in his field!",
        "Why don't eggs tell jokes? They'd crack each other up!",
        "What do you call a fake noodle? An impasta!",
        "Why did the math book look so sad? Because it had too many problems!"
    ]
    print("Bot: " + random.choice(jokes))

if __name__ == "__main__":
    chatbot()