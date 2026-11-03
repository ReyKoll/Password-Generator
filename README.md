# Password Generator

Кроссплатформенный генератор паролей: Python 3 + Tkinter (только стандартная библиотека).
Works on Windows, macOS and Linux without changes.

## Возможности

- Криптографически стойкая генерация через `secrets`
- Выбор наборов символов: lower case / UPPER CASE / цифры / спецсимволы
- Опция «исключить неоднозначные символы» (O/0, l/1, I, |, кавычки, зеркальные скобки)
- Гарантия минимум одного символа из каждой выбранной категории
- Длина от 6 до 64 символов
- Копирование в буфер обмена, сохранение в файл

## Запуск

```bash
python3 main.py
```

**Важно для macOS**: не используйте системный Python из CommandLineTools —
в нём Tcl/Tk 8.5.9, который не отрисовывает окно на современных macOS.
Нужен Python с python.org (или `brew install python-tk`):

```bash
python3.14 main.py   # python.org installer bundles modern Tcl/Tk
```

## Сборка (PyInstaller)

```bash
pip install pyinstaller
pyinstaller --windowed --onefile --name "Password Generator" --icon icon.icns main.py   # macOS
pyinstaller --windowed --onefile --name "Password Generator" --icon icon.ico main.py    # Windows
```

Готовый бандл появится в `dist/`.
