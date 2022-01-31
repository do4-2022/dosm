#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk


def main():
    root_window = tk.Tk()
    root_window.title('DOSM')

    notebook = ttk.Notebook(root_window)
    notebook.pack()

    frames = []

    for frame in frames:
        notebook.add(frame['widget'], text=frame['name'])

    root_window.mainloop()


if __name__ == '__main__':
    main()