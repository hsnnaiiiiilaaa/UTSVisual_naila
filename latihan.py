import sys
from PyQt5.QtWidgets import QApplication,QLabel,QWidget
app = QApplication([])
windows = QWidget()
windows.setWindowTitle("PyQt App")
windows.setGeometry(100, 100, 280, 80)
helloMsg = QLabel("Hello, World", parent=windows)
helloMsg.move(60, 15)
windows.show()
sys.exit(app.exec())