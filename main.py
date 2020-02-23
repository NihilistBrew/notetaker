import yaml
from colorama import init, Style, Fore

init(autoreset=True)


class Note:
    def __init__(self, title, time, desc):
        self.title = title
        self.time = time if time else ''
        self.desc = desc


class Notes:
    notes = []


class Interface:
    def __init__(self,
                 title_format=Style.BRIGHT,
                 time_format=Style.DIM,
                 desc_format=Style.NORMAL,
                 note_marker='[*] ',
                 tab=None,
                 compact=False):

        self.title_format = title_format
        self.time_format = time_format
        self.desc_format = desc_format
        self.note_marker = note_marker
        self.tab = tab if tab else ' ' * len(note_marker)
        self.compact = compact

    def __choose_newline(self):
        return '\n\n' if not self.compact else '\n'

    def view(self, note, should_print=True):
        title = self.title_format + self.note_marker + note.title
        time = self.time_format + note.time
        desc = ''.join(self.tab + self.desc_format + desc_line + '\n' for desc_line in note.desc)
        s = ''
        s += f'{title} ({time})'
        s += self.__choose_newline()
        s += desc
        s += self.__choose_newline()

        if should_print:
            print(s)
        else:
            return s

    def view_all(self, notes, should_print=True):
        s = ''.join(self.view(note, should_print=False) for note in notes)

        if should_print:
            print(s)
        else:
            return s


class InputHandler:
    def __get_desc(self, s):
        return s.split('; ')

    def add_note(self, notes):
        title = input('Title: ')
        time = t if ((t := input('Time: ')) != '') else None
        desc = self.__get_desc(input('Description: '))
        notes.append(Note(title, time, desc))

    def remove_note(self, notes, query):
        if query.isdigit():  # Assume the input is an index
            del notes[int(query)]
        else:  # Assume the input (note) is a title
            for i in notes[:]:
                if i.title == query:
                    notes.remove(i)

    def input_loop(self):
        pass

notes = Notes.notes

ih = InputHandler()
#ih.add_note(notes)

notes.append(Note('Test title', '15:30', ['this is', 'a test', 'description']))

ih.remove_note(notes, '0')

interface = Interface()
interface.view_all(notes)
