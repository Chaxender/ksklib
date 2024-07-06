import speech_recognition as sr
import pyttsx3

def listen_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Dinliyorum...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio, language="tr-TR")
            print(f"Komut: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("Anlamadım")
            return ""
        except sr.RequestError:
            print("Google Servisine erişilemiyor")
            return ""

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

if __name__ == "__main__":
    while True:
        command = listen_command()
        if "merhaba" in command:
            speak("Merhaba! Size nasıl yardımcı olabilirim?")
        elif "nasılsın" in command:
            speak("Teşekkür ederim, siz nasılsınız?")
        elif "kapat" in command:
            speak("Görüşürüz!")
            break
