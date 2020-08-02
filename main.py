#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick

# Create your objects here.
ev3 = EV3Brick()

# Write your program here.
ev3.speaker.set_volume(100)
ev3.speaker.beep()

# Define phrase to speak
sample = "The five boxing wizards jump quickly"

# Set other options
wordsPerMinute = 180
voicePitch = 50

# Define an array of possible voices
voices = ['f1', 'f2', 'f3', 'f4', 'f5',
          'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7',
          'croak', 'whisper', 'whisperf']

# Loop through each voice and repeat the phrase
for voice in voices:

    ev3.speaker.set_speech_options(None, voice, wordsPerMinute, voicePitch)
    ev3.speaker.say(sample)

# Sample the f1 voice using different pitches
for i in range(1, 99, 32):

    ev3.speaker.set_speech_options(None, 'f1', wordsPerMinute, i)
    ev3.speaker.say(sample)

# Sample the f1 voice using different words per minute
for i in range(60, 400, 60):

    ev3.speaker.set_speech_options(None, 'f1', i, voicePitch)
    ev3.speaker.say(sample)
