from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QGridLayout, QLineEdit, QPushButton, QHBoxLayout, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

class Calculator(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.interfejs()

    def interfejs(self):

        label_1 = QLabel("number 1:", self)
        label_2 = QLabel("number 2:", self)
        label_3 = QLabel("result:", self)

        table = QGridLayout()
        table.addWidget(label_1, 0, 0)
        table.addWidget(label_2, 0, 1)
        table.addWidget(label_3, 0, 2)

        self.number_1_Edt = QLineEdit()
        self.number_2_Edt = QLineEdit()
        self.result_Edt = QLineEdit()

        self.result_Edt.readonly = True
        self.result_Edt.setToolTip('Give <b>numbers</b> and choose operation...')

        table.addWidget(self.number_1_Edt, 1, 0)
        table.addWidget(self.number_2_Edt, 1, 1)
        table.addWidget(self.result_Edt, 1, 2)

        add_btn = QPushButton("&Add", self)
        subtract_btn = QPushButton("&Subtract", self)
        multiply_btn = QPushButton("&Multiply", self)
        divide_btn = QPushButton("&Divide", self)
        end_btn = QPushButton("&End", self)
        end_btn.resize(end_btn.sizeHint())

        table_H = QHBoxLayout()
        table_H.addWidget(add_btn)
        table_H.addWidget(subtract_btn)
        table_H.addWidget(multiply_btn)
        table_H.addWidget(divide_btn)

        table.addLayout(table_H, 2, 0, 1, 3)
        table.addWidget(end_btn, 3, 0, 1, 3)

        self.setLayout(table)
        end_btn.clicked.connect(self.end)
        add_btn.clicked.connect(self.operation)
        subtract_btn.clicked.connect(self.operation)
        multiply_btn.clicked.connect(self.operation)
        divide_btn.clicked.connect(self.operation)

        self.number_1_Edt.setFocus()
        self.setGeometry(20, 20, 300, 100)
        self.setWindowIcon(QIcon('calculator.png'))
        self.setWindowTitle("simple calculator")
        self.show()

    def end(self):
        self.close()

    def closeEvent(self, event):
        answer = QMessageBox.question(
            self, "Statement",
            "Are you sure, that you finished?",
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No
        )

        if answer == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

    def operation(self):
        sender = self.sender()

        try:
            number_1 = float(self.number_1_Edt.text())
            number_2 = float(self.number_2_Edt.text())
            result = ""

            if sender.text() == "&Add":
                result = number_1 + number_2
            elif sender.text() == "&Subtract":
                result = number_1 - number_2
            elif sender.text() == "&Multiply":
                result = number_1 * number_2
            else:
                try:
                    result = round(number_1/number_2, 9)
                except ZeroDivisionError:
                    QMessageBox.critical(
                        self, "Error", "Dividing by 0 is forbidden!"
                    )
                    return

            self.result_Edt.setText(str(result))

        except ValueError:
            QMessageBox.warning(self, "Error", "Wrong data", QMessageBox.Ok)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
