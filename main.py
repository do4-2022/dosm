#!/usr/bin/env python3

from time import time
import tkinter as tk
from tkinter import ttk

import config


def update(root_window, frames, dt):
    for frame in frames:
        frame['widget'].update()
    root_window.after(config.UPDATE_INTERVAL, update, root_window, frames, time() - dt)


def main():
    root_window = tk.Tk()
    root_window.title('DOSM')

    notebook = ttk.Notebook(root_window)
    notebook.pack()

    frames = []

    for frame in frames:
        notebook.add(frame['widget'], text=frame['name'])

    root_window.after(config.UPDATE_INTERVAL, update, root_window, frames, 0)
    root_window.mainloop()


if __name__ == '__main__':
    main()