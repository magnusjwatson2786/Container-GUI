import sys
import os
import platform
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

from ui import *

widgets = None


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        widgets.pushButton_5.clicked.connect(
            lambda: Fxns.toggleMenu(self, True))
        Fxns.fxnsdef(self)

        widgets.pushButton_6.clicked.connect(self.buttonClick)
        widgets.pushButton_7.clicked.connect(self.buttonClick)
        widgets.pushButton_8.clicked.connect(self.buttonClick)
        widgets.pushButton_9.clicked.connect(self.buttonClick)
        widgets.pushButton_10.clicked.connect(self.buttonClick)

        self.show()

        themeFile = "themes\deep_ocean.qss"
        Fxns.theme(self, themeFile, True)

        widgets.stackedWidget.setCurrentWidget(widgets.page)
        widgets.pushButton_6.setStyleSheet(
            Fxns.selectMenu(widgets.pushButton_6.styleSheet()))

    def buttonClick(self):
        btn = self.sender()
        btnName = btn.objectName()

        if btnName == "pushButton_6":
            widgets.stackedWidget.setCurrentWidget(widgets.page)
            Fxns.resetStyle(self, btnName)
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))

        if btnName == "pushButton_7":
            widgets.stackedWidget.setCurrentWidget(widgets.page_2)
            Fxns.resetStyle(self, btnName)
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))

        if btnName == "pushButton_8":
            widgets.stackedWidget.setCurrentWidget(widgets.page_3)
            Fxns.resetStyle(self, btnName)
            btn.setStyleSheet(Fxns.selectMenu(btn.styleSheet()))

        if btnName == "pushButton_9":
            self.close()

        if btnName == "pushButton_10":
            Fxns.resetStyle(self, btnName, True)

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MainWindow()
    sys.exit(app.exec())
