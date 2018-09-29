from PyQt5.QtWidgets import QApplication, QWidget

class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):
        self.resize(600, 200)
        self.setWindowTitle("simple calculator")
        self.show()

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
