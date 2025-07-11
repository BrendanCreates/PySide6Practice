# Responding to the button VERSION 1

from PySide6.QtWidgets import QApplication, QPushButton

# The slot - responds when something happens
def button_clicked():
    print("You clicked the button didn't you!")

app = QApplication()
button = QPushButton("Press Me")

# THe next line is how we want to respond to the signal
# clicked is the signal we want to respond to, we say the name of the variable.clicked to respond to
# we call the connect method on this to specify the method responds to the signal
# we know button has a clicked signal because of the documentation for QPushButton (Look at the provided slots for QAbstractButton class)
# The signal - clicked
# this line we can refer to as "the connection"
button.clicked.connect(button_clicked)

button.show()
app.exec()