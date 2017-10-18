import speech_recognition as sr
r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
        with open("recording.flac", "wb") as f:
            f.write(audio.get_flac_data())

    try:
        text = r.recognize_google(audio)
        print("RECOGNISED: "+text)
        return str(text)
    except sr.UnknownValueError:
        print("Failed to recognize Audio")
    except sr.RequestError as e:
        print("Failed to request from google SR; {0}".format(e))
