from pygame import mixer

mixer.init()

def play_sound(sound_file: str):
    sound = mixer.Sound(sound_file)
    sound.play()

def stop_sound():
    mixer.stop()