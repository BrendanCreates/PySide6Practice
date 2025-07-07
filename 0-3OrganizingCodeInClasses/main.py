from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

import sys
app = QApplication(sys.argv)

# MainWindow can have menus and toolbars and stuff, different type of window, we can also give it a central widget
window = QMainWindow() 
window.setWindowTitle("Our first MainWindow App!")

# This button will be added to the main window
button = QPushButton()
button.setText("Press Me")

# We are adding it to the main window here
window.setCentralWidget(button)

window.show()
app.exec()

# In the terminal type python main.py to run and see a blank window
# (run button works just fine)