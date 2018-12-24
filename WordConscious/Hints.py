
from LinkedList.LinkedList import List

from secrets import randbelow

class Hints:

    def __init__(self, min_chars_unrevealed: int):

        self.min_chars_unrevealed: int = min_chars_unrevealed

        self.current_hint_index: int = 0

        self.current_guess_word: str = str()

        self.chars_revealed: int = 0

    def get_hint(self, guessable_words: List) -> str:

        """
        Take the list of current guessable words, and return a hint
        string. Example: he***
        """
        
        # Check if the current_word is outside the bounds of the list

        current_guess_word: str = None

        current_hint_index: int = self.current_hint_index

        if (current_hint_index < guessable_words.length):

            current_guess_word = guessable_words[current_hint_index]

        # If the index has gone out of bounds (caused by words being guessed)
        # or the indexes have changed (can be caused by a word being guessed or
        # The Hints object being new)
        # then pick a new random word from the list
        if current_guess_word == None or not \
           current_guess_word == self.current_guess_word:

            new_rand_index: int = randbelow(guessable_words.length)

            # Reset the revealed characters count to 0

            self.chars_revealed = 0

            new_guess_word: str = guessable_words[new_rand_index]

            # Update the current guess word and hint_index to their new values
            current_guess_word = new_guess_word
            
            self.current_hint_index = new_rand_index

            self.current_guess_word = new_guess_word

        # Now that the value of the current_guess_word is known,
        # build the hint string.
        current_hint_word_length: int = len(current_guess_word)

        hint_string: list = list()

        # Build the new hint string using current_guess_word
        # Reveal one more character, than previously revealed (if applicable)
        # unless it is over the min_chars_revealed limit
        # Hide all other characters with *
        for i in range(0, current_hint_word_length):

            if i <= self.chars_revealed and i < (current_hint_word_length - self.min_chars_unrevealed):

                hint_string.append(current_guess_word[i])

            else:

                hint_string.append("*")

        self.chars_revealed += 1

        return str().join(hint_string)
        