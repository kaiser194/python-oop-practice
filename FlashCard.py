import random

class FlashCard:
    def __init__(self):
        self.fruits = {
            "Banana": "yellow",
            "Strawberries": "pink",
            "Apple": "red",
            "Grapes": "green"
        }

    def play(self):
        fruit, color = random.choice(list(self.fruits.items()))

        print("\nWhat is the color of", fruit)
        user_answer = input().strip().lower()

        if user_answer == color.lower():
            print("Correct answer")
        else:
            print("Wrong answer")




print("Welcome to fruit quiz")

obj = FlashCard()

while True:
    obj.play()
    choice = input("Enter 0 to play again, 1 to exit: ").strip()
    if choice == "0":
        break
