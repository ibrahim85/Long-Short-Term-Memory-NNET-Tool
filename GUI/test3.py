#!/usr/bin/python
"""
- read output from a subprocess in a background thread
- show the output in the GUI
"""
import sys
from itertools import islice
from subprocess import Popen, PIPE
from textwrap import dedent
from threading import Thread
import time

try:
    from Tkinter import *
    import Tkinter as tk
    from Queue import Queue, Empty
except ImportError:
    import tkinter as tk # Python 3
    from queue import Queue, Empty # Python 3

def iter_except(function, exception):
    """Works like builtin 2-argument `iter()`, but stops on `exception`."""
    try:
        while True:
            yield function()
    except exception:
        return

class DisplaySubprocessOutputDemo:
    def __init__(self, root):
        self.root = root


        self.process = Popen([sys.executable,"neural1.py"], stderr=PIPE, stdout=PIPE)

        # launch thread to read the subprocess output
        #   (put the subprocess output into the queue in a background thread,
        #    get output from the queue in the GUI thread.
        #    Output chain: process.readline -> queue -> label)
        q = Queue()  # limit output buffering (may stall subprocess)
        t = Thread(target=self.reader_thread, args=[q])
        t.daemon = True # close pipe if GUI process exits
        t.start()

        self.root.pack()
        self.update(q) # start update loop

    def reader_thread(self, q):
        """Read subprocess output and put it into the queue."""
        try:
            for line1 in iter(self.process.stderr.readline, b''):
                q.put(line1)
                #q.put(line2)
        finally:
            q.put(None)

    def update(self, q):
        """Update GUI with items from the queue."""
        for line in iter_except(q.get_nowait, Empty): # display all content
            if line is None:
                #time.sleep(5)
                #self.root.delete(1.0, END)
                #self.quit()
                return
            else:
                #self.label['text'] = line # update GUI
                self.root.insert(END, line)
                break # display no more than one line per 40 milliseconds
        self.root.after(40, self.update, q) # schedule next update

    def quit(self):
        self.process.kill() # exit subprocess if GUI is closed (zombie!)
        self.root.destroy()



root = Tk()
text = tk.Text(root)
app = DisplaySubprocessOutputDemo(text)
#root.protocol("WM_DELETE_WINDOW", app.quit)
# center window
#root.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))
root.mainloop()
