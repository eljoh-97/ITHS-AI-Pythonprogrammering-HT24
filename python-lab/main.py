import random
from output_list import random_words
import colored
from colored import stylize

green = colored.fg(2) # green
blue =  colored.fg(4) # blue
red =  colored.fg(9) # light red
yellow = colored.fg(3) # yellow
magenta = colored.fg(5) # magenta
cyan = colored.fg(6) # cyan               

class Hangman:
    
    def __init__(self, use_random_words=True, max_guesses=15):
        
        # Only used for testing purpose when use_random_words is set to False
        testing_words = ["fanta", "sprite", "cola", "pepsi"]
        
        if use_random_words and random_words:
            self.word = random.choice(random_words)
        else:
            self.word = random.choice(testing_words)
        
        self.display = ['_' for letter in self.word]
        self.guesses = 0
        self.guessed_letters = set()
        self.max_guesses = max_guesses
    
    def __str__(self):
        display = ' '.join(self.display)
        return f"Ordet är: {display}"
    
    def get_word(self, guess):
        # Check, if the letter exist or not
        if guess in self.guessed_letters:
            print(stylize(f"Du har redan gissat på följande bokstav: '{guess}'!", magenta))
            
        # Else, proceed and add it to the guess list
        guess_list = []
        for index, char in enumerate(list(self.word)):
            if char == guess:
                guess_list.append(index)
        
        self.guessed_letters.add(guess)
        return guess_list
    
    def update(self, idx, letter):
        # Remove the '_' with the correct letter
        for number in idx:
            self.display[number] = letter
    
    def check_guess(self, guess):
        # Check if the guessed letter is in the word
        if guess in self.word:
            idx = self.get_word(guess)
            self.update(idx, guess)
        else:
            print(stylize(f"Bokstaven '{guess}' finns inte i ordet.\n", yellow))

    def check_loss(self):
        # If the user has guessed more than max_guesses
        if self.guesses >= self.max_guesses:
            print(stylize(f"\nTyvärr så har du gissat {self.guesses} gånger vilket är mycket! Ordet vi sökte var: {self.word}\n", red))
            return True
        return False

    def check_win(self):
        # Check if all letters have been guessed and inside the max_guesses range
        if self.display == list(self.word):
            print(stylize(f"\nGrattis du har gissat rätt!!, rätt ord var: {self.word}!", green))
            return True
        return False
    
    def number_of_guess_left(self):
        # Display the number of guess left, until the user has reached the correct word
        guess_left = self.max_guesses - self.guesses
        if guess_left != 0:
            print(stylize(f"Du har {guess_left} gissningar kvar\n", cyan))
        elif guess_left == 0:
            return guess_left
        
def main():
    print("Programmet startar...\n")
    use_random_words = True  # Set to False to use testing words list
    word = Hangman(use_random_words, max_guesses=15)
    print("Välkommen till Hänga Gubbe!")
    name = None
    try: # Prevent the program from crashing by error handler: 'KeyboardInterrupt'
        
        # 1st while loop will run until a valid value has been inputted
        while name is None:
            try: # Prevent the program from crashing by error handler: 'KeyboardInterrupt'
                name = input("Vad är ditt namn?\n").capitalize()
            except KeyboardInterrupt:
                print("\nVänligen, försök igen att ange ditt namn")
                continue
        # 2nd while loop will run until check if the user are aware of the rules of the program, will run until a valid value has been inputted
        while True:
            try: # Prevent the program from crashing by error handler: 'KeyboardInterrupt' + 'ValueError'
                identify_the_user = input(f"\n{name} kan du spelets regler? (Ja / Nej): \n").lower()
                if identify_the_user == "ja": # In case of 'Yes', the while loop ends and continue the program
                    print("\nHärligt! Låt spelet börja.")
                    break
                elif identify_the_user == 'nej': # In case of 'No', we print out a short description and the while loop ends and continue the program
                    print(stylize("\n----------------------------------------------------------------------------------------------------------------------------------------------------", blue))
                    print(stylize("""Okej! Här kommer en kort beskrivning kring spelets regler:\nHänga gubbe är orgniellt en penna- och papperslek för en eller flera deltagare. Men här kommer vi istället använda oss av en dator.\nSpelet går ut på att gissa bokstäver i ett ord vars bokstäver initialt är helt dolda, men som visas som ledtrådar när spelaren lyckats gissa på dem.""", blue))
                    print(stylize("----------------------------------------------------------------------------------------------------------------------------------------------------", blue))
                    break
                else:
                    print("Du har angett ett felaktigt värde, vänligen ange 'Ja' eller 'Nej.")
            except KeyboardInterrupt:
                print("\nFelaktig inmatning. Vänligen ange 'Ja' eller 'Nej och försök igen.")
                continue
            except ValueError:
                print("\nFelaktig inmatning. Vänligen ange 'Ja' eller 'Nej och försök igen.")
                continue
        # 3rd while loop will run until the program is done, displaying win, losses & remaining guesses 
        while True:
            try: # Prevent the program from crashing by error handler: 'KeyboardInterrupt' + 'ValueError'
                guess = input(f"\n{name} vänligen gissa en bokstav: ").lower() # Check if the inputted value is str and an alphabetic string, if not print out a message
                if len(guess) != 1 or not guess.isalpha():
                    print("Ange endast en enda bokstav\n")
                    continue
                word.check_guess(guess) # Check if the letter is already guessed
                print(word)
                word.guesses += 1 # Track incorrect guesses
                word.number_of_guess_left() # Number of guesses left
                if word.check_loss(): # In case of loss
                    break
                if word.check_win(): # In case of win
                    print(stylize(f"{name}, det tog dig {word.guesses} gissningar!\n", green))
                    break
            except KeyboardInterrupt: # Prevent the program from crashing  - in case of typing e.g CTRL+C 
                print("\nFelaktig inmatning. Vänligen ange en bokstav och försök igen.")
                continue
            except ValueError:
                print("\nFelaktig inmatning. Vänligen ange en bokstav och försök igen.")
                continue
            except Exception as e:
                print(f"\n Ett fel har inträffat {e}. Vänligen försök igen!")
    except KeyboardInterrupt:
        print("\nKeyboardInterrupt caught. Programmet avslutas nu.")
    except Exception as e:
        print(f"\nOväntat fel: {e}. Programmet avslutas nu.")
    finally:
        print("Tack för att du spelade Hänga Gubbe.")

if __name__ == "__main__":
    main()
