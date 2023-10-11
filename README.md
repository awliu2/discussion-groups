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
$ python3 groups.py example_roster -a alex, ava
⚠️  WARNING: no exact match for alex found in the roster.
Did you mean Alex de Minaur?  [y/n]: y
✅  Removed Alex de Minaur from the roster.
⚠️  WARNING: no exact match for ava found in the roster.
        1: Ava Martinez
        2: Ava Thompson
Did you mean one of the above? choices -> [1/2/n]: 1
✅  Removed Ava Martinez from the roster.
Generating groups for 13 students
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Group # ┃ Manager        ┃ Recorder         ┃ Spokesperson   ┃ Extra Member     ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│    1    │ Aiden Clark    │ Sophia Davis     │ Noah Tran      │                  │
│    2    │ Lucas Turner   │ Isabella Johnson │ Emma Taylor    │                  │
│    3    │ Ethan Anderson │ Jackson Li       │ Mia Moore      │                  │
│    4    │ Mason Spencer  │ Ava Thompson     │ Charlotte Hong │ Olivia Rodriguez │
└─────────┴────────────────┴──────────────────┴────────────────┴──────────────────┘
```
