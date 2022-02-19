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

### Logger::create_logger

This method create a new logger with a name.

| Argument name | Argument type |  Argument default |  Argument description |
|-|-|-|-|
| name | String | `null` | The name of the logger |
| factory | LoggerFactory | `null` | The instance of the factory |

Example :

```python
logger = Logger.create_logger("hello", factory)
```

### Logger::write_log

This method write a log to the `log` destination with a level.

| Argument name | Argument type |  Argument default |  Argument description |
|-|-|-|-|
| message | String | `null` | The message of the log |
| level | LogLevel | `LogLevel.INFO` | The level of the log |

Example :

```python
logger.write_log("This is a test line", level=LogLevel.WARN)
```

## Integrate to the main module

First of all, you need to create the `LoggerFactory`.
The `LoggerFactory` load all the dependencies and open the log files needed for the logger.
With the factory, you will be able to create `Logger`.

There is an example :

```python
factory = LoggerFactory()
logger = Logger.create_logger("my-module", factory)
```

