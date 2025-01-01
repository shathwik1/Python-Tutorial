import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)

        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        font_path = "DS-DIGIT.TTF"
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]

        custom_font = QFont(font_family, 150)
        self.time_label.setFont(custom_font)

        self.time_label.setAlignment(Qt.AlignCenter)
        self.setStyleSheet("background-color: black;")
        self.time_label.setStyleSheet("color: hsl(111, 100%, 50%);")

        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        self.update_time()

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss:AP")
        self.time_label.setText(current_time)


def main():
    app = QApplication(sys.argv)
    window = DigitalClock()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
