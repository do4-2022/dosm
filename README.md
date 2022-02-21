# dosm
DOSM DevOps System Monitor (Not to be confused with BDSM) is a system monitoring tool writtent in python that tracks various system informations (CPU usage, Disk Usage etc..)

Currently integrated
- [ ] cpu
- [ ] disks
- [x] home
- [ ] last users
- [x] logged users
- [ ] memory
- [ ] network
- [x] ports
- [ ] process

## Worflow

Each person will work on his module. Everyone have to implements a package derived from the main frame. Those methods will be written in `./integrator/frame.py`.

** Works on our feature : **
1. Create a branch with the name : `module-functionnality` and move into :
```
   git branch <branch-name>
   git checkout <branch-name>
```
1. Create the 2 files `__init__.py` and `frame.py`
1. See your modifications in your `dev.py` file. This file will be ignore by commits

**Pushing your works**  
When you're done with your work, here are the step to push.
```bash
git fetch
git rebase origin/main #Get the last modifications from the main, 
```

If there are conflicts, check the file and fix the MC. Then continue the process until the rebase is completely done.
```bash
git rebase continue
```

Finally, save and push your work.
```bash
git add .
git commit -m "any modification done" # Describe here what you have done
git push
git merge <branch-name>
```

See conventionnals commits here : https://www.conventionalcommits.org/en/v1.0.0-beta.2/

### Logger

We will have two ways to communicate with the Logger :
- Metrics : Send a dictionnary / key->value object by the name of the metrics and the value. Te logger will retrieve the timestamp and write it on hi sown
Example : Chrome is consumming 54% CPU : ["cpu.chrome"][.54]

- Logs : Send a string with the name of the modul and the message

Methods :
- writeMetric
- readMetric
- readLog
- writeLog

## Testing

Please create a `dev.py` file at the root of this project. This file will not be saved through git.

Here is a classical example to test you're frame.

```python
# import tkinter (as tk is optional) and your frame
import tkinter as tk
from your_package import frame

# create a new window
window = tk.Tk()

# create a new frame from your custom class
a_frame_instance = frame.YouFrame(window, None)
a_frame_instance.pack()

# if you want you can test your frame methods like this
a_frame_instance.show() # for example

# run in event-driven mode. This line is blocking since the window is opened
window.mainloop()
```
