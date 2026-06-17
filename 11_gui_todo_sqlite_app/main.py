import sys
import sqlite3
from pathlib import Path

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QListWidget,
    QLineEdit,
    QMessageBox
)


# DATABASE
BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "todo.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT DEFAULT 'Pending'
)
""")

conn.commit()


# GUI WINDOW
class TodoApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Todo App")
        self.resize(500, 400)

        self.setup_ui()
        self.load_tasks()

    # UI
    def setup_ui(self):

        layout = QVBoxLayout()

        # Input
        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter task...")
        layout.addWidget(self.task_input)

        # Buttons
        button_layout = QHBoxLayout()

        self.add_btn = QPushButton("Add")
        self.complete_btn = QPushButton("Complete")
        self.delete_btn = QPushButton("Delete")

        button_layout.addWidget(self.add_btn)
        button_layout.addWidget(self.complete_btn)
        button_layout.addWidget(self.delete_btn)

        layout.addLayout(button_layout)

        # Task List
        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        self.setLayout(layout)

        # Signals
        self.add_btn.clicked.connect(self.add_task)
        self.complete_btn.clicked.connect(self.complete_task)
        self.delete_btn.clicked.connect(self.delete_task)

    # LOAD TASKS
    def load_tasks(self):

        self.task_list.clear()

        cursor.execute(
            "SELECT id, task, status FROM tasks"
        )

        tasks = cursor.fetchall()

        for task_id, task, status in tasks:
            self.task_list.addItem(
                f"{task_id} | {task} | {status}"
            )

    # ADD TASK
    def add_task(self):

        task = self.task_input.text().strip()

        if not task:
            QMessageBox.warning(
                self,
                "Error",
                "Task cannot be empty!"
            )
            return

        cursor.execute(
            "INSERT INTO tasks (task) VALUES (?)",
            (task,)
        )

        conn.commit()

        self.task_input.clear()
        self.load_tasks()

    # GET SELECTED TASK ID
    def get_selected_task_id(self):

        item = self.task_list.currentItem()

        if not item:
            QMessageBox.warning(
                self,
                "Error",
                "Please select a task!"
            )
            return None

        return int(
            item.text().split("|")[0].strip()
        )

    # COMPLETE TASK
    def complete_task(self):

        task_id = self.get_selected_task_id()

        if task_id is None:
            return

        cursor.execute(
            """
            UPDATE tasks
            SET status = 'Completed'
            WHERE id = ?
            """,
            (task_id,)
        )

        conn.commit()
        self.load_tasks()

    # DELETE TASK
    def delete_task(self):

        task_id = self.get_selected_task_id()

        if task_id is None:
            return

        reply = QMessageBox.question(
            self,
            "Delete Task",
            "Are you sure you want to delete this task?",
            QMessageBox.Yes | QMessageBox.No
        )

        if reply == QMessageBox.No:
            return

        cursor.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )

        conn.commit()
        self.load_tasks()

    # CLOSE DATABASE ON EXIT
    def closeEvent(self, event):

        conn.close()
        event.accept()


# APP START
app = QApplication(sys.argv)

window = TodoApp()
window.show()

sys.exit(app.exec())