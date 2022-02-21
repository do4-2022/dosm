from tkinter import Frame
from integrator import base_frame
from home.base_summary_frame import BaseSummaryFrame
from config import NB_OF_MINI_FRAME


class TabFrame(base_frame.BaseFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.summary_frames = []
        self.name = 'Accueil'
        
    def show(self):
        # grid
        grid_frame = Frame(self)

        # create mini frames
        for _ in range(NB_OF_MINI_FRAME + 1):
            summary_frame = BaseSummaryFrame(grid_frame, self.logger)
            self.summary_frames.append(summary_frame)
            summary_frame.show()

        # fill the grid
        index = 0
        for r in range(3):
            for c in range(3):
                self.summary_frames[index].grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
                index += 1
                grid_frame.grid_rowconfigure(r, weight=1)
                grid_frame.grid_columnconfigure(c, weight=1)

        grid_frame.pack(fill="both", expand=True)

    def update(self, dt):
        for summary_frame in self.summary_frames:
            summary_frame.update(dt)

    def hide(self):
        for summary_frame in self.summary_frames:
            summary_frame.hide()
