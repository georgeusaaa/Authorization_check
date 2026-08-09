from PyQt6.QtWidgets import *
from random import *
import sys

app = QApplication(sys.argv)
app.setStyleSheet("""
    /* Стилизация всех окон приложения */
    QWidget {
        background-color: #1e1e24;
        color: #e0e0e0;
        font-family: "Segoe UI", sans-serif;
        font-size: 14px;
    }

    /* Стилизация полей ввода текста */
    QLineEdit {
        background-color: #2a2a32;
        color: #ffffff;
        border: 2px solid #3a3a44;
        border-radius: 6px;
        padding: 8px 12px;
    }
    QLineEdit:focus {
        border: 2px solid #2196F3; /* Подсветка активного поля синим */
    }

    /* Общие стили для ВСЕХ кнопок */
    QPushButton {
        background-color: #3a3a44;
        color: #ffffff;
        border: none;
        border-radius: 6px;
        padding: 8px 16px;
        font-weight: bold;
    }
    QPushButton:hover {
        background-color: #4a4a56; /* Эффект при наведении */
    }
    QPushButton:pressed {
        background-color: #2d2d35; /* Эффект при клике */
    }

    /* Стили для главных акцентных кнопок по их ID */
    QPushButton#AccentBtn {
        background-color: #2196F3;
    }
    QPushButton#AccentBtn:hover {
        background-color: #1976D2;
    }
    QPushButton#AccentBtn:pressed {
        background-color: #0D47A1;
    }

    /* Стили для меток текста (текст вывода пароля и т.д.) */
    QLabel {
        color: #b0b0b5;
        font-size: 13px;
        padding: 4px;
    }
""")

window = QWidget()
window.setWindowTitle("Тренировка Авторизации")
window.show()

layout = QVBoxLayout()
layout.setSpacing(5)

inp = QLineEdit()
inp.setPlaceholderText('Логин')
layout.addWidget(inp)

inp1 = QLineEdit()
inp1.setPlaceholderText('Пароль')
layout.addWidget(inp1)

btn_1 = QPushButton('Нажать')
layout.addWidget(btn_1)
btn_1.setFixedSize(150, 50)

g_btn = QPushButton("Придумать пароль")
layout.addWidget(g_btn)

generate_passw = QLabel("")
layout.addWidget(generate_passw)

ls = ['1', '2', '3', '4', '5', '6', '7', '8', '9']


def generation():
    log_cur = inp.text()
    random_chars = "".join(choices(ls, k=4))
    generate_passw.setText("Скопируй: " + log_cur + random_chars)
    inp1.setText(log_cur + random_chars)


g_btn.clicked.connect(generation)

log = ""
passw = ""


def ckick_btn_on():
    global log, passw

    log = inp.text()
    passw = inp1.text()

    if log == "" or passw == "":
        generate_passw.setText("Заполните все поля!")
        generate_passw.setStyleSheet("color: red;")
    else:
        generate_passw.setText("")
        ckick_btn()


def ckick_btn():
    global window2

    window2 = QWidget()
    window2.setWindowTitle("Авторизация")
    window2.resize(300, 200)

    layout2 = QVBoxLayout()
    layout2.setSpacing(5)

    inp2 = QLineEdit()
    inp2.setPlaceholderText('Введите Логин')
    layout2.addWidget(inp2)

    inp3 = QLineEdit()
    inp3.setPlaceholderText('Введите Пароль')
    layout2.addWidget(inp3)

    btn_2 = QPushButton('Проверить')
    layout2.addWidget(btn_2)
    btn_2.setFixedSize(150, 50)

    result_label = QLabel("")
    layout2.addWidget(result_label)

    window2.setLayout(layout2)
    window2.show()

    window.hide()

    def checking():
        log2 = inp2.text()
        passw2 = inp3.text()

        if log2 == log and passw2 == passw:
            result_label.setText("Верно")
            result_label.setStyleSheet("color: green;")
        else:
            result_label.setText("Неверно")
            result_label.setStyleSheet("color: red;")

    btn_2.clicked.connect(checking)


btn_1.clicked.connect(ckick_btn_on)

window.setLayout(layout)
app.exec()
