import sys

from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance: ")

        time_label = QLabel("Time (hours): ")

        calculate_button = QPushButton("Calculatre Speed: ")

        # Add widgets to greid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(time_label, 0, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)

        self.setLayout(grid)

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())