"""Form layout example."""

import sys

from PyQt6.QtWidgets import QApplication, QFormLayout, QLineEdit, QWidget

app = QApplication([])
window = QWidget()
window.setWindowTitle("QFormLayout")

layout = QFormLayout()
layout.addRow("Имя:", QLineEdit())
layout.addRow("Возраст:", QLineEdit())
layout.addRow("Работа:", QLineEdit())
layout.addRow("Хобби:", QLineEdit())
window.setLayout(layout)

window.show()
sys.exit(app.exec())
