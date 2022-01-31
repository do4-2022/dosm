from tkinter import Tk, Frame, Label
from integrator import frame

class Tab(frame.DOSMFrame):
    def show(self):
        pass

    def update(self, dt):
        """
        `dt` is the elapsed delta time since the last update in second
        """
        pass

    def hide(self):
        pass

homeWindow = Tk()

mainframe=Frame(homeWindow, bg="red")
mainframe.pack(fill="both", expand=True)

title=Label(mainframe,text="Home", bg="black", fg="white", padx=5, pady=5)
title.config(font=("Arial", 24))
title.pack(fill="x")

# verticalFrame=Frame(mainframe,bg="blue")
# item1=Label(verticalFrame,text="Item 1",bg="orange",padx=10,pady=10,fg="blue").pack(fill="x",padx=10,pady=10)
# item2=Label(verticalFrame,text="Item 2",bg="yellow",padx=10,pady=10,fg="black").pack(fill="x",padx=10,pady=10)
# verticalFrame.pack(fill="x")

# label=Label(mainframe,text="Grid Frame Example",bg="black",fg="white",padx=5,pady=5)
# label.config(font=("Arial",18))
# label.pack(fill="x")

grid_frame=Frame(mainframe)
for r in range(3):
    for c in range(3):
        label=Label(grid_frame, text="Item", bg="red", fg="white", padx=5, pady=5)
        label.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")
        grid_frame.grid_rowconfigure(r, weight=1)
        grid_frame.grid_columnconfigure(c, weight=1)

grid_frame.pack(fill="both", expand=True)


homeWindow.mainloop()