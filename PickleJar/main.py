import pickle
pickle.init()
from Senses.input import listen
from Senses.output import say
from process import process


s = listen()
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
