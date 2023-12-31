import argparse

from time import sleep
from random import shuffle

from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt

from thefuzz import fuzz


WARNING_MSG = ":warning-emoji:  WARNING: no exact match for {} found in the roster."
REMOVED_MSG = ":white_check_mark:  Removed {} from the roster."


def get_close_matches(absentee, students, thres=60):
    res = []

    for student in students:
        space_idx = student.index(" ")

        # first name is everything before the first space
        first_name, last_name = student[:space_idx], student[space_idx + 1:]

        if (fuzz.ratio(absentee, student) >= thres or
            fuzz.ratio(absentee, first_name) >= thres or
            fuzz.ratio(absentee, last_name) >= thres):
            res.append(student)

    return res


def parse_absent_students(c, absent_list, students):
    """
    Removes absent students from the roster
    """

    # delimit on commas, and strip leading + trailing whitespace
    absent_list = [name.strip() for name in absent_list.split(",")]


    for absentee in absent_list:
        if absentee in students:
            students.remove(absentee)
            continue

        c.print(f"[yellow]{WARNING_MSG.format(absentee)}[/yellow]")

        matches = get_close_matches(absentee, students)

        if not matches:
            continue

        if len(matches) == 1:
            user_input = Prompt.ask(
                f"Did you mean {matches[0]}? [y/n]",
                show_choices=True,
                choices=["y", "n"],
            )
            if user_input == "y":
                students.remove(matches[0])
                c.print(f"[green]{REMOVED_MSG.format(matches[0])}[/green]")
                continue
            else:
                c.print(f"[yellow]Skipping {absentee}[/yellow]")
                continue

        for i, match in enumerate(matches):
            c.print(f"\t{i + 1}: {match}")

        user_input = Prompt.ask(
            f"Did you mean one of the above? choices ->",
            show_choices=True,
            choices=[str(i + 1) for i in range(len(matches))] + ["n"],
        )
        if user_input == "n":
            continue
        index = int(user_input) - 1
        students.remove(matches[index])
        c.print(f"[green]{REMOVED_MSG.format(matches[index])}[/green]")


def tabulate_groups(c, groups, extra_member):
    """
    Pretty prints the groups into a table using rich
    """
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Group #", style="dim", width=7, justify="center")
    table.add_column("Manager", justify="left")
    table.add_column("Recorder", justify="left")
    table.add_column("Spokesperson", justify="left")
    if extra_member:
        table.add_column("Extra Member", justify="left")
    for i, group in enumerate(groups):
        if "Extra Member" in group:
            table.add_row(
                str(i + 1),
                group["Manager"],
                group["Recorder"],
                group["Spokesperson"],
                group["Extra Member"],
            )
        elif "Manager" not in group:
            table.add_row(
                str(i + 1),
                "[grey15]None[/grey15]",
                group["Recorder"],
                group["Spokesperson"],
            )
        else:
            table.add_row(
                str(i + 1),
                group["Manager"],
                group["Recorder"],
                group["Spokesperson"],
            )
    c.print(table)


def main():
    """
    Main function

    Usage:
        python groups.py <filename> --absent <absent students>
    Options:
        filename: txt file containing student names (one per line)
        --absent, -a: list of absent students to exclude from group generation
        --help, "-h": show help message
    """
    c = Console()
    parser = argparse.ArgumentParser(
        description="Randomly assign groups for discussion sections"
    )
    parser.add_argument(
        "filename",
        type=str,
        help="path to a file containing student names (one per line)",
    )
    parser.add_argument(
        "--absent",
        "-a",
        default=[],
        nargs="+",
        help="comma separated list of absent students to exclude from group generation",
    )

    args = parser.parse_args()
    students = []

    with open(args.filename, "r") as f:
        for line in f:
            students.append(line.strip())

    if args.absent:
        parse_absent_students(c, " ".join(args.absent), students)

    # LOL just for memes
    sleep(1)

    print(f"Generating groups for {len(students)} students")
    shuffle(students)

    # LOL just for memes again
    sleep(1)

    groups = []
    i = 0
    extra_member = False

    while i < len(students):
        # creates a group of 4 if there's only 1 student left
        if i + 1 == len(students):
            extra_member = True
            groups[-1]["Extra Member"] = students[i]
            break

        group_of_two = i + 2 == len(students)
        # no manager role for groups of 2
        if group_of_two:
            group = {
                "Recorder": students[i],
                "Spokesperson": students[i + 1],
            }
        else:
            group = {
                "Manager": students[i],
                "Recorder": students[i + 1],
                "Spokesperson": students[i + 2]
            }
        groups.append(group)
        i += 3

    if group_of_two:
        c.print(
            f"[yellow]Group of 2: {group['Recorder']} and {group['Spokesperson']}[/yellow]"
        )

    tabulate_groups(c, groups, extra_member=extra_member)


if __name__ == "__main__":
    main()
