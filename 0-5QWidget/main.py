# If we import QWidget and did window = QWidget() and window.show() then executed the app it would just be a black grey page, we must make something of the widget

from PySide6.QtWidgets import QApplication
from rockwidget import RockWidget
import sys

app = QApplication(sys.argv)

widget = RockWidget()
widget.show()

app.exec()