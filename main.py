import random

# Class to represent a Word and its Hint
class WordHint:
#This class initilize a word and its associated hint.
    
    def __init__(self, word, hint):
        self.word = word  # it's a varialble that stores the word that the player has to guess. 
        self.hint = hint  # A variable to help the player

    def is_letter_in_word(self, letter): # Checks if the guessed letter is part of the word.
       return letter in self.word

# Function to load words and hints from a file
def load_words(filename):
    
#Reads the file and creates a list of WordHint objects.
#Each line in the file should contain a word and its hint, separated by a comma.
    
    words = []
#try and except blocks in this program are using for exception and handling. 
    try: 
        with open(filename, "r") as file: #passing a file name my_word.txt
            for line in file:
                word, hint = line.strip().split(",")
                words.append(WordHint(word, hint))
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found!")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
    return words

# Function to display the current state of the guessed word
def display_word(word, guessed_letters):
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter + " "
        else:
            displayed_word += "_ "
    return displayed_word.strip()
#Display the word with guessed letters revealed and blanks for unguessed letters.
    

# Function to save the user's score to a file
def save_score(filename, score, total):
    
#writes the player's score to a file.
    with open(filename, "w") as file: 
        file.write(f"Final Score: {score}/{total}\n")

# Main function for the Hangman game
def play_hangman(word_list):
   
#Main function to play the Hangman game.
    
    score = 0  # Player's score
    total_questions = len(word_list)  # Total number of words

    print("Welcome to the Hangman Game!\n")

    # Iterate through each word in the word list
    for index, word_hint in enumerate(word_list):
        print(f"\nQuestion {index + 1}")
        print(f"Hint: {word_hint.hint}")

        guessed_letters = set()  # Store guessed letters
        attempts = 4  # Maximum attempts per word

        while attempts > 0:
            #the current progress of the word
            print("\n" + display_word(word_hint.word, guessed_letters))
            print(f"Attempts left: {attempts}")

            guess = input("Guess a letter: ").lower()

            #Making the input value is valid
            if len(guess) != 1 or not guess.isalpha():
                print("Invalid input! Please guess a single letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter!")
                continue
            guessed_letters.add(guess)

            # Check if the guess is correct
            if word_hint.is_letter_in_word(guess):
                print(f"Good job! '{guess}' is in the word!")
            else:
                print(f"Oops! '{guess}' is not in the word.")
                attempts -= 1

            # Check if the player guessed the word
            word_guessed = True
            for letter in word_hint.word: #this loop will iteraters the letters through the word_hint.word
                if letter not in guessed_letters: #this will check the letter present in guessed_letter or not.
                    word_guessed = False 
                    break

            if word_guessed:
                print(f"\nCongratulations! You've guessed the word: {word_hint.word}")
                score += 1  # Increment score for a correct guess
                break
        else:
            print(f"\nOut of attempts! The word was: {word_hint.word}")

    # Display final score and save to a file
    print(f"\nGame Over! Your final score is: {score}/{total_questions}")
    save_score("score.txt", score, total_questions)

# Main program execution
if __name__ == "__main__":
    # Assigning the words file
    words_file = "my_words.txt"

    # read words from the file
    words = load_words(words_file)

    # Play the Hangman game
    if words:
        play_hangman(words)