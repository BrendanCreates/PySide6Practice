# This is a window that can have little parts or components we can customize like
# a menu bar on the top, below that a toolbar, a center widget where most of the useful stuff is
# we can call menuBar function on QMainWindow to get menubar object and add acctions to it
# we can add actions to the tool bar or the menu bar
# actions have a triggered signal we can then connect it to a quit method so quit action quits the application
# we can create QAction objects and give them icons along with the standard name
# we can create a status bar by using the setSttatusBar method and passing the QStatusBar object in place
# we can also add an icon for the toolbar itself

"""

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()

Running this basic code and the basic class with nothing in it is not much more than displaying a QWidget, the benefit of the QMainWindow is all the different things we can add to it

"""

from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys

app = QApplication(sys.argv)

window = MainWindow(app)
window.show()

app.exec()