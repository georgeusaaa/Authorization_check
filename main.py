import secrets
import string
import sys

from PyQt6.QtWidgets import QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget

STYLE = """
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
"""


def generate_password(login: str, digits: int = 4) -> str:
    """Логин + случайные цифры. secrets вместо random — результат нельзя предсказать."""
    return login + "".join(secrets.choice(string.digits) for _ in range(digits))


class RegisterWindow(QWidget):
    """Первое окно: придумываем логин и пароль."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Тренировка Авторизации")
        self.login_window = None

        layout = QVBoxLayout(self)
        layout.setSpacing(5)

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Логин")
        layout.addWidget(self.login_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        layout.addWidget(self.password_input)

        self.submit_btn = QPushButton("Нажать")
        self.submit_btn.setObjectName("AccentBtn")
        self.submit_btn.setFixedSize(150, 50)
        self.submit_btn.clicked.connect(self.on_submit)
        layout.addWidget(self.submit_btn)

        self.generate_btn = QPushButton("Придумать пароль")
        self.generate_btn.clicked.connect(self.on_generate)
        layout.addWidget(self.generate_btn)

        self.status_label = QLabel("")
        layout.addWidget(self.status_label)

    def on_generate(self):
        login = self.login_input.text().strip()
        if not login:
            self.show_status("Сначала введите логин!", "red")
            return
        password = generate_password(login)
        self.password_input.setText(password)
        self.show_status("Скопируй: " + password, "#b0b0b5")

    def on_submit(self):
        login = self.login_input.text().strip()
        password = self.password_input.text()

        if not login or not password:
            self.show_status("Заполните все поля!", "red")
            return

        self.login_window = LoginWindow(login, password)
        self.login_window.show()
        self.hide()

    def show_status(self, text: str, color: str):
        self.status_label.setText(text)
        self.status_label.setStyleSheet(f"color: {color};")


class LoginWindow(QWidget):
    """Второе окно: проверяем, что пользователь запомнил логин и пароль."""

    def __init__(self, login: str, password: str):
        super().__init__()
        self.login = login
        self.password = password

        self.setWindowTitle("Авторизация")
        self.resize(300, 200)

        layout = QVBoxLayout(self)
        layout.setSpacing(5)

        self.login_input = QLineEdit()
        self.login_input.setPlaceholderText("Введите Логин")
        layout.addWidget(self.login_input)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Введите Пароль")
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.returnPressed.connect(self.on_check)
        layout.addWidget(self.password_input)

        self.check_btn = QPushButton("Проверить")
        self.check_btn.setObjectName("AccentBtn")
        self.check_btn.setFixedSize(150, 50)
        self.check_btn.clicked.connect(self.on_check)
        layout.addWidget(self.check_btn)

        self.result_label = QLabel("")
        layout.addWidget(self.result_label)

    def on_check(self):
        if self.login_input.text().strip() == self.login and self.password_input.text() == self.password:
            self.result_label.setText("Верно")
            self.result_label.setStyleSheet("color: green;")
        else:
            self.result_label.setText("Неверно")
            self.result_label.setStyleSheet("color: red;")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(STYLE)
    window = RegisterWindow()
    window.show()
    sys.exit(app.exec())
