import csv
import tkinter as tk
from tkinter import filedialog, messagebox

def txt_to_csv(input_filename, output_filename):
    with open(input_filename, 'r', encoding='utf-8') as txt_file, open(output_filename, 'w', newline='', encoding='utf-8-sig') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in txt_file:
            row = [cell.strip() for cell in line.split('\n')]
            csv_writer.writerow(row)

def convert_and_open():
    input_file = input_path.get()
    output_file = "output.csv"

    txt_to_csv(input_file, output_file)
    messagebox.showinfo("Успешно", "Конвертация завершена.")

    open_file = messagebox.askyesno("Открыть файл", "Хотите открыть сконвертированный файл?")
    if open_file:
        import os
        os.system(f"start excel {output_file}")

def browse_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        input_path.set(file_path)

app = tk.Tk()
app.title("Конвертер TXT в CSV")
app.geometry("300x100")

input_path = tk.StringVar()

input_label = tk.Label(app, text="Выберите файл TXT:")
input_label.pack()

input_entry = tk.Entry(app, textvariable=input_path)
input_entry.pack()

browse_button = tk.Button(app, text="Обзор...", command=browse_file)
browse_button.pack()

convert_button = tk.Button(app, text="Конвертировать", command=convert_and_open)
convert_button.pack()

app.mainloop()
