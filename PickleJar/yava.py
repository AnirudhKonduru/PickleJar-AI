import pickle
pickle.init()
from Senses.input import listen
from Senses.output import say
from process import process

import os, sys, pyaudio
from pocketsphinx.pocketsphinx import *
from sphinxbase.sphinxbase import *


modeldir = "/home/ani/penv/pickle/lib/python3.5/site-packages/pocketsphinx/model" #""~/penv/pickle/lib/python3.5/site-packages/pocketsphinx/model"
config = Decoder.default_config()
config.set_string('-hmm', os.path.join(modeldir, 'en-us'))
config.set_string('-dict', os.path.join(modeldir, 'cmudict-en-us.dict'))
config.set_string('-kws', 'command.list')

decoder = Decoder(config)

p = pyaudio.PyAudio()
stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True)
stream.start_stream()

# Process audio chunk by chunk. On keyword detected perform action and restart search
decoder = Decoder(config)
decoder.start_utt()
while True:
    buf = stream.read(1024)

    decoder.process_raw(buf, False, False)

    if decoder.hyp() is not None:
        print([(seg.word, seg.prob, seg.start_frame, seg.end_frame) for seg in decoder.seg()])
        print("Detected keyword, restarting search")
        #
        # Here you run the code you want based on keyword
        #
        say("What can I help you with?")
        s = listen()

        if s is None:
            say("come again?")
            s=listen()
        if s is None:
            say("Sorry, Could not understand")
            decoder.end_utt()
            decoder.start_utt()
            continue
        print("said "+s)
        response = process(s)
        if response is None:
            say("Could not understand " + s)
        else:
            say(response)
        decoder.end_utt()
        decoder.start_utt()
