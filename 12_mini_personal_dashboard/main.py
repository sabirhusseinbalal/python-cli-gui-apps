import sys
import json
import subprocess
from pathlib import Path
from datetime import datetime

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QLabel, QFrame
)

# PATHS
BASE_DIR = Path(__file__).resolve().parent
ROOT = BASE_DIR.parent

todo_py = ROOT / "01_cli_todo_app" / "main.py"
todo_file = ROOT / "01_cli_todo_app" / "data.json"

bookmark_py = ROOT / "08_bookmark_manager" / "main.py"
bookmark_file = ROOT / "08_bookmark_manager" / "data.json"

url_py = ROOT / "09_url_shortener" / "main.py"
url_file = ROOT / "09_url_shortener" / "links.json"

vault_py = ROOT / "10_account_vault_simulator" / "main.py"
vault_file = ROOT / "10_account_vault_simulator" / "vault.json"


# LOAD DATA
def load_data(json_file):
    if json_file.exists():
        try:
            with json_file.open("r", encoding="utf-8") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []


def open_app(py_file):
    subprocess.Popen([sys.executable, str(py_file)])


def line():
    l = QFrame()
    l.setFrameShape(QFrame.HLine)
    return l


# DASHBOARD
class PersonalDashboard(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Personal Dashboard")
        self.resize(360, 520)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.build_ui()

    # UI BUILDER
    def build_ui(self):
        self.build_header()
        self.todo_section()
        self.bookmark_section()
        self.url_section()
        self.vault_section()

        # refresh button ONLY ONCE (important)
        refresh_btn = QPushButton("Refresh")
        refresh_btn.clicked.connect(self.refresh_dashboard)
        self.layout.addWidget(refresh_btn)

    # HEADER
    def build_header(self):
        today = datetime.today()

        title = QLabel("PERSONAL DASHBOARD")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("font-size:16px;font-weight:bold;")

        self.layout.addWidget(title)
        self.layout.addWidget(QLabel("TODAY"))
        self.layout.addWidget(QLabel(today.strftime("%d %B %Y")))
        self.layout.addWidget(QLabel(today.strftime("%A")))
        self.layout.addWidget(line())

    # TOD0
    def todo_section(self):
        self.layout.addWidget(QLabel("TODO"))

        btn = QPushButton("Open Todo")
        btn.clicked.connect(lambda: open_app(todo_py))
        self.layout.addWidget(btn)

        data = load_data(todo_file)

        pending = sum(1 for x in data if x.get("status") == "pending")
        done = sum(1 for x in data if x.get("status") == "completed")

        self.layout.addWidget(QLabel(f"Pending: {pending}"))
        self.layout.addWidget(QLabel(f"Completed: {done}"))
        self.layout.addWidget(line())

    # BOOKMARK
    def bookmark_section(self):
        self.layout.addWidget(QLabel("BOOKMARKS"))

        btn = QPushButton("Open Bookmark")
        btn.clicked.connect(lambda: open_app(bookmark_py))
        self.layout.addWidget(btn)

        data = load_data(bookmark_file)
        self.layout.addWidget(QLabel(f"Saved: {len(data)}"))
        self.layout.addWidget(line())

    # URL
    def url_section(self):
        self.layout.addWidget(QLabel("URL SHORTENER"))

        btn = QPushButton("Open URL Tool")
        btn.clicked.connect(lambda: open_app(url_py))
        self.layout.addWidget(btn)

        data = load_data(url_file)
        self.layout.addWidget(QLabel(f"Saved: {len(data)}"))
        self.layout.addWidget(line())

    # VAULT
    def vault_section(self):
        self.layout.addWidget(QLabel("VAULT"))

        btn = QPushButton("Open Vault")
        btn.clicked.connect(lambda: open_app(vault_py))
        self.layout.addWidget(btn)

        data = load_data(vault_file)
        self.layout.addWidget(QLabel(f"Accounts: {len(data)}"))
        self.layout.addWidget(line())

    # REFRESH
    def refresh_dashboard(self):

        # clear UI
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget:
                widget.deleteLater()

        # rebuild
        self.build_ui()


# RUN 
app = QApplication(sys.argv)
window = PersonalDashboard()
window.show()
sys.exit(app.exec())