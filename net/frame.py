from integrator.frame import DOSMFrame

class Tab(DOSMFrame):
    def __init__(self, logger):
        super().__init__(logger)

    def show(self):
        return super().show()

    def update(self, dt):
        return super().update(dt)

    def hide(self):
        return super().hide()