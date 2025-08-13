import pyttsx3
engine = pyttsx3.init()
print("Listening to you.....")
write = input("Enter something:")
engine.say(write)
engine.runAndWait()