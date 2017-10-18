import os


def say(something):
    return os.system("espeak \""+something+" \"")