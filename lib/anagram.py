class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, candidates):
        sorted_word = sorted(self.word)  # Sort the letters of the initialized word
        matches = []
        for candidate in candidates:
            if sorted_word == sorted(candidate):  # Compare sorted version of candidate to sorted word
                matches.append(candidate)
        return matches
