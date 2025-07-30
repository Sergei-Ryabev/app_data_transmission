import sys

from PySide6.QtWidgets import QApplication

from services.main_window import MainWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())