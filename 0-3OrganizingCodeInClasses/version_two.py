# Goal is to organize code in classes and have separate files
# Functionality in class VERSION 2

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys

# Subclass QMainWindow to customize our application's main window
# This class inherets from QMainWindow
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__() # this is used in child classes to call the __init__ method of the parent class
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press Me!")
        # Set our button as the central widget
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = ButtonHolder() # because we did super().__init__() then the object we are designating as our window has all the standard window object stuff
window.show() # the sub class has all of the QMainWindow functions
app.exec()