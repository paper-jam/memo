# pylint: disable=C0103, C0114, C0116,C0115, R0903, C0304
import sys
from PySide6.QtWidgets import QPushButton, QHBoxLayout, QWidget, QApplication

class MainUi(QWidget):

    def __init__(self):
        super().__init__()

        # self.setWindowTitle("My App")
        # button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        # self.setCentralWidget(button)

        self.setWindowTitle('Printer')

        button1 = QPushButton('Print Bonjour!')
        button2 = QPushButton('Print Au revoir!')

        bonjour = lambda x: self.afficher_mot("bonjour ")
        aurevoir = lambda x: self.afficher_mot("au revoir ")

        button1.clicked.connect(bonjour)
        button2.clicked.connect(aurevoir)

        main_layout = QHBoxLayout()
        main_layout.addWidget(button1)
        main_layout.addWidget(button2)

        self.setLayout(main_layout)

    def afficher_mot(self, mot):
        print(mot)


if __name__ == '__main__':
    app = QApplication()
    win = MainUi()
    win.show()
    app.exec()
