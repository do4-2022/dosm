import json
import os
import tkinter as tk

from os import path as op
from pathlib import Path
from PIL import Image, ImageTk
from tkinter import ttk
from time import time

from config import MIN_WINDOW_SIZE, UPDATE_INTERVAL
from connected_users import tab_frame as cu_frame
from cpu import tab_frame as cpu_frame
from home import tab_frame as home_frame
from ipc import tab_frame as ipc_frame
from login_history import tab_frame as lh_frame
from net import tab_frame as net_frame
from ports import tab_frame as ports_frame
from process import tab_frame as process_frame
from logger import factory, logger
from memory import tab_frame as memory_frame


class Integrator:
    def __init__(self):
        """ Init a new Integrator. A logger, a window, a notebook and tabs are created here. """
        # Create a new logger for the gui
        self.logger_factory = factory.LoggerFactory()
        self.logger = logger.Logger('integrator', self.logger_factory)
        self.logger.write_log('Creating main gui...')

        # Create the window
        self.window = tk.Tk()
        self.window.title('DOSM')
        self.window.minsize(*MIN_WINDOW_SIZE)

        image = Image.open('images/icon.png')
        photo = ImageTk.PhotoImage(image)
        self.window.wm_iconphoto(False, photo)

        # Create the notebook to display tabs
        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(fill='both', expand=True)

        self.logger.write_log('Done')
        self.logger.write_log('Creating tabs...')

        # Create the tabs
        self.tabs = [
            home_frame.TabFrame(self.notebook, logger.Logger('home', self.logger_factory)),
            ipc_frame.TabFrame(self.notebook, logger.Logger('ipc', self.logger_factory)),
            cu_frame.TabFrame(self.notebook, logger.Logger('connected_users', self.logger_factory)),
            cpu_frame.TabFrame(self.notebook, logger.Logger('cpu', self.logger_factory)),
            lh_frame.TabFrame(self.notebook, logger.Logger('login_history', self.logger_factory)),
            net_frame.TabFrame(self.notebook, logger.Logger('net', self.logger_factory)),
            ports_frame.TabFrame(self.notebook, logger.Logger('ports', self.logger_factory)),
            process_frame.TabFrame(self.notebook, logger.Logger('process', self.logger_factory)),
            memory_frame.TabFrame(self.notebook, logger.Logger('memory', self.logger_factory)),
            
        ]

        for tab in self.tabs:
            self.notebook.add(tab, text=tab.name)

        self.logger.write_log('Done')

        # Bind notebook tab changed event to select_tab method
        self.selected_tab = 0
        self.notebook.bind('<<NotebookTabChanged>>', self.on_select_tab)

        self.load()

    def update(self, last_time: float):
        """ Update the integrator.
            
        `last_time` (float): The time before the last call of this method. """
        new_time = time()
        for tab in self.tabs:
            tab.update(new_time - last_time)
        self.window.after(UPDATE_INTERVAL, self.update, new_time)

    def on_select_tab(self, event):
        """ Hide current tab and show the selected one.
        
        `event` (VirtualEvent): A notebook virtual event. """
        if self.tabs[self.selected_tab].shown:
            self.tabs[self.selected_tab].hide()
        
        self.selected_tab = self.notebook.index(self.notebook.select())
        
        if not self.tabs[self.selected_tab].shown:
            self.tabs[self.selected_tab].show()

        self.save()

    def select_tab(self, tab_index):
        """ Select a tab with a specific `tab_index` """
        self.notebook.select(self.notebook.tabs()[tab_index])
    
    def run(self):
        """ Run the window mainloop. """
        self.window.after(UPDATE_INTERVAL, self.update, time())
        self.window.mainloop()

    def save(self):
        """ Save the integrator states. """
        home_folder = Path.home()
        conf_folder = home_folder / '.dosm'
        
        self.logger.write_log('Saving states...')

        if not op.exists(conf_folder):
            os.mkdir(conf_folder)

        if not op.isdir(conf_folder):
            msg = f'Unable to save states: "{conf_folder}" is not a folder'
            self.logger.write_log(msg)
            return
        
        with open(conf_folder / 'integrator_state.json', 'w') as file:
            file.write(json.dumps({'selected_tab': self.selected_tab}))
        
        self.logger.write_log('Done')

    def load(self):
        """ Load the integrator states. """
        home_folder = Path.home()
        conf_file = home_folder / '.dosm' / 'integrator_state.json'
        
        self.logger.write_log('Loading states...')

        if not op.exists(conf_file):
            return 
        
        if not op.isfile(conf_file):
            msg = f'Unable to load states: "{conf_file}" is not a file'
            self.logger.write_log(msg)
            return
        
        try:
            with open(conf_file, 'r') as file:
                self.select_tab(int(json.load(file).get('selected_tab', 0)))
        except Exception as e:
            self.logger.write_log('Unable to load "selected_tab" from states')
        else:
            self.logger.write_log('Done')
