# Class in separate file VERSION 3

import sys
from PySide6.QtWidgets import QApplication
from version_three_class import ButtonHolder # from Python file name import class name

app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

app.exec()