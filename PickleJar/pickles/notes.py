from Senses.stt import listen
from Senses.tts import say

from datetime import datetime

import sqlite3

triggers = {

    'take_note':[
        ['take','note'],
        ['write','note'],
        ['save', 'note'],
        ['note', 'down']
    ],

    'show_notes':[
        ['show', 'note'],
        ['show', 'notes'],
        ['print', 'notes']
    ]

}

conn = sqlite3.connect("notes.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS notes(username VARCHAR(8), date date, text text)")


def take_note(s):
    say("What would you like me to note down?")
    note = listen()
    resp = c.execute('INSERT INTO notes VALUES(?,?,?)', ("default", datetime.now().date(), note))
    conn.commit()
    conn.close()
    print(resp)
    return "note saved"


def show_notes(s):
    for row in conn.execute('SELECT * FROM notes ORDER BY username'):
        print("NOTE:", row)
        conn.close()
    return "displaying all notes"