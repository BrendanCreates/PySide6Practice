# Class in separate file VERSION 3

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

# Subclass QMainWindow to customize our application's main window
# This class inherets from QMainWindow
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__() # this is used in child classes to call the __init__ method of the parent class
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press Me!")
        # Set our button as the central widget
        self.setCentralWidget(button)