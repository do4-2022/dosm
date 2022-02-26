from tkinter import Frame
from integrator import base_frame
from home import base_summary_frame
from config import NB_OF_MINI_FRAME

from connected_users import summary_frame as cu_frame
from cpu import summary_frame as cpu_frame
from ipc import summary_frame as ipc_frame
# from memory import summary_frame as memory_frame
from net import summary_frame as net_frame
from ports import summary_frame as ports_frame
# from process import summary_frame as process_frame


class TabFrame(base_frame.BaseFrame):
    def __init__(self, master, logger, **options):
        super().__init__(master, logger, **options)
        self.logger = logger
        self.summary_frames = []
        for i in range(NB_OF_MINI_FRAME + 1):
            self.summary_frames.append(None)
        self.name = 'Home'
        
    def show(self):
        # grid
        grid_frame = Frame(self)

        self.summary_frames[0] = ipc_frame.SummaryFrame(grid_frame, self.logger)
        # self.summary_frames.append(memory_frame.SummaryFrame(grid_frame, self.logger))
        self.summary_frames[1] = cpu_frame.SummaryFrame(grid_frame, self.logger)
        self.summary_frames[2] = cu_frame.SummaryFrame(grid_frame, self.logger)
        self.summary_frames[3] = net_frame.SummaryFrame(grid_frame, self.logger)
        self.summary_frames[4] = ports_frame.SummaryFrame(grid_frame, self.logger)

        # init summary frames
        for i in range(NB_OF_MINI_FRAME + 1):
            if i > 4:
                summary_frame = base_summary_frame.BaseSummaryFrame(grid_frame, self.logger)
                self.summary_frames[i] = summary_frame
            else:
                self.summary_frames[i].show()
        

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
