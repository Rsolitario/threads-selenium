
class Hashtag:

    def __init__(self) -> None:
        self.current_word = ""

    def next(self):
        # operaciones para encontrar el siguiente
        self.current_word = "trading"
        return "trading"
    
    def current(self):
        return "trading"

class Target:
    hashtag = Hashtag()