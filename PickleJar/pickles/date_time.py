from Senses.input import listen
from Senses.output import say

import random
from datetime import datetime


triggers = {
    'date_func': [['what', 'date']]
}


def date_func(s):
    print(str(datetime.now().date()))
    say(str(datetime.now().date()))
    return str(datetime.now().date().strftime('%A %d %B %Y'))
