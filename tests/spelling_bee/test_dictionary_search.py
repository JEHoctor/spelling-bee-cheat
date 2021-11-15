from spelling_bee import dictionary_search, DictionarySearch

class TestDictionarySearch:

    def test_dictionary_search(self):
        words = dictionary_search(
            letters="abc",
            center_letter="a",
            dictionary=[
                "a",
                "ab",
                "bac",
                "abch",
                "bcbc",
            ],
            min_len=2,
        )

        expected_words = [
            "ab",
            "bac",
        ]

        assert words == expected_words

    def test_load_default_dictionary(self):

        assert DictionarySearch.dictionary is None

        _ = dictionary_search(
            letters="abcde",
            center_letter="a",
        )

        assert isinstance(DictionarySearch.dictionary, list)
