from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from constants import MIN_MESH_DISTANCE


class NoPatchSelectedDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.botao = QPushButton("Ok", self)
        self.botao.clicked.connect(self.exitDialog)

        self.label = QLabel("No Patch Selected")

        self.line = QLineEdit()

        self.grid = QGridLayout()

        self.grid.addWidget(self.label, 0, 0)
        self.grid.addWidget(self.botao, 1, 0)

        self.setLayout(self.grid)

        self.setWindowTitle("ERRO")
        self.setWindowModality(Qt.ApplicationModal)

    def exitDialog(self):
        self.close()


class CreateMeshDialog(QDialog):
    distance = MIN_MESH_DISTANCE

    def __init__(self):
        super().__init__()
        self.botaoPontos = QPushButton("Ok", self)
        self.botaoCancelar = QPushButton("Cancel", self)

        self.botaoCancelar.clicked.connect(self.exitDialog)
        self.botaoPontos.clicked.connect(self.validateDistance)

        self.label = QLabel(f"Distance Between Points (Default: {MIN_MESH_DISTANCE})")

        self.line = QLineEdit()
        self.line.setText(f"{MIN_MESH_DISTANCE}")

        self.grid = QGridLayout()

        self.grid.addWidget(self.label, 0, 0)
        self.grid.addWidget(self.line, 1, 0)
        self.grid.addWidget(self.botaoPontos, 3, 0)
        self.grid.addWidget(self.botaoCancelar, 4, 0)

        self.setLayout(self.grid)

        self.setWindowTitle("Create Mesh")
        self.setWindowModality(Qt.ApplicationModal)

    def exitDialog(self):
        self.distance = 0
        self.close()

    def setDistance(self):
        self.distance = int(self.line.text())

    def getDistance(self):
        return self.distance

    def validateDistance(self):
        distance = self.line.text()
        if distance.isdigit() and int(distance) >= MIN_MESH_DISTANCE:
            self.setDistance()
            self.close()
        else:
            self.errorLabel = QLabel(
                f"Invalid Distance. Distance must be greater than {MIN_MESH_DISTANCE}."
            )
            self.grid.addWidget(self.errorLabel, 2, 0)
