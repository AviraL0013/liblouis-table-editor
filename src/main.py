# main.py
import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTabWidget, QFileDialog, QMessageBox
from config import WINDOW_WIDTH, WINDOW_HEIGHT
from components.Menubar import create_menubar
from components.TableEditor import TableEditor

class TableManager(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Liblouis Tables Manager')
        self.resize(WINDOW_WIDTH, WINDOW_HEIGHT)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Create menubar
        menubar = create_menubar(self)

        # Set the menubar
        layout.setMenuBar(menubar)

        # Tab widget for file contents
        self.tab_widget = QTabWidget()
        layout.addWidget(self.tab_widget)

        self.setLayout(layout)

    def add_tab(self, file_name, file_content):
        new_tab = QWidget()
        layout = QVBoxLayout()
        
        # Create an instance of TableEditor
        table_editor = TableEditor()
        table_editor.set_content(file_content)
        
        layout.addWidget(table_editor)
        new_tab.setLayout(layout)
        
        self.tab_widget.addTab(new_tab, file_name)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = TableManager()
    window.show()

    sys.exit(app.exec_())
