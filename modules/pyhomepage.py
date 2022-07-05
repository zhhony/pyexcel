import modules.pyappui as pyappui
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from typing import *
from py_test_tools import *


class HomePage():
    def __init__(self, MainWindow: QMainWindow, ui: pyappui.Ui_MainWindow) -> None:
        self._APP_VERSION = 'v0.4.0'
        self._MainWindow = MainWindow
        self._ui = ui
