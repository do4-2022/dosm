from tkinter import Frame, Label
from integrator import frame
from home.mini_frame import MiniFrame


NB_OF_MINI_FRAME = 9

class Tab(frame.DOSMFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.logger = logger
        self.mini_frames = []
        
    def show(self):
        # main frame
        mainframe = Frame(self.master, bg='white')
        mainframe.pack(fill="both", expand=True)

        # grid
        grid_frame = Frame(mainframe)

        # create mini frames
        for _ in range(NB_OF_MINI_FRAME + 1):
            self.mini_frames.append(MiniFrame(grid_frame, self.logger))

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
        """
        `dt` is the elapsed delta time since the last update in second
        """
        for i in len(self.mini_frames):
            self.mini_frames[i].update(dt)

    def hide(self):
        for i in len(self.mini_frames):
            self.mini_frames[i].hide()
