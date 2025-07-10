# Slider Version 3

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QSlider

# The slot - responds when something happens
def respond_to_slider(data):
    #fstring is better
    print(f"Slider moved to : {data}") # This is also a way to add a value and add a space before data print("Slider moved to : ", data) its a way to print multiple values separated by spaces

app = QApplication()
slider = QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

# The Qt system takes care of passing the data from the signal to the slot
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()