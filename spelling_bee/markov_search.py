import typing as tp
from itertools import product
from string import ascii_lowercase

import numpy as np
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline

from spelling_bee.dictionary import load_default_dictionary
from spelling_bee.nyt_scraping import PuzzleData

from tqdm import tqdm


ascii_lowercase_list = list(ascii_lowercase)


class MarkovSearch:
    """
    """

    @classmethod
    def _make_word(cls, g, l):
        return "".join(g.choice(ascii_lowercase_list, size=l))

    @classmethod
    def _make_negative_word(cls, g, l, positive_words):
        while True:
            word = cls._make_word(g, l)
            if word not in positive_words:
                return word

    @classmethod
    def _make_negative_words(cls, positive_words, g):
        positive_word_set = set(positive_words)
        return tuple(
            cls._make_negative_word(g, len(pword), positive_word_set)
            for pword in tqdm(positive_words, desc="making negative words")
        )

    @classmethod
    def _make_dataset(cls, random_state):
        g = np.random.default_rng(seed=random_state)

        positive_examples = load_default_dictionary()
        negative_examples = cls._make_negative_words(positive_examples, g)

        return pd.concat((
            pd.DataFrame({"word": positive_examples, "exists": True}),
            pd.DataFrame({"word": negative_examples, "exists": False}),
        ))

    def __init__(self, random_state=1234):
        """
        """
        self.pipeline = make_pipeline(
            TfidfVectorizer(analyzer="char_wb", ngram_range=(1, 3)),
            LogisticRegression(C=0.1),
        )

        self.dataset = self._make_dataset(random_state)

        self.pipeline.fit(self.dataset["word"], self.dataset["exists"])

    def markov_search(self, pdat: PuzzleData) -> tp.List[str]:
        """
        """
        valid_letters = pdat.valid_letters
        center_letter = pdat.center_letter
        max_length = pd.Series(pdat.answers).str.len().max()

        words = []
        for length in range(4, max_length + 1):
            for letters in product(*[valid_letters] * length):
                if center_letter in letters:
                    words.append("".join(letters))

        words_df = pd.DataFrame({
            "word": words,
            "dfunc": self.pipeline.decision_function(words)
        })
        return words_df.sort_values("dfunc", ascending=False)["word"].to_list()
