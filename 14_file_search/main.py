from pathlib import Path
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QLineEdit,
    QLabel,
    QMessageBox,
    QFileDialog
)



BASE_DIR = Path(__file__).resolve().parent

# GUI WINDOW
class FileSearchApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("File Search App")
        self.resize(500, 400)

        self.setup_ui()

        self.search_mode = "name"
        self.browse_btn.clicked.connect(self.select_folder)

        self.name_btn.clicked.connect(lambda: self.set_mode("name"))
        self.ext_btn.clicked.connect(lambda: self.set_mode("ext"))
        self.size_btn.clicked.connect(lambda: self.set_mode("size"))
        self.content_btn.clicked.connect(lambda: self.set_mode("content"))

        self.search_btn.clicked.connect(self.search_files)

        self.set_mode("name")

    # UI
    def setup_ui(self):

        layout = QVBoxLayout()

        # Title
        title = QLabel("FILE SEARCH TOOL")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("""
            font-size:16px;
            font-weight:bold;
        """)
        layout.addWidget(title)

        layout.addSpacing(10)

        # Folder
        folder_label = QLabel("Folder")
        layout.addWidget(folder_label)

        folder_layout = QHBoxLayout()

        self.folder_input = QLineEdit()
        self.folder_input.setPlaceholderText("Select folder...")

        self.browse_btn = QPushButton("Browse")

        folder_layout.addWidget(self.folder_input)
        folder_layout.addWidget(self.browse_btn)

        layout.addLayout(folder_layout)

        layout.addSpacing(15)

        # Search Type
        search_type = QLabel("Search Type")
        search_type.setStyleSheet("font-weight:bold;")
        layout.addWidget(search_type)

        type_layout = QHBoxLayout()

        self.name_btn = QPushButton("File Name")
        self.ext_btn = QPushButton("Extension")
        self.size_btn = QPushButton("Max Size")
        self.content_btn = QPushButton("Content")

        type_layout.addWidget(self.name_btn)
        type_layout.addWidget(self.ext_btn)
        type_layout.addWidget(self.size_btn)
        type_layout.addWidget(self.content_btn)

        layout.addLayout(type_layout)

        layout.addSpacing(15)

        # Search Box
        search_label = QLabel("Search")
        layout.addWidget(search_label)

        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Enter search value...")
        layout.addWidget(self.search_input)

        layout.addSpacing(10)

        # Search Button
        self.search_btn = QPushButton("Search")
        layout.addWidget(self.search_btn)

        layout.addSpacing(15)

        # Results
        result_label = QLabel("Results")
        result_label.setStyleSheet("font-weight:bold;")
        layout.addWidget(result_label)

        self.result_list = QListWidget()
        layout.addWidget(self.result_list)

        layout.addSpacing(10)

        # Footer
        self.total_label = QLabel("Found: 0 files")
        self.total_label.setAlignment(Qt.AlignRight)
        layout.addWidget(self.total_label)

        self.setLayout(layout)
    
    def set_mode(self, mode):
        self.search_mode = mode

        self.name_btn.setStyleSheet("")
        self.ext_btn.setStyleSheet("")
        self.size_btn.setStyleSheet("")
        self.content_btn.setStyleSheet("")

        style = "background:#2196F3;color:white;font-weight:bold;"

        if mode == "name":
            self.name_btn.setStyleSheet(style)
            self.search_input.setPlaceholderText("Enter file name")

        elif mode == "ext":
            self.ext_btn.setStyleSheet(style)
            self.search_input.setPlaceholderText("Enter extension (.py)")

        elif mode == "size":
            self.size_btn.setStyleSheet(style)
            self.search_input.setPlaceholderText("Enter max size (KB)")

        elif mode == "content":
            self.content_btn.setStyleSheet(style)
            self.search_input.setPlaceholderText("Enter text to search")
    
    def search_files(self):
        folder = self.folder_input.text().strip()

        if not folder:
            folder = str(BASE_DIR / "input")

        path = Path(folder)

        if not path.is_dir():
            QMessageBox.warning(self, "Error", "Folder not found.")
            return

        keyword = self.search_input.text().strip()

        self.result_list.clear()

        count = 0

        try:

            if self.search_mode == "name":

                if not keyword:
                    keyword = "main.py"

                for file in path.rglob("*"):
                    if file.is_file() and file.name == keyword:
                        self.result_list.addItem(
                            f"{file.relative_to(path)} ({file.stat().st_size} bytes)"
                        )
                        count += 1

            elif self.search_mode == "ext":

                if not keyword:
                    keyword = ".py"

                if not keyword.startswith("."):
                    keyword = "." + keyword

                for file in path.rglob("*"):
                    if file.is_file() and file.suffix == keyword:
                        self.result_list.addItem(
                            f"{file.relative_to(path)} ({file.stat().st_size} bytes)"
                        )
                        count += 1

            elif self.search_mode == "size":

                if not keyword:
                    max_size = 300 * 1024
                else:
                    try:
                        max_size = int(keyword) * 1024
                    except ValueError:
                        QMessageBox.warning(
                            self,
                            "Error",
                            "Enter a valid size."
                        )
                        return

                for file in path.rglob("*"):
                    if file.is_file() and file.stat().st_size <= max_size:
                        self.result_list.addItem(
                            f"{file.relative_to(path)} ({file.stat().st_size} bytes)"
                        )
                        count += 1

            elif self.search_mode == "content":

                if not keyword:
                    keyword = "Welcome to the system"

                for file in path.rglob("*"):

                    if not file.is_file():
                        continue

                    try:
                        with file.open("r", encoding="utf-8") as f:

                            if keyword in f.read():
                                self.result_list.addItem(
                                    f"{file.relative_to(path)} ({file.stat().st_size} bytes)"
                                )
                                count += 1

                    except Exception:
                        continue

            self.total_label.setText(f"Found: {count} files")

            if count == 0:
                QMessageBox.information(self, "Search", "No matching files found.")

        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(
            self,
            "Select Folder",
            str(BASE_DIR)
        )

        if folder:
            self.folder_input.setText(folder)

 
    # CLOSE
    def closeEvent(self, event):
        event.accept()


# APP START
app = QApplication(sys.argv)

window = FileSearchApp()
window.show()

sys.exit(app.exec())