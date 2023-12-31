import json
import os
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QWidget, QHBoxLayout, QGridLayout, QAction, \
    QLabel, QRadioButton, QPushButton
from PyQt5.QtWidgets import QLineEdit, QVBoxLayout, \
    QSpacerItem, QSizePolicy, QStackedWidget

from respongiver import *

data = {
    "key1": "value1",
    "key2": "value2",
}


# self.show()


class ChatbotApp(QMainWindow):
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

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        login_page = QWidget()
        welcome_page = QWidget()
        signup_page = QWidget()
        Chatbot_page = QWidget()

        self.stacked_widget.setCurrentIndex(0)
        self.stacked_widget.addWidget(login_page)
        self.stacked_widget.addWidget(welcome_page)
        self.stacked_widget.addWidget(signup_page)
        self.stacked_widget.addWidget(Chatbot_page)

        self.init_login_page(login_page)
        self.init_welcome_page(welcome_page)
        self.init_signup_page(signup_page)
        self.init_Chatbot_page(Chatbot_page)

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

    def on_guest_button_clicked(self):
        print("Guest button clicked")

    class SettingsWindow(QWidget):
        def __init__(self):
            super().__init__()
            self.setWindowTitle('Change The ChatBot')
            self.setGeometry(100, 100, 320, 210)

            self.settings_window = None

            # create a grid layout
            layout = QGridLayout()
            self.setLayout(layout)

            text = QLabel("Change The Chatbot Module", self)

            rb_Inbuild = QRadioButton('Inbuild', self)
            rb_Inbuild.toggled.connect(self.update)

            rb_ChatGPT = QRadioButton('ChatGPT(Openai)', self)
            rb_ChatGPT.toggled.connect(self.update)

            rb_Bard = QRadioButton('Bard', self)
            rb_Bard.toggled.connect(self.update)

            self.result_label = QLabel('', self)

            apply_bt = QPushButton("Apply", self)
            apply_bt.clicked.connect(self.hide1)

            layout.addWidget(text)
            layout.addWidget(rb_Inbuild)
            layout.addWidget(rb_ChatGPT)
            layout.addWidget(rb_Bard)
            layout.addWidget(self.result_label)

            # self.show()

        def hide1(self):
            self.hide()

        def update(self):
            # get the radio button the send the signal
            rb = self.sender()

            # check if the radio button is checked
            if rb.isChecked():
                self.result_label.setText(f'You selected {rb.text()}')
                print((rb.text()))
            data = {
                "model": rb.text(),
            }
            with open("setting.json", "w") as json_file:
                json.dump(data, json_file)

    def init_Chatbot_page(self, page):

        self.setWindowTitle("Chatbot Interface")

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)
        setting_menu = menubar.addMenu("Configuration")

        setting_action = QAction("Setting", self)
        setting_action.triggered.connect(self.open_setting_window)
        setting_menu.addAction(setting_action)

        layout = QVBoxLayout()
        # Create a text area for the chat history
        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)
        layout.addWidget(self.chat_history)

        layout1 = QHBoxLayout()

        self.user_input = QTextEdit(self)
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.handle_send_button)
        layout1.addWidget(self.user_input)
        layout1.addWidget(self.send_button)

        layout.addLayout(layout1)
        page.setLayout(layout)



    def handle_send_button(self):
        user_message = self.user_input.toPlainText().strip()
        user_input = user_message
        print(user_input)

        res1 = process(user_message)
        res1 = str(res1)

        user_message_formatted = "You: " + user_message
        self.chat_history.append(user_message_formatted)

        if res1 is not None:
            bot_response = "Bot: " + res1
        else:
            bot_response = "Bot: Sorry, I didn't get it."
        bot_response = "Bot: " + res1

        self.chat_history.append(bot_response)
        self.user_input.clear()

        u_chat = {
            "Q": user_message,
            "A": bot_response,
        }

        if os.path.exists("config.json"):
            with open("config.json", "a") as json_file:
                json.dump(u_chat, json_file, indent=4)
        else:
            with open("config.json", "w") as json_file:
                json.dump(u_chat, json_file, indent=4)

    def open_setting_window(self):
        if not self.settings_window:
            self.settings_window = self.SettingsWindow()  # Create an instance of SettingsWindow
        self.settings_window.show()

    # Didnt Worked After One Time Press

    with open("setting.json", "r") as setting_file:
        data = json.load(setting_file)

    setting = data["model"]

    def show_login_page(self):
        self.stacked_widget.setCurrentIndex(0)
        username = self.username_input.text()
        password = self.password_input.text()

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()

        if username in self.default_credentials and self.default_credentials[username] == password:
            self.show_welcome_page()
            self.stacked_widget.setCurrentIndex(3)

        else:
            print("Login failed. Incorrect username or password.")

    def show_welcome_page(self):
        self.stacked_widget.setCurrentIndex(1)

    def show_signup_page(self):
        self.stacked_widget.setCurrentIndex(2)

    def check(self):
        n1 = self.C1_password_input.text()
        n2 = self.C2_password_input.text()

        if n1 == n2:
            self.ChatbotShowUp()
        else:
            print("Create Account failed.Password didnt match")

    def ChatbotShowUp(self):
        self.stacked_widget.setCurrentIndex(3)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotApp()
    window.show()
    sys.exit(app.exec_())
