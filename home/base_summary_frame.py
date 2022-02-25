from integrator import base_frame


class BaseSummaryFrame(base_frame.BaseFrame):
    def __init__(self, master, logger, **options):
      super().__init__(master, logger, width=300, height=250, bg="#5D55C1", **options)
