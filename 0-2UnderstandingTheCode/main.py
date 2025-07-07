from PySide6.QtWidgets import QApplication, QWidget # QApplication and QWidget are the classes we will be using

# sys is used to process command line arguments
# they will be picked up by the QApplication instance (app)
# they can then be processes in the Qt application (window)
import sys

# application is like a wrapper that englobes everything in Qt application
# responsible for runnig application and waiting for things to happen
app = QApplication(sys.argv)

# widgets or windows are hidden by default so we need to show it
# reading up on QWidget object may be very useful, "atom" of the user interface
window = QWidget()
window.show()

# run the exec function on the application to start the event loop
# while loop waiting for things to happen (e.x. button click)
app.exec()

# In the terminal type python main.py to run and see a blank window
# (run button works just fine)