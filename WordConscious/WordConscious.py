import configparser
from LinkedList.LinkedList import List
from Hints import Hints
from Words import Words, GuessSet

def main():
    # Read configurable values in from the configuration file
    config: configparser.ConfigParser = configparser.ConfigParser()
    config.read("WordConscious.conf")
    # Make sure that the config for playing exists.
    # Otherwise the game cannot be played.
    if not config.has_section("WordConscious"):
        print("Configuration file not loaded. Exiting.")
        return

    hints: Hints = Hints(int(config["WordConscious"]["min_left_hint_reveal"]))
    # Enter into the play loop. (User is now playing until they enter q.)
    while True:
        # Get a set of random words from the words file, and the characters that they are made up of in a random order.
        guess_set: GuessSet = Words.get_guess_set(config["WordConscious"]["words_file_path"], int(config["WordConscious"]["amount_of_words_per_set"]), 
                                                  int(config["WordConscious"]["minimum_word_length"]), int(config["WordConscious"]["maximum_word_length"]))
        guessable_words = guess_set.words
        # If there are 0 words from get_guess_set, try again to get words
        if guessable_words.length == 0:
            continue

        guessable_characters = guess_set.characters
        # Show the user the characters, and the game is afoot!
        print(guessable_characters)

        while True:
            guess: str = input("Enter a word to guess (? for help, q to quit.)-> ")
            guess_lower = guess.lower()

            if guess_lower == "?":
                print("===WordConscious Help===\n" + \
                      "\t? -> This help screen\n" + \
                      "\ts -> Shuffle\n" + \
                      "\th -> Hint\n" + \
                      "\tw -> Number of words left\n" + \
                      "\tq -> quit")

            elif guess_lower == "q":
                return

            elif guess_lower == "s":
                guessable_characters.shuffle()
                print(guessable_characters)

            elif guess_lower == "h":
                print(hints.get_hint(guessable_words))

            elif guess_lower == "w":
                print("Word(s) Left: " + str(guessable_words.length))

            elif guess in guessable_words:
                guessable_words.remove_value(guess)
                words_list_length: int = guessable_words.length

                if not words_list_length == 0:
                    print("Correct! " + str(words_list_length) + " word(s) left.")
            
            else:
                print("Wrong guess! Try again.")

            if guessable_words.length == 0:
                print("All words guessed!")
                break

if __name__ == "__main__":
    main()
