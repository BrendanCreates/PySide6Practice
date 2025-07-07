from PySide6.QtWidgets import QApplication, QWidget # QApplication and QWidget are the classes we will be using

import sys

app = QApplication(sys.argv)

window = QWidget()
window.show()

app.exec()

# In the terminal type python main.py to run and see a blank window