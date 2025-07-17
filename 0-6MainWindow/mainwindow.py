# We need to import QSize from QtCore so we can set the size of the icons
from PySide6.QtCore import QSize
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar

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
        # the & ("&File")means the F key becomes the access key (Alt + F will open the menu)
        file_menu = menu_bar.addMenu("&File")
        quit_action = file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Cut")
        edit_menu.addAction("Paste")
        edit_menu.addAction("Undo")
        edit_menu.addAction("Redo")

        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")



        toolbar = QToolBar("My main toolbar")
        toolbar.setIconSize(QSize(16,16))
        self.addToolBar(toolbar)

        toolbar.addAction(quit_action) # Doesn't just have to be a name as we can pass in an already existing action as seen here

        # Qt / PySide has us pass in the parent object as the second parameter in many classes
        # Qt uses a parent child hierarchy to manage object lifetimes so everything can be properly managed when something is deleted
        # which also prevents memory leakage
        # so action1 is considered a child of MainWindow
        action1 = QAction("Some Action", self)
        # this line was not included in the course but the following line
        # another (redundant) way to do this is self.setStatusBar(self.statusBar()) where statusBar is created if it doesnt exist from self.statusBar() and is returned, to the setStatusBar method and that sets the returned status bar
        status_bar = self.statusBar()
        # sets message in status bar which is a place at the bottom of the screen where tips and info show up
        action1.setStatusTip("Status message for some action")
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)



    def quit_app(self):
        self.app.quit()
    
    def toolbar_button_click(self):
        print("action1 triggered")