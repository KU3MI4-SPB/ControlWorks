import csv
from note import Note
from datetime import datetime

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    current_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("Control_Work_2/notes.csv", "r") as csvfile:  
        reader = csv.reader(csvfile, delimiter=";")
        notes = list(reader)
    
    note_id = str(len(notes) + 1) 
    
    note = Note(note_id, title, body, current_datetime)
    
    with open("Control_Work_2/notes.csv", "a", newline="") as csvfile: 
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow([note.id, note.title, note.body, note.datetime])
        
    print("Заметка успешно создана.")

def read_notes():
    with open("Control_Work_2/notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        for row in reader:
            print(f"ID: {row[0]}\nЗаголовок: {row[1]}\nТекст: {row[2]}\nДата/время: {row[3]}\n")

def edit_note():
    note_id = input("Введите ID заметки для редактирования: ")
    new_title = input("Введите новый заголовок заметки: ")
    new_body = input("Введите новый текст заметки: ")
    new_datetime = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    with open("Control_Work_2/notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        notes = list(reader)
        
    found = False
    count = 0
    with open("Control_Work_2/notes.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for note in notes:
            if note[0] == note_id:
                writer.writerow([note_id, new_title, new_body, new_datetime])
                found = True
                count += 1
            else:
                writer.writerow(note)
                
    if count > 0:
        print("Заметка успешно отредактирована.")
    else:
        print("Заметка с данным ID не найдена.")

def delete_note():
    note_id = input("Введите ID заметки для удаления: ")
    
    with open("Control_Work_2/notes.csv", "r") as csvfile:
        reader = csv.reader(csvfile, delimiter=";")
        notes = list(reader)
        
    found = False
    count = 0
    with open("Control_Work_2/notes.csv", "w", newline="") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        for note in notes:
            if note[0] != note_id:
                writer.writerow(note)
            else:
                found = True
                
    if count > 0:
        print("Заметка успешно удалена.")
    else:
        print("Заметка с данным ID не найдена.")