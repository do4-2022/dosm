from integrator import base_frame


class BaseSummaryFrame(base_frame.BaseFrame):
    def __init__(self, master, logger, **options):
      super().__init__(master, logger, width=300, height=250, borderwidth=10, highlightbackground="#5D55C1", highlightthickness=1, **options)
