from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit
from gurobipy import Model, GRB
from PyQt5.QtCore import Qt

class KnapsackSolver(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)