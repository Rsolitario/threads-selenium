from settings import *

class Hashtag:

    def __init__(self) -> None:
        self.n = 0
        with open(Settings.hashtagfile, "r", encoding='utf-8') as f:
            self._l_word = f.read().split('\n')
        del self._l_word[len(self._l_word) - 1]

    def next(self, sequence:int):
        # operaciones para encontrar el siguiente
        if Settings.debug:
            print("next: ", sequence, Settings.range_feed)
        if sequence == Settings.range_feed - 1:         
            self.n = self.n % len(self._l_word)
            self.n += 1
            if Settings.debug:
                print(self.n)
        return self._l_word[self.n - 1]
    
    def current(self):
        return "love"

class Target:
    hashtag = Hashtag()