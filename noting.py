import yaml
import os
import os.path


class Note:
    def __init__(self, title, time, desc):
        self.title = title
        self.time = time if time else ''
        self.desc = desc if isinstance(desc, list) or desc is None else desc.split('; ')  # Convert semi-colon-seperated desc to list.


class Notes:
    note_path = 'notes.yaml'

    @property
    def notes(self):
        if not os.path.isfile(self.note_path):
            open(self.note_path, 'w').close()

        with open(self.note_path, 'r') as f:
            yml = yaml.load(f, Loader=yaml.Loader)

            return [note for note in yml] if yml is not None else None

    @classmethod
    def save(cls, new_notes):
        with open(cls.note_path, 'w') as f:
            yaml.dump(new_notes, f)

    def add(self, note):
        new_notes = self.notes if isinstance(self.notes, list) else []
        new_notes.append(note)
        Notes.save(new_notes)

    def remove(self, note):
        old_notes = self.notes
        new_notes = [no for no in old_notes if no.title != note.title]
        Notes.save(new_notes)

    def get_from_string(self, s):
        if self.notes is None: return None
        if s.isdigit():
            try:
                return self.notes[int(s)]
            except IndexError:
                return None
        else:
            for note in self.notes:
                if note.title == s:
                    return note
            else:
                return None
