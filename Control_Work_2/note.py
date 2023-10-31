import commands

class Note:
    def __init__(self, id, title, body, datetime):
        self.id = id
        self.title = title
        self.body = body
        self.datetime = datetime

def show_menu():
    print("Выберите действие:")
    print("1. Создать заметку")
    print("2. Просмотреть список заметок")
    print("3. Отредактировать заметку")
    print("4. Удалить заметку")
    print("5. Выйти")

def main():
    while True:
        show_menu()
        choice = input("Введите номер действия: ")

        if choice == "1":
            commands.create_note()
        elif choice == "2":
            commands.read_notes()
        elif choice == "3":
            commands.edit_note()
        elif choice == "4":
            commands.delete_note()
        elif choice == "5":
            print("Программа завершена.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()