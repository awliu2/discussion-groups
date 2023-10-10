## python script to generate groups for cs141 discussion sections

```
usage: groups.py [-h] [--absent ABSENT [ABSENT ...]] filename

Randomly assign groups for discussion sections

positional arguments:
  filename              txt file containing student names (one per line), default: students.txt

options:
  -h, --help            show this help message and exit
  --absent ABSENT [ABSENT ...]
                        list of absent students to exclude from group generation
```

## example

```
$ python3 groups.py example_roster -a Olivia
⚠️ WARNING: no exact match for Olivia found in the roster.
Did you mean Olivia Rodriguez?  [y/n]: y
✅  Removed Olivia Rodriguez from the roster.
Generating groups for 13 students
┏━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┓
┃ Group # ┃ Manager        ┃ Recorder       ┃ Spokesperson     ┃ Extra Member ┃
┡━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━┩
│    1    │ Ethan Anderson │ Noah Tran      │ Isabella Johnson │              │
│    2    │ Lucas Turner   │ Ava Martinez   │ Mia Moore        │              │
│    3    │ Jackson Li     │ Liam Thompson  │ Mason Spencer    │              │
│    4    │ Emma Taylor    │ Charlotte Hong │ Sophia Davis     │ Aiden Clark  │
└─────────┴────────────────┴────────────────┴──────────────────┴──────────────┘

```
