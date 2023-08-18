import json
import os
import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QWidget, QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QRadioButton, QPushButton
from PyQt5.QtWidgets import QTextEdit

from respongiver import *

data = {
    "key1": "value1",
    "key2": "value2",
}


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Change The ChatBot')
        self.setGeometry(100, 100, 320, 210)

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

        self.show()

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

        self.show()


class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Chatbot Interface")
        self.setGeometry(100, 100, 800, 600)

        menubar = self.menuBar()
        file_menu = menubar.addMenu("File")

        exit_action = QAction("Exit", self)
        exit_action.triggered.connect(self.close)

        file_menu.addAction(exit_action)
        setting_menu = menubar.addMenu("Configuration")

        setting_action = QAction("Setting", self)
        setting_action.triggered.connect(self.open_setting_window)
        setting_menu.addAction(setting_action)

        # Create a text area for the chat history
        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)

        self.user_input = QTextEdit(self)
        self.send_button = QPushButton("Send", self)
        self.send_button.clicked.connect(self.handle_send_button)

        main_layout = QGridLayout()

        main_layout.addWidget(self.chat_history, 0, 0, 1, 2)  # Chat history spans two columns
        main_layout.addWidget(self.user_input, 1, 0, 1, 1)  # User input field
        main_layout.addWidget(self.send_button, 1, 1, 1, 1)  # "Send" button

        container = QWidget()
        container.setLayout(main_layout)
        # Set the container as the central widget
        self.setCentralWidget(container)
        self.user_input.setMaximumHeight(self.send_button.sizeHint().height())

        self.settings_window = None

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
            self.settings_window = SettingsWindow()
            self.settings_window.show()

    # Didnt Worked After One Time Press

    with open("setting.json", "r") as setting_file:
        data = json.load(setting_file)

    setting = data["model"]


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotWindow()
    window.show()
    sys.exit(app.exec_())
