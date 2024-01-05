# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, possibilities):
        matched = []
        word_letters = [letter for letter in self.word]
        for possible in possibilities:
            possible_letters = [letter for letter in possible]
            if sorted(word_letters) == sorted(possible_letters):
                matched.append(possible)
        return matched
