# Game status categories
# Change the values as you see fit
from collections import defaultdict

STATUS_WIN = 'win'
STATUS_LOSE = 'lose'
STATUS_ONGOING = 'ongoing'


# At each turn a player guesses a character;
# if it exists in the word, then the character is placed
# at its corresponding indices of the masked word.
# If it doesn't exist in the word, the number of remaining
# guesses is decremented by one.
# The game ends when the complete word has been guessed
# correctly, or 10 guesses have been exhausted.
class Hangman:
    def __init__(self, word: str) -> None:
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING
        self.masked_word = ['_'] * len(word)
        self.index_map = defaultdict(list)
        for (i, ch) in enumerate(word):
            self.index_map[ch].append(i)

    def guess(self, char: str) -> None:
        if self.status != STATUS_ONGOING:
            raise ValueError('The game has already ended.')
        if char in self.index_map:
            for i in self.index_map.pop(char):
                self.masked_word[i] = char
            if not self.index_map:
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

    def get_masked_word(self) -> str:
        return ''.join(self.masked_word)

    def get_status(self) -> str:
        return self.status
