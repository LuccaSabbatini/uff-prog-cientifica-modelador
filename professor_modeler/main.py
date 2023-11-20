import sys
from PyQt5.QtWidgets import QApplication
from src.window import *


def main():
    app = QApplication(sys.argv)
    gui = MyWindow()
    gui.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()