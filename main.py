import csv
import tkinter as tk
from tkinter import filedialog, messagebox
import os


def txt_to_csv(input_filename, output_filename, merge_from_row):
    with open(input_filename, 'r', encoding='utf-8') as txt_file, open(output_filename, 'w', newline='',
                                                                       encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        current_row = 1
        merged_line = ""

        for line in txt_file:
            if merge_from_row == 0:
                csv_writer.writerow([line.strip()])
            else:
                if current_row >= merge_from_row:
                    merged_line += line.strip()
                else:
                    csv_writer.writerow([line.strip()])
            current_row += 1

        if merge_from_row != 0 and merged_line:
            csv_writer.writerow([merged_line])


def convert_and_open(input_folder, merge_from_row):
    output_folder = "Converted CSVs"
    if not os.path.exists(output_folder):
        os.mkdir(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith(".txt"):
            input_file = os.path.join(input_folder, filename)
            output_file = os.path.join(output_folder, filename.replace(".txt", ".csv"))
            txt_to_csv(input_file, output_file, merge_from_row)

    messagebox.showinfo("Успешно", "Конвертация завершена.")


def browse_folder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        input_path.set(folder_path)


app = tk.Tk()
app.title("Конвертер TXT в CSV")
app.geometry("400x220")

input_path = tk.StringVar()
merge_from_row = tk.IntVar()

input_label = tk.Label(app, text="Выберите папку:")
input_label.pack()

input_entry = tk.Entry(app, textvariable=input_path)
input_entry.pack()

merge_label = tk.Label(app, text="Начать объединение со строки (0 - каждая строка в новой ячейке):")
merge_label.pack()

merge_entry = tk.Entry(app, textvariable=merge_from_row)
merge_entry.pack()

browse_button = tk.Button(app, text="Обзор...", command=browse_folder)
browse_button.pack()

convert_button = tk.Button(app, text="Конвертировать",
                           command=lambda: convert_and_open(input_path.get(), merge_from_row.get()))
convert_button.pack()

app.mainloop()
