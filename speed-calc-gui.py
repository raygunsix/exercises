import sys

from PyQt6.QtWidgets import QApplication, QComboBox, QGridLayout, QLabel, QLineEdit, QPushButton, QStatusBar, QWidget 


class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("Distance: ")
        self.distance_line_edit = QLineEdit()

        time_label = QLabel("Time (hours): ")
        self.time_line_edit = QLineEdit()

        self.combo = QComboBox()
        self.combo.addItems(['Metric (km)', 'Imperial (miles)'])

        calculate_button = QPushButton("Calculate")
        calculate_button.clicked.connect(self.average_speed)

        self.status_bar = QStatusBar()

        # Add widgets to greid
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combo, 0, 2)
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)
        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.status_bar, 3, 0, 1, 2)

        self.setLayout(grid)

    def average_speed(self):

        avg = int(self.distance_line_edit.text()) / int(self.time_line_edit.text())

        if self.combo.currentText() == "Imperial (miles)":
            units = "mph"
        if self.combo.currentText() == "Metric (km)":
            units = "km/h"

        self.status_bar.showMessage(f"Average Speed: {avg} {units}")


app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())