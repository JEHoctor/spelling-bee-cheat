from spelling_bee_cheat.dictionary_search import dictionary_search


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
        )

        expected_words = [
            "a",
            "ab",
            "bac",
        ]

        assert words == expected_words