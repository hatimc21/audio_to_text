import speech_recognition as sr
import keyboard # type: ignore

def transcribe_audio():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    print("Press '0' to start recording audio.")

    while True:
        keyboard.wait("0")
        print("Recording... Press '1' to stop.")
        with microphone as source:
            recognizer.adjust_for_ambient_noise(source)
            audio_data = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio_data)
            words = text.split()
            for word in words:
                print(word)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand the audio.")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        keyboard.wait("1")
        print("Recording stopped. Press '0' to start recording again.")

transcribe_audio()
