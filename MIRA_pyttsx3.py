#!/usr/bin/env python3

import os
import aiml
import pyttsx3

BRAIN_FILE="hippocampus.brn"
language = 'en-uk'

k = aiml.Kernel()
engine = pyttsx3.init()
voices = engine.getProperty('voices')

# part to learn everything and store in the brain
if os.path.exists(BRAIN_FILE):
    print("Loading from memory: " + BRAIN_FILE)
    k.loadBrain(BRAIN_FILE)
else:
    print("Parsing aiml files")
    k.bootstrap(learnFiles="std-startup.aiml", commands="LIBRARY")
    print("Saving memory: " + BRAIN_FILE)
    k.saveBrain(BRAIN_FILE)

# Endless loop which passes the input to the bot and prints
# its response
while True:
# to get list of voice in PC
#    for voice in voices:
#        print(voice, voice.id)
#        engine.setProperty('voice', voices[2].id)
    engine.setProperty('voice', voices[6].id) # change voice from list
    input_text = input(" Human : > ")
    response = k.respond(input_text)
    engine.say(response)
    print(" [ MIRA ] > "+response)
    engine.runAndWait()
    if response == "See you Later ." or response == "Bye." or response == "TTYL, ." or response == "Goodbye." or response == "Thanks for chatting, ." or response == "Sayonara." or response == "Until next time.":
        print("*** MIRA exit chatting ***")
        break


#while True:
#    reply = k.respond(input(" Human : >>>> "))
#    if reply:
#        print(" [ MIRA ] >>>>  ", reply)
#    else:
#        print(" [ MIRA ] >>>>   :) ", )
