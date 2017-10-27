from Senses.input import listen
from Senses.output import say

from datetime import datetime

import sqlite3
import time

triggers = {

    'take_note': [
        ['take', 'note'],
        ['write', 'note'],
        ['save', 'note'],
        ['take', 'notes'],
        ['write', 'notes'],
        ['save', 'notes'],
        ['note', 'down']
    ],

    'show_notes': [
        ['show', 'note'],
        ['show', 'notes'],
        ['print', 'notes']
    ],

    'tell_notes': [
        ['tell', 'note'],
        ['tell', 'notes']
    ]
}

conn = sqlite3.connect('notes.db')
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS notes(username VARCHAR(8), date date, text text)")

conn.commit()


def take_note(s):
    say("What would you like me to note down?")
    note = listen()
    resp = c.execute('INSERT INTO notes VALUES(?,?,?)', ("default", datetime.now().date(), note))
    conn.commit()
    print(resp)
    return "note saved"


def show_notes(s):
    for row in conn.execute('SELECT * FROM notes ORDER BY username'):
        print("NOTE:", row)
    return "displaying all notes"


def tell_notes(s):
    for row in conn.execute('SELECT text FROM notes ORDER BY username'):
        print(row)
        row=str(row)
        say(row)
        time.sleep(1)
        say("next note")
        time.sleep(1)
    return "end of notes"
