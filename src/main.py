from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pyqt5_material import apply_stylesheet

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Root Finding Algorithm Comparator')
        
        self.resize(800, 400)

        self.prepare_ui()
        self.show()
    
    def prepare_ui(self):
        self.btn1 = QPushButton('Home', self)
        self.btn1.clicked.connect(self.display_home)

        self.btn2 = QPushButton('Graph', self)
        self.btn2.clicked.connect(self.display_plot)

        self.btn3 = QPushButton('Setting', self)
        self.btn3.clicked.connect(self.display_setting)

        left_side = QVBoxLayout()
        left_side.addWidget(self.btn1)
        left_side.addWidget(self.btn2)
        left_side.addWidget(self.btn3)
        left_side.addStretch(5)
        left_side.addSpacing(20)
        left_widget = QWidget()
        left_widget.setLayout(left_side)

        self.right_widget = QTabWidget()
        self.right_widget.tabBar().setObjectName('tab')
        self.right_widget.addTab(self.build_home(), '')
        self.right_widget.addTab(self.build_plot(), '')
        self.right_widget.addTab(self.build_setting(), '')
        self.right_widget.setCurrentIndex(0)
        self.right_widget.setStyleSheet('QTabBar::tab{width: 0; height: 0; margin: 0; padding: 0; border: none;}')

        main = QHBoxLayout()
        main.addWidget(left_widget)
        main.addWidget(self.right_widget)
        main.setStretch(1, 200)
        main_widget = QWidget()
        main_widget.setLayout(main)
        self.setCentralWidget(main_widget)

    def build_home(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Home'))
        layout.addStretch(5)
        main = QWidget()
        main.setLayout(layout)
        return main

    def build_plot(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Plot'))
        layout.addStretch(5)
        main = QWidget()
        main.setLayout(layout)
        return main

    def build_setting(self):
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Setting'))
        layout.addStretch(5)
        main = QWidget()
        main.setLayout(layout)
        return main

    def display_home(self):
        self.right_widget.setCurrentIndex(0)
    
    def display_plot(self):
        self.right_widget.setCurrentIndex(1)
    
    def display_setting(self):
        self.right_widget.setCurrentIndex(2)


app = QApplication([])
app.setFont(QFont('Open Sans', 14))
mw = MainWindow()
apply_stylesheet(app, theme='dark_amber.xml')
app.exec_()
