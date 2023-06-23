import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import csv
import psycopg2 #połączenie skryptu z bazą danych PostgreSQL
from jsonschema import validate #walidacja danych

folder_path = "C:\\Users\\Gaming\\Desktop\\Projects\\estate-marketplace\\ImportAndOutput"
schema = {
    "fields": [
        {"name": "column1", "type": "string", "required": True},
        {"name": "column2", "type": "integer", "required": True},
        {"name": "column3", "type": "float", "required": False},
    ]
}


def process_csv(file_path):
    # Walidacja pliku CSV
    with open(file_path, "r") as file:
        csv_data = file.read()
    try:
        validate(instance=csv_data, schema=schema)
        print("Plik CSV jest zgodny ze schematem.")

        # Odczyt danych z pliku CSV
        # Przykładowa implementacja
        with open(file_path, "r") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Pominięcie nagłówka pliku CSV, jeśli istnieje
            csv_data = []  #Stworzenie pustej listy - przechowuje dane odczytane z pliku CSV
            for row in csv_reader:
                csv_data.append(tuple(row))


        # Połączenie z bazą danych PostgreSQL
        conn = psycopg2.connect(
            database="postgres",
            user="postgres",
            password="pass",
            host="localhost",
            port="5432",
        )
        cursor = conn.cursor()

        # Zapis danych do bazy danych
        # Przykładowa implementacja
        query = "INSERT INTO table_name (column1, column2, column3) VALUES (%s, %s, %s)"
        cursor.executemany(query, csv_data)

        conn.commit()
        conn.close()

        print("Dane zostały zapisane do bazy danych.")
    except Exception as e:
        print("Błąd walidacji lub zapisu danych:", str(e))


class FolderEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory and event.src_path.endswith(".csv"):
            process_csv(event.src_path)


event_handler = FolderEventHandler()
observer = Observer()
observer.schedule(event_handler, folder_path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()

#ten skrypt waliduje plik CSV, odczytuje dane z pliku, łączy się z bazą danych PostgreSQL i zapisuje dane do określonej tabeli. Jeśli wszystko przebiegnie pomyślnie, dane zostaną załadowane do bazy danych.