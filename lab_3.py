import tkinter as tk
from tkinter import filedialog
import datetime
import csv
import json

now = datetime.datetime.now()
local_now = now.astimezone()
local_tz = local_now.tzinfo

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Etiam sit amet suscipit mi, non porttitor mauris. Aliquam in lorem risus. Proin mauris mauris, varius ac vulputate sed, tempor nec lacus. Morbi sodales turpis in placerat semper. Donec bibendum blandit ante sit amet hendrerit.'
notes = []

def submit():
    global notes
    created = datetime.datetime.now()
    title = note_title.get()
    text = note_text.get('1.0', 'end').strip('\n')
    meta = f'created {created}, {local_tz}'
    note_dict = {'title': title, 'text': text, 'meta': meta}
    notes.append(note_dict)
    print(title)
    print(text)
    print(meta)
    return note_dict

def open_file():
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\andynguyen\\INST 326 Notes",
                                          filetypes=[("text files", "*.txt"),
                                                     ("csv files", "*.csv"),
                                                     ("all files", "*.*")])
    if filepath:
        with open(filepath, "r") as file:
            file_list = file.read().split('\n')
            note_title.delete(0, 'end')
            note_text.delete('1.0', 'end')
            note_title.insert(0, file_list[0])
            note_text.insert('1.0', file_list[1])
            meta = file_list[2]
            print(meta)

def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\andynguyen\\INST 326 Notes",
                                     defaultextension=".txt",
                                     title="Save File",
                                     filetypes=[("text file", ".txt"), ("all files", ".*")])
    if file:
        note = submit()
        filetext = f"{note['title']}\n{note['text']}\n{note['meta']}\n"
        file.write(filetext)
        file.close()

root = tk.Tk()
root.geometry("600x400")
root.title('Note Form')
root.config(bg='light gray')

title_label = tk.Label(root, bg='light gray', text='Note Title:')
title_label.grid(padx=10, pady=10, row=1, column=0, sticky='e')

text_label = tk.Label(root, bg='light gray', text='Note Text:')
text_label.grid(padx=10, pady=10, row=2, column=0, sticky='e')

note_title = tk.Entry(root, width=80)
note_title.grid(padx=10, pady=10, row=1, column=1, sticky='w')
note_title.insert(0, 'New note title')

note_text = tk.Text(root, height=10, width=60)
note_text.grid(padx=10, pady=10, row=2, column=1)
note_text.insert('1.0', lorem)

b1 = tk.Button(root, text='Submit', command=submit)
b1.grid(padx=10, pady=10, row=6, column=1, sticky='w')

b2 = tk.Button(root, text='Open File', command=open_file)
b2.grid(padx=10, pady=10, row=5, column=1, sticky='w')

b3 = tk.Button(root, text='Save File', command=save_file)
b3.grid(padx=10, pady=10, row=5, column=0)

b4 = tk.Button(root, text='Quit', command=root.destroy)
b4.grid(padx=10, pady=10, row=6, column=0)

root.mainloop()

print(notes)

# Save as a text file
with open("notes1.txt", "w") as f:
    for note in notes:
        f.write(f"{note['title']}\n{note['text']}\n{note['meta']}\n")

# Read from the text file
new_notes = []
with open('notes1.txt', 'r') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 3):
        title = lines[i].strip()
        text = lines[i + 1].strip()
        meta = lines[i + 2].strip()
        new_notes.append({'title': title, 'text': text, 'meta': meta})

# Save as a CSV file
with open("notes1.csv", "w", newline='') as csvfile:
    fieldnames = ['title', 'text', 'meta']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for note in notes:
        writer.writerow(note)

# Read from the CSV file
new_notes_csv = []
with open("notes1.csv", "r", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        new_notes_csv.append(row)
    print(new_notes_csv)

# Save as a JSON file
with open('notes1.json', 'w') as jsonfile:
    json.dump(notes, jsonfile)

# Read from the JSON file
with open('notes1.json', 'r') as jsonfile:
    new_notes_json = json.load(jsonfile)
