"""Password Generator — cross-platform (Windows / macOS / Linux), Tkinter + secrets."""

import os
import secrets
import sys
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

LOWER = 'abcdefghijklmnopqrstuvwxyz'
UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SPECIAL = '!@#$%^&*()?-=_+[]{}'
AMBIGUOUS = set('O0oIl1|`\'")({}[]')  # easily confused characters

MIN_LENGTH = 6
MAX_LENGTH = 64


def generate_password(length: int, use_upper: bool, use_numbers: bool, use_special: bool,
                      exclude_ambiguous: bool = False) -> str:
    """Cryptographically secure password with at least one char from each selected category."""

    def allowed(chars: str) -> str:
        if exclude_ambiguous:
            return ''.join(c for c in chars if c not in AMBIGUOUS)
        return chars

    categories = [allowed(LOWER)]
    if use_upper:
        categories.append(allowed(UPPER))
    if use_numbers:
        categories.append(allowed(NUMBERS))
    if use_special:
        categories.append(allowed(SPECIAL))
    categories = [c for c in categories if c]
    pool = ''.join(categories)
    # Guarantee one character from each selected category
    chars = [secrets.choice(cat) for cat in categories]
    chars += [secrets.choice(pool) for _ in range(length - len(chars))]
    # Fisher-Yates with secrets
    for i in reversed(range(1, len(chars))):
        j = secrets.randbelow(i + 1)
        chars[i], chars[j] = chars[j], chars[i]
    return ''.join(chars)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Password Generator')
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icon.png')
        if os.path.exists(icon_path):
            self._icon = tk.PhotoImage(file=icon_path)
            self.iconphoto(False, self._icon)
        self.resizable(False, False)
        self._init_ui()
        # Make sure the window is brought to front on macOS
        self.attributes('-topmost', True)
        self.lift()
        self.focus_force()
        self.after(300, lambda: self.attributes('-topmost', False))

    def _init_ui(self):
        pad = {'padx': 12, 'pady': 4}
        frm = ttk.Frame(self, padding=16)
        frm.pack(fill='both', expand=True)

        # Output field
        self.var_password = tk.StringVar()
        self.entry_password = ttk.Entry(frm, textvariable=self.var_password, width=38,
                                         state='readonly')
        self.entry_password.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        # Length
        ttk.Label(frm, text='Length:').grid(row=1, column=0, sticky='w', **pad)
        self.var_length = tk.IntVar(value=12)
        self.spin_length = ttk.Spinbox(frm, from_=MIN_LENGTH, to=MAX_LENGTH,
                                       textvariable=self.var_length, width=6)
        self.spin_length.grid(row=1, column=1, sticky='w', **pad)

        # Checkboxes
        self.var_upper = tk.BooleanVar(value=True)
        self.var_numbers = tk.BooleanVar(value=True)
        self.var_special = tk.BooleanVar(value=False)
        self.var_no_ambiguous = tk.BooleanVar(value=False)
        ttk.Checkbutton(frm, text='Upper case (A-Z)', variable=self.var_upper).grid(
            row=2, column=0, columnspan=2, sticky='w', **pad)
        ttk.Checkbutton(frm, text='Numbers (0-9)', variable=self.var_numbers).grid(
            row=3, column=0, columnspan=2, sticky='w', **pad)
        ttk.Checkbutton(frm, text='Special symbols (!@#$…)', variable=self.var_special).grid(
            row=4, column=0, columnspan=2, sticky='w', **pad)
        ttk.Checkbutton(frm, text='Exclude ambiguous characters (O/0, l/1…)',
                        variable=self.var_no_ambiguous).grid(
            row=5, column=0, columnspan=2, sticky='w', **pad)

        # Buttons
        ttk.Button(frm, text='Generate', command=self.generate).grid(
            row=6, column=0, sticky='ew', **pad)
        ttk.Button(frm, text='Copy', command=self.copy_to_clipboard).grid(
            row=6, column=1, sticky='ew', **pad)
        ttk.Button(frm, text='Clear', command=self.clear).grid(
            row=7, column=0, sticky='ew', **pad)
        ttk.Button(frm, text='Save to file…', command=self.save_to_file).grid(
            row=7, column=1, sticky='ew', **pad)

        self.lbl_copied = ttk.Label(frm, text='Copied!', foreground='green')
        self.lbl_copied.grid(row=8, column=0, columnspan=2)

    def generate(self):
        if self.var_length.get() < MIN_LENGTH:
            messagebox.showwarning('Warning', f'Minimum length is {MIN_LENGTH}')
            return
        self.var_password.set(generate_password(
            self.var_length.get(),
            self.var_upper.get(),
            self.var_numbers.get(),
            self.var_special.get(),
            self.var_no_ambiguous.get(),
        ))
        self.lbl_copied.config(text='')

    def copy_to_clipboard(self):
        if not self.var_password.get():
            return
        self.clipboard_clear()
        self.clipboard_append(self.var_password.get())
        self.lbl_copied.config(text='Copied!')

    def clear(self):
        self.var_password.set('')
        self.lbl_copied.config(text='')

    def save_to_file(self):
        if not self.var_password.get():
            messagebox.showwarning('Warning', 'Password has not been generated yet')
            return
        file_name = filedialog.asksaveasfilename(
            title='Save Password', initialdir=os.getenv('HOME') or os.path.expanduser('~'))
        if not file_name:
            return  # user cancelled the dialog
        try:
            with open(file_name, 'w') as file:
                file.write(self.var_password.get())
        except OSError:
            messagebox.showwarning('Error', 'Could not save file')


if __name__ == '__main__':
    app = App()
    app.mainloop()
