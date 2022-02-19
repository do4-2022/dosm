# Mini Frame

This file explain all you need to add a mini frame to your module.

## Typical architecture
```bash
├── __pycache__
├── __init__.py
├── frame.py
├── mini_frame.py
```

## Example of mini_frame.py

### With multiple inheritance

Reuse your own Tab frame, so in must cases you don't need to rewrite update and hide methods

```python
from your_package import frame
from home import mini_frame

class MiniFrame(frame.YourTab, mini_frame.MiniFrame):
    def __init__(self, master, logger, **options):
      super().__init__(master, logger, **options)
    
    def show(self):
      ''' view of your mini frame '''
      pass
```

### With single inheritance
```python
from your_package import frame
from home import mini_frame

class MiniFrame(mini_frame.MiniFrame):
    def __init__(self, master, logger, **options):
      super().__init__(master, logger, **options)
    
    def show(self):
      ''' view of your mini frame '''
      pass
    
    def update(self):
      ''' your update implementation '''
      pass

    def hide(self):
      ''' your hide implementation '''
      pass
```
