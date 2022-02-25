# CLI

This program includes the cli for fetching logs from the console.

## Example

```bash
$ python cli/main.py show-files .

  ├ 2022-02-11-1.log (4KB)
  ├ 2022-02-11-2.log (639B)
  ├ 2022-02-11-3.log (639B)
  ├ 2022-02-11-4.log (639B)

```

## Commands

### get

This command show all the logs with the given level and the timestamp.

| Argument name | Argument type |  Argument default |  Argument description |
|-|-|-|-|
| path | String | `null` | Path to the root folder of dosm |
| start | DateTime | `null` | Start date of the logs |
| end | DateTime | `null` | End date of the logs |

| Option name | Option type |  Option default |  Option description |
|-|-|-|-|
| --level | String | `ALL` | Level of the logs to be displayed |

Example :

```python
python cli/main.py get . "2022-02-11" "2022-02-13" --level ERROR
```

### show-files

This command show all the logs files.

| Argument name | Argument type |  Argument default |  Argument description |
|-|-|-|-|
| path | String | `null` | Path to the root folder of dosm |

Example :

```python
python cli/main.py show-files path/to/folder
```

### version

This command show the version for the cli program.

Example :

```python
python cli/main.py version
```
