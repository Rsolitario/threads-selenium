import random

class Settings:
    range_feed = 37
    debug = True
    scroll = 3
    sleep_time = random.randint((60*55), (60*65*2))
    max_sleep_run = random.randint(60, max(60, 120))
    maximum_number_of_likes = random.randint(8, 12)
    hashtagfile  = "hashtagfile"