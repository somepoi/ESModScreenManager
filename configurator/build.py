"""
скрипт сборки в exe через PyInstaller

запуск:
    python build.py
"""

import os
import sys
import shutil
import subprocess
from pathlib import Path

print("Собираем configurator...")

# определяем разделитель для add-data (Windows=; Unix=:)
path_separator = ';' if sys.platform == 'win32' else ':'

# команда сборки
build_cmd = [
    "pyinstaller",
    "--clean",  # очистка предыдущих сборок
    "--name=configurator",
    "--windowed",  # без консоли
    "--onedir",  # одна папка, не один файл
    f"--add-data=example{path_separator}example",  # включаем файлы примеров
    f"--add-data=resources{path_separator}resources",  # включаем ресурсы
    "--hidden-import=tkinter",
    "--hidden-import=tkinter.ttk",
    "--hidden-import=tkinter.filedialog",
    "--hidden-import=tkinter.messagebox",
    "--collect-all=customtkinter",
    "--noconfirm",
    "main.py"
]

print("Команда:", " ".join(build_cmd))

# используем subprocess.run вместо os.system для лучшей обработки ошибок
result = subprocess.run(build_cmd, check=False)

if result.returncode != 0:
    print(f"\nОшибка сборки! Код возврата: {result.returncode}")
    sys.exit(result.returncode)

print("\nГотово!")
print("Папка с результатом: dist/configurator")
