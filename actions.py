from main import Note

from collections import namedtuple

actions = []


def action(aliases):
    def decorator(func):
        Action = namedtuple('Action', 'key aliases func')
        actions.append(Action(aliases[0], aliases, func))

        def inner(*args, **kwargs):
            func(*args, **kwargs)

        return inner

    return decorator


@action(aliases=('add', 'a', 'append'))
def add_note(notes_instance):
    title = input('Title: ')
    time = t if ((t := input('Time (leave empty for None): ')) != '') else None
    desc = d if ((d := input('Description (leave empty for None): ')) != '') else None
    notes_instance.add(Note(title, time, desc))


@action(aliases=('remove', 'r', 'rem'))
def remove_note(notes_instance):
    query = str(input('Note to be deleted (number will act as index): '))
    notes_instance.remove(notes_instance.get_from_string(query))


@action(aliases=('help', 'h', 'actions'))
def print_actions():
    print(f'Available commands: {", ".join(act.key for act in actions)}')

