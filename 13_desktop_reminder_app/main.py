import sys
import sqlite3
from pathlib import Path
from datetime import datetime, timedelta

from plyer import notification
from PySide6.QtCore import QTimer, Qt
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QPushButton, QListWidget, QLineEdit,
    QMessageBox, QLabel
)

# DATABASE
BASE_DIR = Path(__file__).resolve().parent
DB_FILE = BASE_DIR / "list.db"

conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    target_time TEXT NOT NULL,
    status TEXT DEFAULT 'Waiting'
)
""")
conn.commit()


class ReminderApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Desktop Reminder App")
        self.resize(500, 400)

        self.setup_ui()
        self.load_tasks()
        self.update_stats()

        # auto check every second
        self.timer = QTimer()
        self.timer.timeout.connect(self.check_reminders)
        self.timer.start(1000)

    # UI
    def setup_ui(self):

        layout = QVBoxLayout()

        self.stats_label = QLabel()
        self.stats_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.stats_label)

        self.task_input = QLineEdit()
        self.task_input.setPlaceholderText("Enter title...")
        layout.addWidget(self.task_input)

        self.minutes_input = QLineEdit()
        self.minutes_input.setPlaceholderText("Enter minutes...")
        layout.addWidget(self.minutes_input)

        self.task_list = QListWidget()
        layout.addWidget(self.task_list)

        add_btn = QPushButton("Add")
        delete_btn = QPushButton("Delete")

        add_btn.clicked.connect(self.add_task)
        delete_btn.clicked.connect(self.delete_task)

        layout.addWidget(add_btn)
        layout.addWidget(delete_btn)

        self.setLayout(layout)

    # LOAD
    def load_tasks(self):

        self.task_list.clear()

        cursor.execute("SELECT id, title, target_time, status FROM tasks")
        tasks = cursor.fetchall()

        for t in tasks:
            self.task_list.addItem(f"{t[0]} | {t[1]} | {t[2]} | {t[3]}")

    # STATS
    def update_stats(self):

        cursor.execute("SELECT status FROM tasks")
        rows = cursor.fetchall()

        waiting = 0
        completed = 0

        for (status,) in rows:
            if status == "Waiting":
                waiting += 1
            else:
                completed += 1

        total = waiting + completed

        self.stats_label.setText(
            f"Waiting: {waiting} | Completed: {completed} | Total: {total}"
        )

    # ADD
    def add_task(self):

        title = self.task_input.text().strip()
        minutes = self.minutes_input.text().strip()

        if not title:
            QMessageBox.warning(self, "Error", "Title cannot be empty")
            return

        try:
            minutes = int(minutes)
            if minutes <= 0:
                raise ValueError
        except:
            QMessageBox.warning(self, "Error", "Invalid minutes")
            return

        target_time = datetime.now() + timedelta(minutes=minutes)

        cursor.execute("""
            INSERT INTO tasks (title, target_time)
            VALUES (?, ?)
        """, (title, target_time.strftime("%Y-%m-%d %H:%M:%S")))

        conn.commit()

        self.task_input.clear()
        self.minutes_input.clear()

        self.load_tasks()
        self.update_stats()

    # DELETE
    def delete_task(self):

        item = self.task_list.currentItem()

        if not item:
            QMessageBox.warning(self, "Error", "Select a task first")
            return

        task_id = int(item.text().split("|")[0].strip())

        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()

        self.load_tasks()
        self.update_stats()

    # CHECK REMINDERS
    def check_reminders(self):

        cursor.execute("SELECT id, title, target_time, status FROM tasks")
        tasks = cursor.fetchall()

        now = datetime.now()
        updated = False

        for task_id, title, target_time, status in tasks:

            if status != "Waiting":
                continue

            target = datetime.strptime(target_time, "%Y-%m-%d %H:%M:%S")

            if now >= target:

                cursor.execute("""
                    UPDATE tasks
                    SET status = 'Completed'
                    WHERE id = ?
                """, (task_id,))

                conn.commit()

                notification.notify(
                    title=title,
                    message="Reminder Time!",
                    timeout=5
                )

                updated = True

        if updated:
            self.load_tasks()
            self.update_stats()

    # CLOSE
    def closeEvent(self, event):
        conn.close()
        event.accept()


# RUN
app = QApplication(sys.argv)
window = ReminderApp()
window.show()
sys.exit(app.exec())