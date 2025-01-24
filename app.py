import os
import sys
from datetime import datetime

def analyze_directory(path="/"):
    # Количество файлов
    num_files = sum(len(files) for _, _, files in os.walk(path))

    # Топ-10 файлов по размеру
    all_files = []
    for root, _, files in os.walk(path):
        for file in files:
            try:
                filepath = os.path.join(root, file)
                size = os.path.getsize(filepath) / 1024  # Размер в Кб
                all_files.append((filepath, size))
            except Exception:
                continue
    top_files = sorted(all_files, key=lambda x: x[1], reverse=True)[:10]

    # Вывод результатов
    print(f"\nКоличество файлов в {path}: {num_files}\n")
    print("Топ-10 файлов по размеру:")
    for i, (file, size) in enumerate(top_files, start=1):
        print(f"{i}. {file} - {size:.2f} Кб")

if __name__ == "__main__":
    name = sys.argv[1] if len(sys.argv) > 1 else "Пользователь"
    path = sys.argv[2] if len(sys.argv) > 2 else "/"

    print(f"Привет, {name}!")
    print(f"Текущее время: {datetime.now()}\n")

    analyze_directory(path)
