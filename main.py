import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from HomePage import HomePage
from KnapsackSolver import KnapsackSolver
from TransportationSolver import TransportationSolver

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()