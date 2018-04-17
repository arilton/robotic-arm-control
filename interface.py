#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from PySide.QtGui import *
from PySide.QtCore import *


qt_app = QApplication(sys.argv)

class InterfaceRobotica(QWidget):

    def initial_set(self):
        self.setWindowTitle(u'Robô Garra')
        self.setMinimumWidth(300)
        self.setMinimumHeight(640)

    def base_incremento(self):
        valor = int(self.motores['base']['valor'].value()) + 10
        valor = 360 if valor > 360 else valor 
        self.motores['base']['valor'].setValue(valor)

    def base_decremento(self):
        valor = int(self.motores['base']['valor'].value()) - 10
        valor = 0 if valor < 0 else valor
        self.motores['base']['valor'].setValue(valor)

    def ombro_incremento(self):
        valor = int(self.motores['ombro']['valor'].value()) + 10
        valor = 360 if valor > 360 else valor
        self.motores['ombro']['valor'].setValue(valor)

    def ombro_decremento(self):
        valor = int(self.motores['ombro']['valor'].value()) - 10
        valor = 0 if valor < 0 else valor
        self.motores['ombro']['valor'].setValue(valor)

    def cotovelo_incremento(self):
        valor = int(self.motores['cotovelo']['valor'].value()) + 10
        valor = 360 if valor > 360 else valor
        self.motores['cotovelo']['valor'].setValue(valor)

    def cotovelo_decremento(self):
        valor = int(self.motores['cotovelo']['valor'].value()) - 10
        valor = 0 if valor < 0 else valor
        self.motores['cotovelo']['valor'].setValue(valor)

    def punho_incremento(self):
        valor = int(self.motores['punho']['valor'].value()) + 10
        valor = 360 if valor > 360 else valor
        self.motores['punho']['valor'].setValue(valor)

    def punho_decremento(self):
        valor = int(self.motores['punho']['valor'].value()) - 10
        valor = 0 if valor < 0 else valor
        self.motores['punho']['valor'].setValue(valor)

    def garra_incremento(self):
        valor = int(self.motores['garra']['valor'].value()) + 10
        valor = 360 if valor > 360 else valor
        self.motores['garra']['valor'].setValue(valor)

    def garra_decremento(self):
        valor = int(self.motores['garra']['valor'].value()) - 10
        valor = 0 if valor < 0 else valor
        self.motores['garra']['valor'].setValue(valor)
    

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            self.base_incremento()
        if event.key() == Qt.Key_W:
            self.base_decremento()
        if event.key() == Qt.Key_A:
            self.ombro_incremento()
        if event.key() == Qt.Key_S:
            self.ombro_decremento()
        if event.key() == Qt.Key_Z:
            self.cotovelo_incremento()
        if event.key() == Qt.Key_X:
            self.cotovelo_decremento()
        if event.key() == Qt.Key_R:
            self.punho_incremento()
        if event.key() == Qt.Key_T:
            self.punho_decremento()
        if event.key() == Qt.Key_F:
            self.garra_incremento()
        if event.key() == Qt.Key_G:
            self.garra_decremento()

    def interface_lateral_esquerda(self):
        for nome_motor, motor in self.motores.iteritems():

            motor['valor'].valueChanged.connect(motor['dial'].setValue)
            motor['dial'].valueChanged.connect(motor['valor'].setValue)
            motor['valor'].setRange(0, 360)
            motor['dial'].setRange(0, 360)
            motor['incremento'].clicked.connect(eval('self.' + nome_motor + '_incremento'))
            motor['decremento'].clicked.connect(eval('self.' + nome_motor + '_decremento'))

            hlayout = QHBoxLayout()
            hlayout.addWidget(motor['dial'])
            flayout = QFormLayout()
            flayout.addRow(motor['incremento'])
            flayout.addRow(motor['decremento'])
            flayout.addRow('Valor atual', motor['valor'])
            flayout.addRow('Velocidade', motor['slider'])

            hlayout.addLayout(flayout)
            motor['box'].setLayout(hlayout)
            self.layout_lateral_esquerda.addWidget(motor['box'])

    def definir_layout(self):
        self.layout.addLayout(self.layout_lateral_esquerda)
        self.layout.addLayout(self.layout_central)
        self.setLayout(self.layout)

    def __init__(self):
        QWidget.__init__(self)
        self.initial_set()

        # Definição dos layouts
        self.layout = QHBoxLayout()
        self.layout_lateral_esquerda = QVBoxLayout()
        self.layout_central = QGridLayout()

        # Definição dos motores
        self.motores = {
            'base': {
                'box': QGroupBox('Motor da Base'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (Q)'),
                'decremento': QPushButton('Decremento (W)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal)
            },
            'ombro': {
                'box': QGroupBox('Motor da Ombro'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (A)'),
                'decremento': QPushButton('Decremento (S)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal)
            },
            'cotovelo': {
                'box': QGroupBox('Motor da Cotovelo'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (Z)'),
                'decremento': QPushButton('Decremento (X)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal)
            },
            'punho': {
                'box': QGroupBox('Motor da Punho'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (R)'),
                'decremento': QPushButton('Decremento (T)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal)
            },
            'garra': {
                'box': QGroupBox('Motor da Garra'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (F)'),
                'decremento': QPushButton('Decremento (G)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal)
            },
        }

        self.interface_lateral_esquerda()

        self.definir_layout()

    def run(self):
        # Show the form
        self.show()
        # Run the qt application
        qt_app.exec_()

app = InterfaceRobotica()
app.run()
