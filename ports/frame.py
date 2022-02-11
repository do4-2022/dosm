from integrator import frame
import tkinter as tk


class PortTab (frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)


    def show(self):
        bluebutton = tk.Button(self, text="Blue", fg="blue")
        bluebutton.pack( side = tk.LEFT )

        
