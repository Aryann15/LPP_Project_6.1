from PyQt5.QtWidgets import QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QTextEdit
from gurobipy import Model, GRB
from PyQt5.QtCore import Qt

class KnapsackSolver(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        # Styling
        self.setStyleSheet("font-size: 16px;")
        # Layouts
        back_layout = QVBoxLayout()
        input_layout = QVBoxLayout()
        main_layout = QVBoxLayout()
        result_layout = QVBoxLayout()
        buttons_layout = QHBoxLayout()
        # Back Button
        back_button = QPushButton("Back")
        back_button.setFixedSize(330, 30)
        back_button.setCursor(Qt.PointingHandCursor)  
        back_button.setStyleSheet(
             "QPushButton {"
            "   font-size: 14px;"
            "   border-radius: 10px;"
            "   background-color: #C8CECF;"
            "   color: #ffffff;"
            "   font-style: italic;"
            "}"
            "QPushButton:hover {"
            "   background-color: #BABFC0;"
            "   font-size:15px;"
            "}"
        )
        back_button.clicked.connect(self.gotoHome)
        back_layout.addWidget(back_button)
        back_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
