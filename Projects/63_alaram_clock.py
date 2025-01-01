# Python Alarm Clock

import time
import datetime
import pygame


def set_alarm(alarm_time):
    sound_file = "/home/shathwik1/Desktop/Python Tutorial/Projects/audio.wav"
    is_running = True

    while is_running:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(current_time)
        if current_time == alarm_time:
            print("WAKE UP!")
            pygame.mixer.init()
            pygame.mixer.music.load(sound_file)
            pygame.mixer.music.play()
            is_running = False
        time.sleep(1)


def main():
    alarm_time = input("Enter the alarm time (HH:MM:SS): ")
    set_alarm(alarm_time)


if __name__ == "__main__":
    main()
