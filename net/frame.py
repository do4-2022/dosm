from integrator.frame import DOSMFrame

import psutil

#TODO
#   -combo list with interfaces
#   -draw switchband usage and find a library to do so..

class Tab(DOSMFrame):
    def __init__(self, logger):
        self.interfaces = psutil.net_if_addrs()
        self.interfaces.pop('lo')
        print("some cool logger passing to super")

    def show(self):
        return super().show()

    def update(self, dt):
        return super().update(dt)

    def hide(self):
        return super().hide()