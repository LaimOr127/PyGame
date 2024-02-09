"""Horizontal layout example."""

import sys

from PyQt6.QtWidgets import QApplication, QHBoxLayout, QPushButton, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("QHBoxLayout")

layout = QHBoxLayout()
layout.addWidget(QPushButton("Левая"))
layout.addWidget(QPushButton("Центральная"))
layout.addWidget(QPushButton("Правая"))
window.setLayout(layout)

window.show()
sys.exit(app.exec())
