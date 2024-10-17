import tkinter
from abc import ABC, abstractmethod

class NoteModel:
    def __init__(self):
        self._notes = [{'id': 1, 'text': 'Сижу на паре'}]

    def get_notes(self):
        return self._notes

    def add_note(self, text):
        next_id = self._get_last_id() + 1
        note = {'id': next_id, 'text': text}
        self._notes.append(note)

    def _get_last_id(self):
        max = self._notes[0]['id']
        for note in self._notes:
            if note['id'] > max:
                max = note['id']
        return max

    def delete_note(self, id):
        for note in self._notes:
            if note['id'] == id:
                self._notes.remove(note)


class AbstractView(ABC):
    @abstractmethod
    def render_notes(self, notes):
        pass

class ConsoleView(AbstractView):
    def render_notes(self, notes):
        for note in notes:
            print(f"{note['id']} - {note['text']}")

class GraphicView(AbstractView):
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title('Тестовое окошко')
        self.listbox = tkinter.Listbox(self.root, height=10, width=50)
        self.listbox.pack(padx=10, pady=10)

    def render_notes(self, notes):

        self.listbox.delete(0, 'end')
        for note in notes:
            text = f"{note['id']} --- {note['text']}"
            self.listbox.insert(tkinter.END, text)

            self.root.mainloop()

class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_notes(self):
        notes = self.model.get_notes()
        self.view.render_notes(notes)

    def add_note(self):
        text = input('Введи текст заметки: ')
        self.model.add_note(text)

    def delete_note(self):
        id = int(input('Введи номер заметки: '))
        self.model.delete_note(id)

model =  NoteModel()
graphic_view = GraphicView()
console_view = ConsoleView()
contr = Controller(model, console_view)

while True:
    print('\n\n1 - Посмотреть все заметки')
    print('2 - Добавить заметку')
    print('3 - Удалить заметку')
    print('q - Выйти\n')

    choice = input('Вибирай: \n')

    if choice == '1':
        contr.show_notes()
    elif choice == '2':
        contr.add_note()
    elif choice == '3':
        contr.delete_note()
    elif choice == 'q':
        break











            
