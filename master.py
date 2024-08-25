from settings import Settings
class Sequence:
    sequence = 0

    def int_sequence(self):
        self.sequence += 1
        self.sequence = self.sequence % Settings.range_feed       
        return self.sequence