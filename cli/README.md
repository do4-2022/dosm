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
