from PySide6.QtWidgets import QApplication, QMainWindow

# we are going to inheret from QMainWindow and make this class that basically just sets up a main window constructred from the main window base object
class MainWindow(QMainWindow):
    # app is the application instance that created the main window
    # this app parameter is not required by the QMainWindow constructor as seen in the super().__init__() line
    def __init__(self, app):
        super().__init__()
        self.app = app # self.name = value declaring member variable app and using app parameter as the value
        self.setWindowTitle("Custom MainWindow")

        # menubar and menus
        menu_bar = self.menuBar()
        # the & means the F key becomes the access key (Alt + F will open the menu)
        file_menu = menu_bar.addMenu("&File")