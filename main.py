import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from HomePage import HomePage
from KnapsackSolver import KnapsackSolver
from TransportationSolver import TransportationSolver

class MainApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Operations Research Project")
        self.setGeometry(330, 120, 1200, 800)
        self.setStyleSheet("QMainWindow { background-color: #E1EFF3; }")
        self.stack = QStackedWidget(self)
        self.home_page = HomePage(self)
        self.knapsack_solver = KnapsackSolver(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec_())