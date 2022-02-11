#!/usr/bin/env python3

from time import time
import tkinter as tk
from tkinter import ttk

import config


def update(root_window, frames, last_time):
    new_time = time()
    for frame in frames:
        frame['widget'].update(new_time - last_time)
    root_window.after(config.UPDATE_INTERVAL, update, root_window, frames, new_time)


def main():
    root_window = tk.Tk()
    root_window.title('DOSM')
    root_window.minsize(*config.MIN_WINDOW_SIZE)

    notebook = ttk.Notebook(root_window)
    notebook.pack()

    frames = []

    if not frames:
        error_label = tk.Label(notebook, text='No frame found')
        error_label.pack()

    for frame in frames:
        notebook.add(frame['widget'], text=frame['name'])

    root_window.after(config.UPDATE_INTERVAL, update, root_window, frames, time())
    root_window.mainloop()


if __name__ == '__main__':
    main()