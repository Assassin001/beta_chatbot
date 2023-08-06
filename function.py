import time
from datetime import date
import pygame
from storage1 import *

def time_1():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    response = "Current time is: " + current_time
    return response

def greet_user():
    response = "Hello! How can I assist you today?"
    return response

def farewell_user():
    response = "Goodbye! Have a great day!"
    return response

def get_weather():
    response = "No Idiea"
    return response

def date_1():
    today1 = date.today()
    today1 = str(today1)
    response ="Today is " + today1
    return response

def play():
    response = "Playing ...."
    play1()
    return response


#def play_music(file_path):
    #pygame.init()
    #pygame.mixer.init()

    #try:
        #pygame.mixer.music.load(file_path)
        #pygame.mixer.music.play()
        #while pygame.mixer.music.get_busy():
            #pygame.time.Clock().tick(10)
    #except pygame.error:
        #print("Error loading or playing music.")

#file_path = "lp.mp3"  # Replace with the path to your music file
#play_music(file_path)
