import speech_recognition as sr

def speech_to_text():

    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)

        print("Speak now...")

        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)

        return text

    except Exception:
        return ""