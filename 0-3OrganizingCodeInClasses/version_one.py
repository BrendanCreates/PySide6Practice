# Goal is to organize code in classes and have separate files
# Global access/scope VERSION 1

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

# MainWindow can have menus and toolbars and stuff, different type of window, we can also give it a central widget
window = QMainWindow() 
window.setWindowTitle("Our first MainWindow App!")

# This button will be added to the main window
# This simply just creates a button but at this point it isnt utilized
button = QPushButton()
button.setText("Press Me")

# We are adding it to the main window here
window.setCentralWidget(button)

window.show()
app.exec()