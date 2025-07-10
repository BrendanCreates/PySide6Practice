# Emitted parameters VERSION 2
# In the signal documentation we can see emitted parameters in ()

from PySide6.QtWidgets import QApplication, QPushButton

# The slot - responds when something happens
def button_clicked(data):
    print("You clicked the button didn't you! checked : ", data)

app = QApplication()
button = QPushButton("Press Me")
# Makes the button checkable, it is uncheckable by default
# Further clicks toggle between checked and unchecked
button.setCheckable(True)

button.clicked.connect(button_clicked)

# Toggle between true and false true and false
button.show()
app.exec()