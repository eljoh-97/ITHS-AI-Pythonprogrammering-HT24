import random
from output_list import random_words

class Hangman:
    
    def __init__(self, use_random_words=True):
        
        # Only used for testing purpose when use_random_words is set to False
        testing_words = ["fanta", "sprite", "cola", "pepsi"]
        
        if use_random_words and random_words:
            self.word = random.choice(random_words)
        else:
            self.word = random.choice(testing_words)
        
        self.display = ['_' for letter in self.word]
        self.guesses = 0
        self.guessed_letters = set()
    
    def __str__(self):
        display = ' '.join(self.display)
        return f"Ordet är: {display}"
    
    def get_word(self, guess):
        # Check, if the letter exist or not
        if guess in self.guessed_letters:
            print(f"Du har redan gissat på följande bokstav: '{guess}'!")
            
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
            print(f"Bokstanven '{guess}' finns inte i ordet.")


    def check_win(self):
        # Check if all letters have been guessed
        if self.display == list(self.word):
            print("\nVinst!!!")
            return True
        return False
        
def main():
    print("Programmet startar...\n")
    use_random_words = False  # Set to False to use testing words list
    word = Hangman(use_random_words)
    print("Välkommen till Hänga Gubbe!")
    name = None
    try:
        while name is None:
            try:
                name = input("Vad är ditt namn?\n").capitalize()
            except KeyboardInterrupt:
                print("\nVänligen, försök igen att ange ditt namn")
                continue
        while True:
            try:
                identify_the_user = input(f"\n{name} kan du spelets regler? (Ja / Nej): \n").lower()
                if identify_the_user == "ja":
                    print("\nHärligt! Låt spelet börja.")
                    break
                elif identify_the_user == 'nej':
                    print("\n----------------------------------------------------------------------------------------------------------------------------------------------------")
                    print("""Okej! Här kommer en kort beskrivning kring spelets regler:\nHänga gubbe är orgniellt en penna- och papperslek för en eller flera deltagare. Men här kommer vi istället använda oss av en dator.\nSpelet går ut på att gissa bokstäver i ett ord vars bokstäver initialt är helt dolda, men som visas som ledtrådar när spelaren lyckats gissa på dem.""")
                    print("----------------------------------------------------------------------------------------------------------------------------------------------------")
                    break
                else:
                    print("Du har angett ett felaktigt värde, vänligen ange 'Ja' eller 'Nej.")
            except KeyboardInterrupt:
                print("\nFelaktig inmatning. Vänligen ange 'Ja' eller 'Nej och försök igen.")
                continue
            except ValueError:
                print("\nFelaktig inmatning. Vänligen ange 'Ja' eller 'Nej och försök igen.")
                continue

        while True:
            try:
                guess = input(f"\n{name} vänligen gissa en bokstav: ").lower()
                if len(guess) != 1 or not guess.isalpha():
                    print("Ange endast en enda bokstav\n")
                    continue
                word.check_guess(guess)
                print(word)
                word.guesses += 1
                if word.check_win():
                    print(f"{name}, det tog dig {word.guesses} gissningar!")
                    break
            except KeyboardInterrupt:
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
