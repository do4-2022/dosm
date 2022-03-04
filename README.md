# DOSM
DOSM for DevOps System Monitor is a system monitoring tool writtent in Python that tracks various system informations (CPU usage, Disk Usage etc..).

Currently integrated
- [x] cpu
- [ ] disks
- [x] home
- [x] ipc
- [x] last users
- [x] logged users
- [x] memory
- [x] network
- [x] ports
- [x] process

## Requirements

You need [Python 3](https://www.python.org/downloads/) and a GNU/Linux based OS to run this project.

All Python modules needed are [Tkinter](https://docs.python.org/fr/3/library/tkinter.html) and the ones listed in requirements.txt.

## Run locally

First clone this repository.

```bash
git clone git@github.com:do3-2021/dosm.git
```
or
```bash
git clone https://github.com/do3-2021/dosm.git
```

Then install requirements.

```bash
cd dosm
python3 -m pip install -r requirements.txt
```

Finally run the project.
```bash
./main.py
```
or
```bash
python3 main.py
```

## Worflow

Each person has worked on one module. Everyone had to implements a package derived from the base frame: `./integrator/base_frame.py`.

**Works on a feature :**

1. Create a branch with the name following the convention `module-functionnality` and checkout it.

```bash
git branch <branch-name>
git checkout <branch-name>
```

2. Create a new Python package with at least these files
   - `__init__.py`: used to mark a folder as Python package.
   - `summary_frame.py`: contains a SummarFrame class which will be displayed in home tab.
   - `tab_frame.py`: contains a TabFrame class which will be displayed as an independant tab in the window.

3. Test your modifications in a `dev.py` file that you can create at the root of this project. This file will be ignored by git.

**Pushing your works**

When you're done with your work, here are the step to push.

```bash
git fetch
git rebase origin/main 
```

If there are conflicts, check the file and fix the merge conflicts. Then continue the process until the rebase is completely done.

```bash
git rebase --continue
```

Finally, save and push your work.

```bash
git add .
git commit -m "any modification done" # Describe here what you have done
git push
git merge <branch-name>
```

See conventionnals commits here : https://www.conventionalcommits.org/en/v1.0.0-beta.2/

## Logger

One of us have implemented a Logger class to store debug messages.

A new logger is created for each `TabFrame`. These one can use their logger with `self.logger.write_log(message)`.

## Testing

Please create a `dev.py` file at the root of this project. This file will not be saved through git.

Here is a classical example to test you're frame.

```python
# import tkinter (as tk is optional) and your frame
import tkinter as tk
import time
from logger import logger, factory
from your_package import tab_frame

def update(window, frame, last_time):
   new_time = time.time()
   frame.update(new_time - last_time)
   window.after(1000, update, window, frame, new_time)

# create a new window
window = tk.Tk()

# create a new logger
logger_instance = logger.Logger('your_package', factory.LoggerFactory())

# create a new frame from your custom TabFrame class
frame_instance = tab_frame.TabFrame(window, logger_instance)
frame_instance.pack(fill=tk.BOTH, expand=True)

# if you want you can test your frame methods like this
frame_instance.show()

# call update periodically
window.after(1000, update, window, frame_instance, time.time())

# run in event-driven mode. This line is blocking since the window is opened
window.mainloop()
```
