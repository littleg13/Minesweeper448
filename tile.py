import sys
from Styles import StyleSheet
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Tile(QWidget):
    def __init__(self):
        super().__init__()

        self.addWidget(QPushButton(""))

    def incCount(self):
        return True

    def setMine(self):
        return True
