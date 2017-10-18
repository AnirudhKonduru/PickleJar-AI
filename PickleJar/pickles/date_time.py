from YaVa.Senses.stt import listen
from YaVa.Senses.tts import say

import random
from datetime import datetime
triggers = {

'datefunc':[['what', 'date']]

}


def datefunc(s):
    print(str(datetime.now().date()))
    return str(datetime.now().date().strftime('%A %d %B %Y'))
