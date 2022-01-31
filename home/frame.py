from tkinter import Tk, Frame, Label
from integrator import frame

class Tab(frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.logger = logger

    def show(self):
        mainframe=Frame(self.master, bg="red")
        mainframe.pack(fill="both", expand=True)

        title=Label(mainframe,text="Home", bg="black", fg="white", padx=5, pady=5)
        title.config(font=("Arial", 24))
        title.pack(fill="x")

        grid_frame=Frame(mainframe)
        for r in range(3):
            for c in range(3):
                label=Label(grid_frame, text="Item", bg="red", fg="white", padx=5, pady=5)
                label.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
                grid_frame.grid_rowconfigure(r, weight=1)
                grid_frame.grid_columnconfigure(c, weight=1)

        grid_frame.pack(fill="both", expand=True)

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        pass

    def hide(self):
        pass
