from typing import List

from nltk.corpus import brown, gutenberg, inaugural, reuters, webtext, words


class DictionarySearch:
    """
    Class for caching the nltk word list for use with the dictionary_search function
    """

    dictionary: List[str] = None

    @classmethod
    def load_default_dictionary(cls):
        """
        Load word lists from several NLTK corpora and combine to create a large word list
        """
        corpora = [brown, gutenberg, inaugural, reuters, webtext, words]
        dictionary = set()
        for corpus in corpora:
            dictionary |= set(word.lower() for word in corpus.words())
        cls.dictionary = sorted(dictionary)

    @classmethod
    def dictionary_search(
        cls,
        letters: str,
        center_letter: str,
        dictionary: List[str] = None,
        min_len: int = 4,
    ) -> List[str]:
        """
        Filter a list of words to those that satisfy the rules of the spelling bee game:
         - contains only letters from the 7 given
         - contains the letter at the center of the puzzle at least once
         - has a minimum length (usually 4)

        Args:
            letters: a string containing the seven allowed letters
            center_letter: a string containing the letter in the center of the puzzle
            dictionary: a list of words to consider. Defaults to nltk.corpus.words.words()
            min_len: the minimum length of word to accept. Defaults to 4, which is standard for spelling bee

        Returns:
            List[str]: a list of words from the dictionary list that obey the rules of the game
        """
        if dictionary is None:
            if cls.dictionary is None:
                cls.load_default_dictionary()
            dictionary = cls.dictionary

        letter_set = set(letters.lower())
        center_letter = center_letter.lower()

        words_found = [
            word
            for word in dictionary
            if len(word) >= min_len
            and center_letter in word
            and set(word) <= letter_set
        ]

        return words_found


dictionary_search = DictionarySearch.dictionary_search
