# Config
___
## NanoID
- `length` : The length of the returned id
- `alphabet` : A string of allowed characters used in generation

### Example

```python
config = {
    "alphabet": "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz",
    "length": 21,
}
```

___
## Snowflake
- `epoch` : The timestamp in seconds or ms since the unix epoch which represents the starting point for ids. 0 will use the unix epoch. A provided timestamp will take the place of the unix epoch and ids will be generated using ms since that timestamp when generating ids.

- `machine_id` : a unique number between 0 and 1023 representing the machine the ids are generated on. if set to 0 or None its will generate this id for you using the thread id and the machines uuid.


### Example
```python
config = {
    "epoch": 1543392060,
    "machine_id": 0,
}
```
___
## ULID
- `epoch` : An optional timestamp in seconds or ms since the unix epoch which represents the starting point for ids. 0 will use the unix epoch. A provided timestamp will take the place of the unix epoch and ids will be generated using ms since that timestamp when generating ids.


### Example
```python
config = {
    "epoch": 1543392060,
    "machine_id": 0,
}
```