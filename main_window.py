from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QDesktopWidget, QTextEdit, QPushButton, QHBoxLayout
import sys

import generate_smali_code

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        self.origin_text_edit = None
        self.trans_text_edit = None
        self.init_widget()
        self.restore_input()

    def move_center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def init_widget(self):
        self.setGeometry(0,0,800,600)
        self.setWindowTitle("easy_smali")

        self.origin_text_edit = QTextEdit()

        sub_layout = QHBoxLayout()
        generate_button = QPushButton()
        restore_button = QPushButton()
        generate_button.setFixedWidth(80)
        restore_button.setFixedWidth(80)
        generate_button.setText("Generate")
        restore_button.setText("Input")
        generate_button.clicked.connect(self.generate_smali_code)
        restore_button.clicked.connect(self.restore_input)
        sub_layout.addStretch(1)
        sub_layout.addWidget(restore_button)
        sub_layout.addWidget(generate_button)

        self.trans_text_edit = QTextEdit()
        # self.trans_text_edit.setEnabled(False)

        layout = QVBoxLayout()
        layout.addWidget(self.origin_text_edit)
        layout.addLayout(sub_layout)
        layout.addWidget(self.trans_text_edit)

        self.setLayout(layout)
        self.move_center()
        self.show()

    def generate_smali_code(self):
        with open('res/Test.java', 'w') as fw:
            fw.write(self.origin_text_edit.toPlainText())
        # self.origin_text_edit.setEnabled(False)
        generate_smali_code.GenerateSmali().generate_smali_code()
        with open('res/output/Test.smali', 'r') as fr:
            self.trans_text_edit.setPlainText(str(fr.read()))

    def restore_input(self):
        # self.origin_text_edit.setEnabled(True)
        self.origin_text_edit.clear()
        self.trans_text_edit.clear()
        with open('res/template', 'r') as fr:
            self.origin_text_edit.setPlainText(str(fr.read()))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWidget = MyWidget()
    sys.exit(app.exec_())