from YaVa.Senses.stt import listen
from YaVa.Senses.tts import say

import random

triggers = {

'who_are_you':[['who','are','you'], ['your', 'name']]

}


def who_are_you(s):
    resp=[
    "Hi, I'm Pickle Bot",
    "My name is Pickle Bot"
    ]
    return random.choice(resp)


def what_are_you(s):
    resp=[
        "I'm a modular AI"
    ]
    return random.choice(resp)
