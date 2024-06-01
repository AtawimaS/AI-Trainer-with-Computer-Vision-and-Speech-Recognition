import speech_recognition as sr
import pyttsx3
listener = sr.Recognizer()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)##voice[1] for girl voice , voice[0] for man voice

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
                speak("yes")
    except:
        pass
    return command

def main():
    command = Take_Command()
    print(command)
    if 'main' in command:
        print("playing")
        speak("Mari Bermain")
main()