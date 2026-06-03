import random

def number_game():
    print("\n------Welcome to the number guessing game !------")
    secret_number = random.randint(1, 10)
    guess = int(input("Guess a random number beetween 1, 10 \n"))
    
    if guess == secret_number:
        print("You got it right 🎉")
    else:
        print(f"❌ Better luck next time, the number was {secret_number}")
        
        
def coin_game():
    print("\n------Welcome to the coin flip game------")
    choice = input("Choose heads or tails \n")
    result = random.choice(["Heads", "Tails"])
    
    print(f"It landed on {result}")
    
    if choice == result:
        print("You win 🎉")
    else:
        print("❌ Better luck next time")
        
        
def main_menu():
    while True:
        print("\n-------Welcome to the main menu--------")
        print("Choose a game to play")
        print("1.Number guessing game")
        print("2.Coin flipping game (The heads or tails)")
        print("3. Quit")
        
        choice = int(input("Pick a number of your choice (1, 3)"))
        
        if choice == 1:
            number_game()
        elif choice == 2:
            coin_game()
        elif choice == 3:
            print("Thank you for playing bye 👋")
        else:
            print("Please pick a number from 1,3")
            
        
        play_again = input("\nDo you want to play a diffrent game? (yes/no)").lower()
        
        if play_again in ["no", "n"]:
            print("Thank you for playing bye 👋")
            break
            
            
main_menu()
            
            
            
    
    