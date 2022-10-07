#!/usr/bin/env python3

import os
import aiml
from gtts import gTTS
import os

BRAIN_FILE="hippocampus.brn"
language = 'en-uk'

k = aiml.Kernel()

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
    input_text = input(" Human : > ")
    response = k.respond(input_text)
    tts = gTTS(text=response, lang=language, slow=False)
    tts.save("MIRA.mp3")
    print(" [ MIRA ] > "+response)
    os.system("mpg321 -q MIRA.mp3")
    if response == "See you Later ." or response == "Bye." or response == "TTYL, ." or response == "Goodbye." or response == "Thanks for chatting, ." or response == "Sayonara." or response == "Until next time.":
        print("*** MIRA exit chatting ***")
        break


#while True:
#    reply = k.respond(input(" Human : >>>> "))
#    if reply:
#        print(" [ MIRA ] >>>>  ", reply)
#    else:
#        print(" [ MIRA ] >>>>   :) ", )
