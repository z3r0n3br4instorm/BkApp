import sys
import os
print("Initializing...")
os.system("pip install requests")
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel, QProgressBar
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont

# Function to handle color-coded messages
def log_message(text_edit, message, color="black"):
    text_edit.setTextColor(Qt.black if color == "black" else Qt.green if color == "green" else Qt.red if color == "red" else Qt.blue)
    text_edit.append(message)

class InstallerUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        # Window setup
        self.setWindowTitle("OPD Management System Installer")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        # Header Label
        header_label = QLabel("Princeton Plainsboro Teaching Hospital | Software Department")
        header_label.setAlignment(Qt.AlignCenter)
        header_label.setFont(QFont('Arial', 12, QFont.Bold))
        layout.addWidget(header_label)

        # Log Text Area
        self.log_text_edit = QTextEdit(self)
        self.log_text_edit.setReadOnly(True)
        layout.addWidget(self.log_text_edit)

        # Progress Bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # Install Buttons
        self.install_mongo_button = QPushButton("Download and Install MongoDB", self)
        self.install_mongo_button.clicked.connect(self.install_mongo)
        layout.addWidget(self.install_mongo_button)

        self.install_compass_button = QPushButton("Download and Install MongoDB Compass", self)
        self.install_compass_button.clicked.connect(self.install_compass)
        layout.addWidget(self.install_compass_button)

        self.install_libs_button = QPushButton("Install Required Libraries", self)
        self.install_libs_button.clicked.connect(self.install_libraries)
        layout.addWidget(self.install_libs_button)

        self.install_font_button = QPushButton("Install Space Grotesk Font", self)
        self.install_font_button.clicked.connect(self.install_font)
        layout.addWidget(self.install_font_button)

        self.run_script_button = QPushButton("Run createDoctor.py Script", self)
        self.run_script_button.clicked.connect(self.run_script)
        layout.addWidget(self.run_script_button)

        self.setLayout(layout)

    def download_file(self, url, dest, desc):
        log_message(self.log_text_edit, f"[INFO] Downloading {desc}...", "blue")
        try:
            response = requests.get(url, stream=True)
            total_size = int(response.headers.get('content-length', 0))
            block_size = 1024
            self.progress_bar.setMaximum(total_size)

            with open(dest, 'wb') as file:
                for data in response.iter_content(block_size):
                    file.write(data)
                    self.progress_bar.setValue(self.progress_bar.value() + len(data))

            log_message(self.log_text_edit, f"[SUCCESS] {desc} Downloaded!", "green")
        except Exception as e:
            log_message(self.log_text_edit, f"[ERROR] Failed to download {desc}: {e}", "red")
        self.progress_bar.setValue(0)  # Reset the progress bar after completion

    def install_mongo(self):
        self.download_file(
            "https://fastdl.mongodb.org/windows/mongodb-windows-x86_64-7.0.11-signed.msi",
            "mongodb-windows-x86_64-7.0.11-signed.msi",
            "MongoDB"
        )

    def install_compass(self):
        self.download_file(
            "https://downloads.mongodb.com/compass/mongodb-compass-1.43.1-win32-x64.exe",
            "mongodb-compass-1.43.1-win32-x64.exe",
            "MongoDB Compass"
        )

    def install_libraries(self):
        log_message(self.log_text_edit, "[INFO] Installing Required Libraries...", "blue")
        try:
            os.system("pip install PyQt5 pymongo")
            log_message(self.log_text_edit, "[SUCCESS] Required Libraries Installed!", "green")
        except Exception as e:
            log_message(self.log_text_edit, f"[ERROR] Failed to install libraries: {e}", "red")

    def install_font(self):
        log_message(self.log_text_edit, "[INFO] Installing Space Grotesk Font...", "blue")
        try:
            os.system("start data/SpaceGrotesk-VariableFont_wght.ttf")
            log_message(self.log_text_edit, "[SUCCESS] Font Installation Completed!", "green")
        except Exception as e:
            log_message(self.log_text_edit, f"[ERROR] Failed to install font: {e}", "red")

    def run_script(self):
        log_message(self.log_text_edit, "[INFO] Running 'createDoctor.py'...", "blue")
        try:
            os.system("python createDoctor.py")
            log_message(self.log_text_edit, "[SUCCESS] Script Executed Successfully!", "green")
        except Exception as e:
            log_message(self.log_text_edit, f"[ERROR] Failed to run script: {e}", "red")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    installer = InstallerUI()
    installer.show()
    sys.exit(app.exec_())
