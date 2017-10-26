import sys
import yaml
from process import process

from Senses.stt import listen
from Senses.tts import say

s = listen()
#s="date"
print("said: "+s)
'''
while(s==None):
    say("come again?")
    s=listen()
'''
response = process(s)
if response is None:
    say("Could not understand "+s)
else:
    say(response)
