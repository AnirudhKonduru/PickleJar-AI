import speech_recognition as sr
import yaml

r = sr.Recognizer()

with open("config.yaml") as stream:
    config = yaml.load(stream)


def stt():
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
#        with open("recording.flac", "wb") as f:
#            f.write(audio.get_flac_data())

    text = ""
    try:
        text = r.recognize_google(audio)
        print("RECOGNISED: "+text)
    except sr.UnknownValueError:
        print("Failed to recognize Audio")
    except sr.RequestError as e:
        print("Failed to request from google SR; {0}".format(e))
    if text == "":
        return None
    return text


def listen():
    if config["input"] == "speech":
        return stt()
    else:
        return input().strip()
