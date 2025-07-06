'''


 --- Goals ---

 
Documentation of the base class for all UI objects:
 --- https://doc.qt.io/qtforpython-6/PySide6/QtWidgets/QWidget.html 
Example code I can examine (probably not run because most are in C++):
 --- https://doc.qt.io/qt-6/qtexamplesandtutorials.html

We want to build with PySide6 and Qt (cute) because we only need to build 
the code once and it will work on Windows, Mac, and Linux.
 --- It will run seamlessly.

Succinctly, we will be building cross platform desktop apps with Qt 
under PySide6.
 --- PySide6 allows us to put Python and Qt together to take advantage 
     of what Qt provides.
 --- Qt is a cross platform framework for building apps but it was
     mainly made for C++.

My goal is to get a strong foundation for GUIs using PySide6.
 --- I will then build GUIs for existing and future Python projects.
 --- This strong foundation should also help me transfer my knowledge
     to a different framework like PyQt.

     
 --- Qt ---

 
Develop cross platform (Windows, Mac, Linux) and even Android and iOS.
 --- and embedded systems! 

We write our code once then recompile it for the destined platform to
get the specific binaries for the operating system.

The main language for Qt is C++ but Python is catching up under Qt for
Python or PySide6.
 --- Android, iOS, and embedded systems support is still in development
     for PySide6.

PyQt is often mentioned along with PySide6 but PySide6 is under the Qt
official project so support for iOS and Android should come faster for 
PySide6.
 --- PyQt also requires a separate license for PyQt AND Qt. PySide6 only
     needs one license.

Software built in Qt: (!!!)
 --- Ableton Live
 --- Some Adobe apps
 --- Autodesk Apps
 --- Google Earth
 --- EAGLE
 --- DaVinci Resolve
 --- Mathematica
 --- OBS
 --- Roblox Studio
 --- Teamviewer
 --- Telegram
 --- VirtualBox
 --- VLC media player
 --- Wireshark

Companies using Qt: (!!!)
 --- AMD
 --- Blizzard Entertainment
 --- BMW
 --- Electronic Arts
 --- European Space Agency
 --- DreamWorks
 --- Microsoft
 --- Samsung

There are 2 APIs when it comes to building Qt applications:
 --- Qt Widgets: we can build UIs for desktop platforms. This is best for
                 desktop only applications. We will be learning this one!
 --- QML: new devices like mobile devices and embedded systems, can be
          used to build more modern looking apps. QML applications can
          also run on desktop so we must do some research to decide. It
          is a declarative language that makes it easy to pick up by
          designers.

Qt is more than GUIs:
 --- We can take advantage of network, threading, databases, and tons of
     other utility classes.
 --- We will touch on the basics of HTTP networking.


 --- Setup ---


Run pip3 install pyside6 in powershell
 
'''