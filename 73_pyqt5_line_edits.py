import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QPushButton, QLabel


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 500, 500)
        self.line_edit = QLineEdit(self)
        self.button = QPushButton("Submit", self)
        self.label = QLabel(self)
        self.initUI()

    def initUI(self):
        self.line_edit.setGeometry(10, 10, 200, 40)
        self.button.setGeometry(220, 10, 100, 40)
        self.line_edit.setPlaceholderText("Enter your name")
        self.line_edit.setStyleSheet("font-size: 25px;font-family: Arial;")
        self.button.setStyleSheet("font-size: 25px;font-family: Arial;")
        self.button.clicked.connect(self.submit)
        self.label.setGeometry(10, 60, 500, 40)
        self.label.setStyleSheet("font-size: 25px;font-family: Arial;")

    def submit(self):
        text = self.line_edit.text()
        self.label.setText(f"Hello {text}!")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
