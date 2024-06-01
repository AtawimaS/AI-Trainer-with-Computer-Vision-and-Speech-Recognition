import speech_recognition as sr
import pyttsx3
from AITrainer import Training

listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)##voice[1] untuk suara cewek, voice[0] untuk suara laki

def speak(command):
    engine.say(command)
    engine.runAndWait()
def Take_Command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice =listener.listen(source)
            command = listener.recognize_google(voice, language="id")
            command = command.lower()
            if 'cek' in command:
                command = command.replace('cek', '')
                speak("ok")
    except:
        pass
    return command

def main():
    command = Take_Command()
    print(command)
    if 'latihan' in command:
        trainer = Training()  # Create an instance of the Training class
        trainer.start_training()  # Call the start_training method
        print("yey")

while True:
    main()