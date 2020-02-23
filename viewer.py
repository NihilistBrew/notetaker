from colorama import init, Style, Fore

init(autoreset=True)


class Viewer:
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

    def view(self, note):
        title = self.title_format + self.note_marker + note.title
        time = self.time_format + ' (' + note.time + ')' if note.time else ''
        desc = ''.join(self.tab + self.desc_format + desc_line + '\n' for desc_line in note.desc) if note.desc else ''
        if desc: desc = desc[:-2] # Shave off last newline
        s = ''
        s += title + time
        s += self.__choose_newline() if note.desc else ''
        s += desc
        s += self.__choose_newline()

        return s

    def view_all(self, notes):
        s = ''.join(self.view(note) for note in notes) if notes else 'There are no notes here. Try adding one with "add"!'

        return s
