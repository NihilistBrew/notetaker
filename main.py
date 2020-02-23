from noting import Notes
from viewer import Viewer
from actions import get_user_action


def main():
    running = True
    while running:
        viewer = Viewer()
        notes_obj = Notes()
        notes = Notes().notes
        print(viewer.view_all(notes))
        get_user_action(notes_obj)


if __name__ == '__main__':
    main()