from noting import Note, Notes

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
    title_done = False
    while not title_done:
        title = input('Title: ')
        if title == '':
            print('Note title cannot be empty!')
            continue  # Avoid the program trying to loop over NoneType later on
        elif notes_instance.get_from_string(title) is not None:
            print(f'Note "{title}" already exists!')
        else:  # All checks passed!
            title_done = True

    time = t if ((t := input('Time (leave empty for None): ')) != '') else None
    desc = d if ((d := input('Description (leave empty for None): ')) != '') else None
    notes_instance.add(Note(title, time, desc))


@action(aliases=('remove', 'r', 'rem'))
def remove_note(notes_instance):
    query = str(input('Note to be deleted (number will act as index): '))
    notes_instance.remove(notes_instance.get_from_string(query))


@action(aliases=('help', 'h', 'actions'))
def print_actions(**kwargs):
    print(f'Available actions: {", ".join(act.key for act in actions)}')


def get_user_action(notes_instance):
    s = str(input('> '))
    for action in actions:
        if s in action.aliases:
            action.func(notes_instance=notes_instance)
    else:
        print('Unrecognized action! Type "help" for available actions.')

