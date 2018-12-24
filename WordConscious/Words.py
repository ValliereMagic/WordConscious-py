
from LinkedList.LinkedList import List

from secrets import randbelow

class GuessSet:

    def __init__(self, words: List, characters: List):

        """
        Words should be all the words that can be corrctly guessed.
        Characters should be a list of all the characters used to make up
        the words in the words list.
        """

        self.words = words

        self.characters = characters


class Words:

    @staticmethod
    def get_guess_set(file_path: str, number_of_words: int, min_word_length: int, max_word_length: int) -> GuessSet:
        
        """
        Return a set of words and characters for the user to guess
        the words using the characters list in the guess set.
        Returns a GuessSet.
        """

        possible_words: List = Words.get_words_from_file(file_path)

        if possible_words.length == 0:
            return None

        pickable_words: List = Words.pick_words_from_available(possible_words, number_of_words, 
                                                               min_word_length, max_word_length)

        pickable_chars: List = Words.get_characters_from_pickable_words(pickable_words)

        return GuessSet(pickable_words, pickable_chars)

    @staticmethod
    def get_words_from_file(file_path: str) -> List:

        """
        Retrieves all the words in the file path passed
        (assumes that there is one word per line)
        and adds those words to a new LinkedList
        (returns the new linked list populated with the words)
        """

        with open(file_path, "r", encoding="utf8") as words_file:

            new_words_list: List = List()    
            
            for word in words_file:

                new_words_list.add(word.replace("\n", ""))

            return new_words_list
        
        return List()

    @staticmethod
    def pick_words_from_available(words_available: List, number_of_words: int, min_chars: int, max_chars: int) -> List:

        """
        From all the worlds available to guess
        pick at random the amount of words passed in number_of_words
        and return a new list containing those randomly chosen words.
        """

        num_available_words: int = words_available.length

        pickable_words: List = List()

        number_of_words_it: int = number_of_words

        i: int = 0

        while i < number_of_words_it:

            rand_index: int = randbelow(num_available_words)

            rand_word: str = words_available[rand_index]

            rand_word_length = len(rand_word)

            if not rand_word in pickable_words and \
               rand_word_length >= min_chars and rand_word_length <= max_chars:

                pickable_words.add(rand_word)

            else:
                
                number_of_words_it += 1

            i += 1

            if number_of_words_it > number_of_words * 4:

                break

        return pickable_words

    @staticmethod
    def get_characters_from_pickable_words(pickable_words: List) -> List:

        """
        From the pickable words available from this set
        retrieve a list of the characters the words are made up of.
        """

        # Dictionary for characters mapped to their required occurances
        char_dict: dict = {}

        for i in range(0, pickable_words.length):

            current_word: str = pickable_words[i]

            # Dictionary for characters mapped to their required occurances
            # in the current word being inspected.
            local_char_dict: dict = {}
            
            # populate local_char_dict with the characters contained
            # in current word with their occurances eg. 'a': 1
            for char in current_word:

                if not char in local_char_dict:
                    
                    local_char_dict[char] = 1

                else:
                    local_char_dict[char] += 1

            # Update the guess_characters dictionary to
            # the new values found in the current word
            # if necessary.
            for key in local_char_dict:
                
                # If the character doesn't exist
                # in the char_dict, add it
                # Or if there are more characters
                # in the current word than 
                # exist in the guess_characters
                # update the value in char_dict
                if not key in char_dict or \
                   local_char_dict[key] > char_dict[key]:

                    char_dict[key] = local_char_dict[key]
        
        # From the created dictionary of characters
        # mapped to occurances, build the guess characters list
        guess_characters: List = List()
       
        for key in char_dict:

            for _ in range(0, char_dict[key]):
                
                guess_characters.add(key)

        # Shuffle the list so that the characters
        # aren't all in line
        guess_characters.shuffle()

        return guess_characters
            