# Write a Python program to use the pyttsx3 library for text-to-speech.
import pyttsx3 
# init() = turning ON the speaker
engine = pyttsx3.init() 
# say() = telling what to speak
engine.say("My Name is Rimsha Fatima and i am recently graduate in Artifical Inteligence")
# runAndWait() = actually speaking
engine.runAndWait()