import os
import yaml

with open("config.yaml") as stream:
    config = yaml.load(stream)


def tts(something):
    return os.system("espeak \""+something+" \" > /dev/null 2>&1")


def say(something):
    if config["output"] == "speech":
        return tts(something)
    else:
        print(something)
