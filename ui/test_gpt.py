import sys
import pandas as pd
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QComboBox, QHBoxLayout

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Process chart')
        self.layout = QVBoxLayout()

        self.addButton = QPushButton('Add')
        self.addButton.clicked.connect(self.addLineEdit)

        self.removeButton = QPushButton('Delete')
        self.removeButton.clicked.connect(self.removeLineEdit)

        self.confirmButton = QPushButton('Done')
        self.confirmButton.clicked.connect(self.confirmData)

        self.layout.addWidget(self.addButton)
        self.layout.addWidget(self.removeButton)
        self.layout.addWidget(self.confirmButton)

        self.setLayout(self.layout)

        self.lineEdits = []

    def addLineEdit(self):
        lineEdit = QLineEdit()
        comboBox = QComboBox()
        comboBox.addItems(["Operation", "Inspection", "Transport", "Delay", "Storage"])

        # นำ LineEdit และ ComboBox มาใส่ใน QHBoxLayout เพื่อให้ติดกันในแนวนอน
        hbox = QHBoxLayout()
        hbox.addWidget(lineEdit)
        hbox.addWidget(comboBox)

        self.lineEdits.append(hbox)
        self.layout.addLayout(hbox)

    def removeLineEdit(self):
        if self.lineEdits:
            layoutItem = self.lineEdits.pop()
            # ลบ Layout ของ LineEdit และ ComboBox
            for i in reversed(range(layoutItem.count())):
                widget = layoutItem.itemAt(i).widget()
                if widget is not None:
                    widget.deleteLater()
            layoutItem.deleteLater()

    def confirmData(self):
        data = []
        for hbox in self.lineEdits:
            lineEdit = hbox.itemAt(0).widget()  # ดึง LineEdit ออกมาจาก QHBoxLayout
            comboBox = hbox.itemAt(1).widget()  # ดึง ComboBox ออกมาจาก QHBoxLayout
            text = lineEdit.text()
            operation = comboBox.currentText()
            data.append([text, operation])
        df = pd.DataFrame(data, columns=["Data", "Operation"])
        print(df)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    widget.show()
    sys.exit(app.exec_())