import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton


class GuessNumberApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Угадай число')
        self.setGeometry(100, 100, 300, 200)

        self.number_to_guess = random.randint(1, 100)
        self.attempts = 10

        layout = QVBoxLayout()

        self.label = QLabel('Введите число от 1 до 100:')
        layout.addWidget(self.label)

        self.input = QLineEdit()
        layout.addWidget(self.input)

        self.button = QPushButton('Угадать')
        self.button.clicked.connect(self.guess_number)
        layout.addWidget(self.button)

        self.result_label = QLabel('')
        layout.addWidget(self.result_label)

        self.setLayout(layout)

    def guess_number(self):
        guess = random.randint(0,100)
        if guess < self.number_to_guess:
            self.result_label.setText('Загаданное число больше')
        elif guess > self.number_to_guess:
            self.result_label.setText('Загаданное число меньше')
        else:
            self.result_label.setText('Вы угадали!')
        self.attempts -= 1
        if self.attempts == 0:
            self.result_label.setText('Вы проиграли. Было загадано число: ' + str(self.number_to_guess))
            self.button.setEnabled(False)



app = QApplication(sys.argv)
window = GuessNumberApp()
window.show()
sys.exit(app.exec())