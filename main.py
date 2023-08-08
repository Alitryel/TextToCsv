import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import os

def txt_to_csv(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as txt_file, open(output_filename, 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in txt_file:
            row = [cell.strip() for cell in line.split('\n')]
            csv_writer.writerow(row)

def convert_and_open(input_folder):
    output_folder = "Converted CSVs"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".txt", ".csv"))
            txt_to_csv(input_file, output_file)

    messagebox.showinfo("Успешно", "Конвертация завершена.")

def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        input_path.set(folder_path)

app = tk.Tk()
app.title("Конвертер TXT в CSV")
app.geometry("300x150")  # Увеличенный размер окна

input_path = tk.StringVar()

input_label = tk.Label(app, text="Выберите папку:")
input_label.pack()

input_entry = tk.Entry(app, textvariable=input_path)
input_entry.pack()

browse_button = tk.Button(app, text="Обзор...", command=browse_folder)
browse_button.pack()

convert_button = tk.Button(app, text="Конвертировать", command=lambda: convert_and_open(input_path.get()))
convert_button.pack()

app.mainloop()
