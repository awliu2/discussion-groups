## python script to generate groups for cs141 discussion sections

```
usage: groups.py [-h] [--absent ABSENT [ABSENT ...]] filename

Randomly assign groups for discussion sections

positional arguments:
  filename              txt file containing student names (one per line), required argument

options:
  -h, --help            show this help message and exit
  --absent ABSENT [ABSENT ...]
                        comma separated list of absent students to exclude from group generation
```

## example

```
$ python3 groups.py example_roster -a Olivia
⚠️  WARNING: no exact match for alex found in the roster.
Did you mean Alex de Minaur?  [y/n]: y
✅  Removed Alex de Minaur from the roster.
⚠️  WARNING: no exact match for charlotte found in the roster.
        1: Charlotte Spencer
        2: Charlotte Hong
Did you mean one of the above? choices -> [1/2/n]: 2
✅  Removed Charlotte Hong from the roster.
Generating groups for 13 students
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Group # ┃ Manager          ┃ Recorder       ┃ Spokesperson      ┃ Extra Member ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│    1    │ Mia Moore        │ Ethan Anderson │ Aiden Clark       │              │
│    2    │ Emma Taylor      │ Jackson Li     │ Charlotte Spencer │              │
│    3    │ Noah Tran        │ Lucas Turner   │ Olivia Rodriguez  │              │
│    4    │ Isabella Johnson │ Ava Martinez   │ Liam Thompson     │ Sophia Davis │
└─────────┴──────────────────┴────────────────┴───────────────────┴──────────────┘
```
