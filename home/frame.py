from tkinter import Frame
from integrator import frame
from home.mini_frame import MiniFrame
from config import NB_OF_MINI_FRAME

class Tab(frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.mini_frames = []
        self.name = 'Accueil'
        
    def show(self):
        # grid
        grid_frame = Frame(self)

        # create mini frames
        for _ in range(NB_OF_MINI_FRAME + 1):
            mini_frame = MiniFrame(grid_frame, self.logger)
            self.mini_frames.append(mini_frame)
            mini_frame.show()

        # fill the grid
        index = 0
        for r in range(3):
            for c in range(3):
                self.mini_frames[index].grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
                index += 1
                grid_frame.grid_rowconfigure(r, weight=1)
                grid_frame.grid_columnconfigure(c, weight=1)

        grid_frame.pack(fill="both", expand=True)

    def update(self, dt):
        for mini_frame in self.mini_frames:
            mini_frame.update(dt)

    def hide(self):
        for mini_frame in self.mini_frames:
            mini_frame.hide()
