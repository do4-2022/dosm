# Logger

This module includes all you need to add logging to our module.

## Example

```python
from integrator import frame
from logger.logger import Logger
from logger.level import LogLevel

class Tab (frame.DOSMFrame):
    def __init__(self, master, logger: Logger, **options):
        super().__init__(master, logger, **options)
        logger.write_log("This is a test line", level=LogLevel.WARN)
```

Output example : `[2022-02-11 15:05:32] [WARN] [my-module] This is a test line`

## Methods

### Logger::write_log

This methods write a log to the `log` destination with a level.

| Argument name | Argument type |  Argument default |  Argument description |
|-|-|-|-|
| message | String | `null` | The message of the log |
| level | LogLevel | `LogLevel.INFO` | The level of the log |

Example :

```python
logger.write_log("This is a test line", level=LogLevel.WARN)
```
