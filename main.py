import sys
import random
import ctypes
from PyQt5.QtGui import QIcon
from ui import form
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow


class App(QMainWindow, form.Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.output_pass = None
        self.init_ui()

    def init_ui(self):
        self.setupUi(self)
        self.setWindowTitle('Password Generator')
        self.setWindowIcon(QIcon('ui/icon.ico'))
        self.setFixedSize(350, 450)
        self.output_pass.setDisabled(True)
        self.output_pass.setPlaceholderText('Your password will be here')
        self.btn_generate.clicked.connect(self.generate_password)
        self.btn_copy.clicked.connect(self.copy_to_clipboard)
        self.btn_clear.clicked.connect(self.clear_password)
        self.spin_box_length.setMinimum(6)
        self.spin_box_length.setMaximum(16)
        self.lbl_copied.setVisible(False)

    def generate_password(self):
        self.output_pass.setText(self.get_password())
        self.lbl_copied.setVisible(False)

    def copy_to_clipboard(self):
        cb = QApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.output_pass.text(), mode=cb.Clipboard)
        self.lbl_copied.setVisible(True)

        if self.output_pass.text() == '':
            self.lbl_copied.setVisible(False)

    def clear_password(self):
        if self.output_pass.text() == '':
            pass
        else:
            self.output_pass.setText('')
            self.lbl_copied.setVisible(False)

    def get_password(self):
        start_list = list('abcdefghijklmnopqrstuvwxyz')
        upper_list = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        number_list = list('1234567890')
        special_list = list('!@#$%^&*()?-=_+[]{}')

        length = self.spin_box_length.value()
        password = ''

        if self.check_upper.isChecked():
            start_list.extend(upper_list)
        if self.check_number.isChecked():
            start_list.extend(number_list)
        if self.check_special.isChecked():
            start_list.extend(special_list)
        elif not self.check_upper.isChecked() and self.check_number.isChecked() and self.check_special.isChecked():
            start_list = password

        for _ in range(length):
            password += random.choice(start_list)

        return password


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app_id = 'app.product.sub_product.version'
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
    main_window = App()
    main_window.show()
    app.exec()
