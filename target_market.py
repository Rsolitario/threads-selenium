from settings import *

class Hashtag:

    def __init__(self) -> None:
        self.n = 0
        with open(Settings.hashtagfile, "r", encoding='utf-8') as f:
            self._l_word = f.read().split('\n')

    def next(self, sequence:int):
        # operaciones para encontrar el siguiente
        print("next: ", sequence, Settings.range_feed)
        if sequence == Settings.range_feed - 1:         
            self.n = self.n % len(self._l_word)
            self.n += 1
            print(self.n)
        return self._l_word[self.n - 1]
    
    def current(self):
        return "love"

class Target:
    hashtag = Hashtag()