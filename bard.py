import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, \
    QSpacerItem, QSizePolicy, QStackedWidget


class LoginApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()

        self.default_credentials = {
            "user123": "password123",
            "admin": "admin123"
        }

    def init_ui(self):
        self.stacked_widget = QStackedWidget(self)

        login_page = QWidget()
        welcome_page = QWidget()
        signup_page = QWidget()

        self.stacked_widget.addWidget(login_page)
        self.stacked_widget.addWidget(welcome_page)
        self.stacked_widget.addWidget(signup_page)

        self.init_login_page(login_page)
        self.init_welcome_page(welcome_page)
        self.init_signup_page(signup_page)

        layout = QVBoxLayout(self)
        layout.addWidget(self.stacked_widget)
        self.setLayout(layout)

    def init_signup_page(self, page):
        layout = QVBoxLayout()

        layout_name = QHBoxLayout()

        self.Name = QLabel("Name    : ")
        self.Cusername_input = QLineEdit()
        self.Cusername_input.setPlaceholderText("Username")
        layout_name.addWidget(self.Name)
        layout_name.addWidget(self.Cusername_input)

        layout2 = QHBoxLayout()
        self.PW = QLabel("PassWord :")
        layout2.addWidget(self.PW)

        self.C1_password_input = QLineEdit()
        self.C1_password_input.setPlaceholderText("Password")
        self.C1_password_input.setEchoMode(QLineEdit.Password)
        layout2.addWidget(self.C1_password_input)

        layout3 = QHBoxLayout()

        self.C2_password_input = QLineEdit()
        self.C2_password_input.setPlaceholderText("Confirm Password")
        self.C2_password_input.setEchoMode(QLineEdit.Password)
        layout2.addWidget(self.C2_password_input)

        sign_button = QPushButton("Create Account")
        sign_button.clicked.connect(self.check)
        back_button = QPushButton("Back")
        back_button.clicked.connect(self.show_login_page)

        layout.addLayout(layout_name)
        layout.addLayout(layout2)
        layout.addLayout(layout3)
        layout.addWidget(sign_button)
        layout.addWidget(back_button)

        page.setLayout(layout)

    def init_login_page(self, page):

        layout = QVBoxLayout()
        center_layout = QVBoxLayout()

        empty = QHBoxLayout()
        self.Hello = QLabel("Hello There")
        self.Hello.setAlignment(Qt.AlignHCenter)
        empty.addWidget(self.Hello)

        layout1 = QHBoxLayout()
        self.username = QLabel("Username:")
        layout1.addWidget(self.username)

        self.username_input = QLineEdit()
        self.username_input.setPlaceholderText("Username")
        layout1.addWidget(self.username_input)

        layout2 = QHBoxLayout()
        self.PW = QLabel("PassWord :")
        layout2.addWidget(self.PW)

        self.password_input = QLineEdit()
        self.password_input.setPlaceholderText("Password")
        self.password_input.setEchoMode(QLineEdit.Password)
        layout2.addWidget(self.password_input)

        button_layout = QHBoxLayout()
        self.guest_button = QPushButton("Guest")
        self.login_button = QPushButton("Login")
        self.signup_button = QPushButton("Sign Up")

        self.guest_button.clicked.connect(self.on_guest_button_clicked)
        self.login_button.clicked.connect(self.login)
        self.signup_button.clicked.connect(self.show_signup_page)

        button_layout.addWidget(self.guest_button)
        button_layout.addWidget(self.login_button)
        button_layout.addWidget(self.signup_button)

        layout.addLayout(empty)
        layout.setSpacing(20)
        layout.addLayout(layout1)
        layout.addLayout(layout2)
        layout.addLayout(button_layout)

        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))
        layout.addLayout(center_layout)
        layout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding))

        # Set spacing and remove margins for the center_layout
        center_layout.setSpacing(20)
        center_layout.setContentsMargins(0, 0, 0, 0)

        page.setLayout(layout)

    def init_welcome_page(self, page):
        layout = QVBoxLayout()

        welcome_label = QLabel("Welcome to the Application!")
        layout.addWidget(welcome_label)

        logout_button = QPushButton("Logout")
        logout_button.clicked.connect(self.show_login_page)
        layout.addWidget(logout_button)

        page.setLayout(layout)

    def check(self):
        n1 = self.C1_password_input.text()
        n2 = self.C2_password_input.text()

        if n1 == n2:
            self.show_welcome_page()
        else:
            print("Create Account failed.Password didnt match")

    def show_signup_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def show_welcome_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_login_page(self):
        self.stacked_widget.setCurrentIndex(0)
        username = self.username_input.text()
        password = self.password_input.text()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.default_credentials and self.default_credentials[username] == password:
            self.show_welcome_page()
        else:
            print("Login failed. Incorrect username or password.")

    def on_guest_button_clicked(self):
        print("Guest button clicked")

    # def on_login_button_clicked(self):
    # username = self.username_input.text()
    # password = self.password_input.text()
    # print(f"Login button clicked\nUsername: {username}\nPassword: {password}")

    # def on_signup_button_clicked(self):
    # print("Sign Up button clicked")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoginApp()
    window.show()
    sys.exit(app.exec_())
