# Widgets are the basic components to build UI, they come from QtWidgetsModule
# QPushButton, QLineEdit, QTextEdit, QMainWindow, Layots, Size policies and stretches
# QWidget is the base class to use in Qt applications
# Also how to use layouts flexibly inside of a widget

from PySide6.QtWidgets import QPushButton, QWidget, QHBoxLayout, QVBoxLayout
class RockWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RockWidget")

        # components
        button1 = QPushButton("BUTTON1")
        button1.clicked.connect(self.button1_clicked)
        button2 = QPushButton("BUTTON2")
        button2.clicked.connect(self.button2_clicked)

        # using layouts
        # widget_layout = QHBoxLayout  # Horizontal
        widget_layout = QVBoxLayout() # Vertical
        widget_layout.addWidget(button1)
        widget_layout.addWidget(button2)
        self.setLayout(widget_layout)

    def button1_clicked(self):
        print("Button1 clicked")
    
    def button2_clicked(self):
        print("Button2 clicked")

