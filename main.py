import random

class SimpleAIGuessingGame:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.previous_guesses = []
        self.max_attempts = 7
        
    def get_hint(self, guess):
        """AI-like hint system based on previous guesses"""
        if not self.previous_guesses:
            return "Try to guess my number between 1 and 100!"
        
        # Analyze previous guesses to give better hints
        last_guess = self.previous_guesses[-1]
        
        if abs(guess - self.number) < abs(last_guess - self.number):
            return "You're getting warmer!"
        else:
            return "You're getting colder."
        
    def evaluate_guess(self, guess):
        """Evaluate the guess and provide feedback"""
        if guess == self.number:
            return "correct"
        elif guess < self.number:
            return "too low"
        else:
            return "too high"
    
    def play(self):
        """Main game loop"""
        print("🎯 Welcome to the AI Number Guessing Game!")
        print(f"I'm thinking of a number between 1 and 100.")
        print(f"You have {self.max_attempts} attempts to guess it!\n")
        
        attempts = 0
        
        while attempts < self.max_attempts:
            try:
                guess = int(input("Enter your guess: "))
                attempts += 1
                self.previous_guesses.append(guess)
                
                result = self.evaluate_guess(guess)
                
                if result == "correct":
                    print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                    print(f"The number was indeed {self.number}!")
                    break
                else:
                    print(f"Your guess is {result}.")
                    
                    # AI hint
                    if len(self.previous_guesses) > 1:
                        hint = self.get_hint(guess)
                        print(f"💡 Hint: {hint}")
                    
                    remaining = self.max_attempts - attempts
                    print(f"Attempts left: {remaining}\n")
                    
            except ValueError:
                print("Please enter a valid number!\n")
                continue
        
        if attempts >= self.max_attempts and self.previous_guesses[-1] != self.number:
            print(f"💔 Game Over! The number was {self.number}.")
            print("Better luck next time!")

# Run the game
if __name__ == "__main__":
    game = SimpleAIGuessingGame()
    game.play()