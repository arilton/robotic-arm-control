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

    def set_valor(self, motor, incremento = True):
        valor = int(motor['valor'].value())
        if incremento:
            valor += 10
            valor = motor['max_range'] if valor > motor['max_range'] else valor
        else:
            valor -= 10
            valor = motor['min_range'] if valor < motor['min_range'] else valor
        motor['valor'].setValue(valor)

    def base_incremento(self):
        self.set_valor(self.motores['base'])

    def base_decremento(self):
        self.set_valor(self.motores['base'], False)

    def ombro_incremento(self):
        self.set_valor(self.motores['ombro'])

    def ombro_decremento(self):
        self.set_valor(self.motores['ombro'], False)

    def cotovelo_incremento(self):
        self.set_valor(self.motores['cotovelo'])

    def cotovelo_decremento(self):
        self.set_valor(self.motores['cotovelo'], False)

    def punho_incremento(self):
        self.set_valor(self.motores['punho'])

    def punho_decremento(self):
        self.set_valor(self.motores['punho'], False)

    def garra_incremento(self):
        self.set_valor(self.motores['garra'])

    def garra_decremento(self):
        self.set_valor(self.motores['garra'], False)

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
            motor['valor'].setRange(motor['min_range'], motor['max_range'])
            motor['dial'].setRange(motor['min_range'], motor['max_range'])
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
                'slider': QSlider(Qt.Horizontal),
                'min_range': 45,
                'max_range': 207,
            },
            'ombro': {
                'box': QGroupBox('Motor da Ombro'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (A)'),
                'decremento': QPushButton('Decremento (S)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal),
                'min_range': 108,
                'max_range': 180,
            },
            'cotovelo': {
                'box': QGroupBox('Motor da Cotovelo'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (Z)'),
                'decremento': QPushButton('Decremento (X)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal),
                'min_range': 99,
                'max_range': 189,
            },
            'punho': {
                'box': QGroupBox('Motor da Punho'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (R)'),
                'decremento': QPushButton('Decremento (T)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal),
                'min_range': 45,
                'max_range': 225,
            },
            'garra': {
                'box': QGroupBox('Motor da Garra'),
                'dial': QDial(),
                'incremento': QPushButton('Incremento (F)'),
                'decremento': QPushButton('Decremento (G)'),
                'valor': QSpinBox(),
                'slider': QSlider(Qt.Horizontal),
                'min_range': 117,
                'max_range': 216,
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
