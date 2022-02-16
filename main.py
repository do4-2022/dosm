#!/usr/bin/env python3

from time import time
import tkinter as tk
from tkinter import ttk

from config import UPDATE_INTERVAL, MIN_WINDOW_SIZE
from home import frame as home_frame
from logger import factory, logger


def update(root_window, frames, last_time):
    new_time = time()
    for frame in frames:
        frame['widget'].update(new_time - last_time)
    root_window.after(UPDATE_INTERVAL, update, root_window, frames, new_time)


def main():
    root_window = tk.Tk()
    root_window.title('DOSM')
    root_window.minsize(*MIN_WINDOW_SIZE)

    notebook = ttk.Notebook(root_window)
    notebook.pack(fill='both', expand=True)

    logger_factory = factory.LoggerFactory()

    frames = [
        {
            'name': 'Accueil',
            'widget': home_frame.Tab(notebook, logger.Logger('home', logger_factory))
        }
    ]

    for frame in frames:
        frame['widget'].show()
        notebook.add(frame['widget'], text=frame['name'])

    root_window.after(UPDATE_INTERVAL, update, root_window, frames, time())
    root_window.mainloop()


if __name__ == '__main__':
    main()