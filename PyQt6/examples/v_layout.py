"""Vertical layout example."""

import sys

from PyQt6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("QVBoxLayout")

layout = QVBoxLayout()
layout.addWidget(QPushButton("Топ"))
layout.addWidget(QPushButton("Центр"))
layout.addWidget(QPushButton("Кнопка"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())
