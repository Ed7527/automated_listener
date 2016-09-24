import winsound
import random
import time
import inspect
file_loc = (inspect.stack()[0][1])[:-11]

mmm_sound = "{}sound files/mmmm.wav".format(file_loc)
yeah_sound = "{}sound files/yeah.wav".format(file_loc)
really_sound = "{}sound files/really".format(file_loc)
uhhuh_sound = "{}sound files/uhhuh.wav".format(file_loc)

list_of_sounds = [mmm_sound, yeah_sound, really_sound, uhhuh_sound]

while True:
    random_amount_of_seconds_to_wait = random.randint(3, 6)
    time.sleep(random_amount_of_seconds_to_wait)

    random_sound = list_of_sounds[random.randint(0, 3)]

    winsound.PlaySound(random_sound, winsound.SND_FILENAME)