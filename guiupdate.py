import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QPushButton, QVBoxLayout, QWidget ,QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenuBar, QWidget, QVBoxLayout, QLabel
from respongiver import *

class SettingsWindow(QWidget):


    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window")
        layout.addWidget(self.label)
        self.setLayout(layout)

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Chatbot Interface")
        self.setGeometry(100, 100, 800, 600)

        menubar =self.menuBar()
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

    def open_setting_window(self):
        if not self.settings_window:
            self.settings_window = SettingsWindow()
            self.settings_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ChatbotWindow()
    window.show()
    sys.exit(app.exec_())