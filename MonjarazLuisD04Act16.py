# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ps.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# Creadores: Jaime Adalberto Lomeli Navarro, Luis Fernando Monjaraz Briseño
# Maestra: Violeta del Rocío Beceera Velázquez
# Materia: Sistemas Operativos


from PyQt5 import QtCore, QtGui, QtWidgets, QtTest
from PyQt5.QtCore import Qt
import random
from PyQt5.QtWidgets import (QApplication, QWidget)
from PyQt5.Qt import Qt
import keyboard
from bcp import *
from PyQt5.QtCore import QTimer, Qt

keyboard.block_key('tab')
keyboard.block_key('space')

class Ui_widget(object):
    def setupUi(self, widget):
        widget.setObjectName("widget")
        widget.resize(1921, 1019)
        widget.setStyleSheet("QWidget#widget{\n"
                    "background-color: rgb(255, 239, 213);}")
        self.label = QtWidgets.QLabel(widget)
        self.label.setGeometry(QtCore.QRect(660, 10, 291, 40))
        self.label.setStyleSheet("font: 20pt \"Algerian\";\n"
"background-color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(widget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 221, 31))
        self.label_2.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.proces = QtWidgets.QLineEdit(widget)
        self.proces.setGeometry(QtCore.QRect(240, 30, 71, 31))
        self.proces.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.proces.setText("")
        self.proces.setObjectName("proces")
        self.iniciar = QtWidgets.QPushButton(widget)
        self.iniciar.setGeometry(QtCore.QRect(320, 70, 141, 31))
        self.iniciar.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.iniciar.setObjectName("iniciar")
        
        self.iniciar.clicked.connect(self.pedirProcesos)
        self.iniciar.clicked.connect(self.inicio)
        self.iniciar.clicked.connect(self.start_stop_func)
        
        self.label_3 = QtWidgets.QLabel(widget)
        self.label_3.setGeometry(QtCore.QRect(90, 160, 177, 31))
        self.label_3.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_3.setObjectName("label_3")
        self.Nuevos = QtWidgets.QLabel(widget)
        self.Nuevos.setGeometry(QtCore.QRect(280, 160, 131, 31))
        self.Nuevos.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.Nuevos.setText("")
        self.Nuevos.setObjectName("Nuevos")
        self.label_4 = QtWidgets.QLabel(widget)
        self.label_4.setGeometry(QtCore.QRect(160, 460, 137, 31))
        self.label_4.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.tablaListos = QtWidgets.QTableWidget(widget)
        self.tablaListos.setGeometry(QtCore.QRect(20, 500, 421, 231))
        self.tablaListos.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.tablaListos.setObjectName("tablaListos")
        self.tablaListos.setColumnCount(3)
        self.tablaListos.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListos.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListos.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tablaListos.setHorizontalHeaderItem(2, item)
        self.label_5 = QtWidgets.QLabel(widget)
        self.label_5.setGeometry(QtCore.QRect(620, 80, 215, 31))
        self.label_5.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(widget)
        self.label_6.setGeometry(QtCore.QRect(550, 130, 244, 27))
        self.label_6.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(widget)
        self.label_7.setGeometry(QtCore.QRect(610, 170, 187, 27))
        self.label_7.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(widget)
        self.label_8.setGeometry(QtCore.QRect(560, 210, 239, 27))
        self.label_8.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_8.setObjectName("label_8")
        self.ID = QtWidgets.QLabel(widget)
        self.ID.setGeometry(QtCore.QRect(810, 130, 121, 31))
        self.ID.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.ID.setText("")
        self.ID.setObjectName("ID")
        self.oper = QtWidgets.QLabel(widget)
        self.oper.setGeometry(QtCore.QRect(810, 170, 121, 31))
        self.oper.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.oper.setText("")
        self.oper.setObjectName("oper")
        self.label_9 = QtWidgets.QLabel(widget)
        self.label_9.setGeometry(QtCore.QRect(610, 250, 191, 27))
        self.label_9.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(widget)
        self.label_10.setGeometry(QtCore.QRect(650, 290, 151, 27))
        self.label_10.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_10.setObjectName("label_10")
        self.tme = QtWidgets.QLabel(widget)
        self.tme.setGeometry(QtCore.QRect(810, 210, 121, 31))
        self.tme.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.tme.setText("")
        self.tme.setObjectName("tme")
        self.tt = QtWidgets.QLabel(widget)
        self.tt.setGeometry(QtCore.QRect(810, 250, 121, 31))
        self.tt.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.tt.setText("")
        self.tt.setObjectName("tt")
        self.tr = QtWidgets.QLabel(widget)
        self.tr.setGeometry(QtCore.QRect(810, 290, 121, 31))
        self.tr.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.tr.setText("")
        self.tr.setObjectName("tr")
        self.label_11 = QtWidgets.QLabel(widget)
        self.label_11.setGeometry(QtCore.QRect(100, 740, 217, 31))
        self.label_11.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_11.setObjectName("label_11")
        self.bloqueados = QtWidgets.QTableWidget(widget)
        self.bloqueados.setGeometry(QtCore.QRect(60, 770, 311, 231))
        self.bloqueados.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.bloqueados.setObjectName("bloqueados")
        self.bloqueados.setColumnCount(2)
        self.bloqueados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.bloqueados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.bloqueados.setHorizontalHeaderItem(1, item)
        self.label_12 = QtWidgets.QLabel(widget)
        self.label_12.setGeometry(QtCore.QRect(640, 400, 215, 31))
        self.label_12.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.label_12.setObjectName("label_12")
        self.Terminados = QtWidgets.QTableWidget(widget)
        self.Terminados.setGeometry(QtCore.QRect(530, 440, 421, 531))
        self.Terminados.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.Terminados.setObjectName("Terminados")
        self.Terminados.setColumnCount(3)
        self.Terminados.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.Terminados.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.Terminados.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.Terminados.setHorizontalHeaderItem(2, item)
        self.label_13 = QtWidgets.QLabel(widget)
        self.label_13.setGeometry(QtCore.QRect(400, 20, 57, 31))
        self.label_13.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_13.setObjectName("label_13")
        self.reloj = QtWidgets.QLabel(widget)
        self.reloj.setGeometry(QtCore.QRect(470, 20, 101, 31))
        self.reloj.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.reloj.setText("")
        self.reloj.setObjectName("reloj")
        self.quant = QtWidgets.QLineEdit(widget)
        self.quant.setGeometry(QtCore.QRect(240, 70, 71, 31))
        self.quant.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.quant.setText("")
        self.quant.setObjectName("quant")
        self.label_14 = QtWidgets.QLabel(widget)
        self.label_14.setGeometry(QtCore.QRect(120, 70, 111, 31))
        self.label_14.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(widget)
        self.label_15.setGeometry(QtCore.QRect(710, 330, 91, 27))
        self.label_15.setStyleSheet("font: 12pt \"Times New Roman\";")
        self.label_15.setObjectName("label_15")
        self.quantLab = QtWidgets.QLabel(widget)
        self.quantLab.setGeometry(QtCore.QRect(810, 330, 121, 31))
        self.quantLab.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.quantLab.setText("")
        self.quantLab.setObjectName("quantLab")
        self.valorQuant = QtWidgets.QLabel(widget)
        self.valorQuant.setGeometry(QtCore.QRect(280, 120, 131, 31))
        self.valorQuant.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.valorQuant.setText("")
        self.valorQuant.setObjectName("valorQuant")
        self.label_16 = QtWidgets.QLabel(widget)
        self.label_16.setGeometry(QtCore.QRect(66, 120, 201, 31))
        self.label_16.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(widget)
        self.label_17.setGeometry(QtCore.QRect(130, 210, 191, 31))
        self.label_17.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_17.setObjectName("label_17")
        self.Nuevos_2 = QtWidgets.QLabel(widget)
        self.Nuevos_2.setGeometry(QtCore.QRect(70, 250, 51, 31))
        self.Nuevos_2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.Nuevos_2.setText("")
        self.Nuevos_2.setObjectName("Nuevos_2")
        self.Nuevos_3 = QtWidgets.QLabel(widget)
        self.Nuevos_3.setGeometry(QtCore.QRect(240, 250, 61, 31))
        self.Nuevos_3.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.Nuevos_3.setText("")
        self.Nuevos_3.setObjectName("Nuevos_3")
        self.label_18 = QtWidgets.QLabel(widget)
        self.label_18.setGeometry(QtCore.QRect(20, 250, 41, 31))
        self.label_18.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(widget)
        self.label_19.setGeometry(QtCore.QRect(140, 250, 91, 31))
        self.label_19.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_19.setObjectName("label_19")
        self.tableWidget = QtWidgets.QTableWidget(widget)
        self.tableWidget.setGeometry(QtCore.QRect(980, 10, 431, 981))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(25)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.tableWidget_2 = QtWidgets.QTableWidget(widget)
        self.tableWidget_2.setGeometry(QtCore.QRect(1450, 10, 431, 981))
        self.tableWidget_2.setObjectName("tableWidget_2")
        self.tableWidget_2.setColumnCount(3)
        self.tableWidget_2.setRowCount(25)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(19, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(20, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(21, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(22, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(23, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setVerticalHeaderItem(24, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, item)
        self.label_20 = QtWidgets.QLabel(widget)
        self.label_20.setGeometry(QtCore.QRect(980, 20, 41, 16))
        self.label_20.setObjectName("label_20")
        self.label_21 = QtWidgets.QLabel(widget)
        self.label_21.setGeometry(QtCore.QRect(1450, 20, 41, 16))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(widget)
        self.label_22.setGeometry(QtCore.QRect(320, 250, 91, 31))
        self.label_22.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_22.setObjectName("label_22")
        self.Nuevos_4 = QtWidgets.QLabel(widget)
        self.Nuevos_4.setGeometry(QtCore.QRect(420, 250, 61, 31))
        self.Nuevos_4.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.Nuevos_4.setText("")
        self.Nuevos_4.setObjectName("Nuevos_4")
        self.label_23 = QtWidgets.QLabel(widget)
        self.label_23.setGeometry(QtCore.QRect(130, 290, 191, 31))
        self.label_23.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(widget)
        self.label_24.setGeometry(QtCore.QRect(20, 380, 41, 31))
        self.label_24.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_24.setObjectName("label_24")
        self.disco3 = QtWidgets.QLabel(widget)
        self.disco3.setGeometry(QtCore.QRect(240, 380, 61, 31))
        self.disco3.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.disco3.setText("")
        self.disco3.setObjectName("disco3")
        self.disco2 = QtWidgets.QLabel(widget)
        self.disco2.setGeometry(QtCore.QRect(70, 380, 51, 31))
        self.disco2.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.disco2.setText("")
        self.disco2.setObjectName("disco2")
        self.label_25 = QtWidgets.QLabel(widget)
        self.label_25.setGeometry(QtCore.QRect(320, 380, 91, 31))
        self.label_25.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_25.setObjectName("label_25")
        self.disco4 = QtWidgets.QLabel(widget)
        self.disco4.setGeometry(QtCore.QRect(420, 380, 61, 31))
        self.disco4.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.disco4.setText("")
        self.disco4.setObjectName("disco4")
        self.label_26 = QtWidgets.QLabel(widget)
        self.label_26.setGeometry(QtCore.QRect(140, 380, 91, 31))
        self.label_26.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_26.setObjectName("label_26")
        self.label_27 = QtWidgets.QLabel(widget)
        self.label_27.setGeometry(QtCore.QRect(100, 330, 191, 31))
        self.label_27.setStyleSheet("font: 14pt \"Times New Roman\";")
        self.label_27.setObjectName("label_27")
        self.disco1 = QtWidgets.QLabel(widget)
        self.disco1.setGeometry(QtCore.QRect(300, 330, 51, 31))
        self.disco1.setStyleSheet("font: 14pt \"Times New Roman\";\n"
"background-color: rgb(255, 255, 255);")
        self.disco1.setText("")
        self.disco1.setObjectName("disco1")
        self.label_28 = QtWidgets.QLabel(widget)
        self.label_28.setGeometry(QtCore.QRect(0, 210, 501, 31))
        self.label_28.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_28.setText("")
        self.label_28.setObjectName("label_28")
        self.label_29 = QtWidgets.QLabel(widget)
        self.label_29.setGeometry(QtCore.QRect(0, 290, 501, 31))
        self.label_29.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_29.setText("")
        self.label_29.setObjectName("label_29")
        self.label_30 = QtWidgets.QLabel(widget)
        self.label_30.setGeometry(QtCore.QRect(490, 210, 16, 241))
        self.label_30.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_30.setText("")
        self.label_30.setObjectName("label_30")
        self.label_31 = QtWidgets.QLabel(widget)
        self.label_31.setGeometry(QtCore.QRect(0, 420, 501, 31))
        self.label_31.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_31.setText("")
        self.label_31.setObjectName("label_31")
        self.label_32 = QtWidgets.QLabel(widget)
        self.label_32.setGeometry(QtCore.QRect(0, 210, 16, 241))
        self.label_32.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_32.setText("")
        self.label_32.setObjectName("label_32")
        self.label_33 = QtWidgets.QLabel(widget)
        self.label_33.setGeometry(QtCore.QRect(520, 80, 431, 31))
        self.label_33.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_33.setText("")
        self.label_33.setObjectName("label_33")
        self.label_34 = QtWidgets.QLabel(widget)
        self.label_34.setGeometry(QtCore.QRect(520, 100, 16, 291))
        self.label_34.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_34.setText("")
        self.label_34.setObjectName("label_34")
        self.label_35 = QtWidgets.QLabel(widget)
        self.label_35.setGeometry(QtCore.QRect(940, 80, 16, 311))
        self.label_35.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_35.setText("")
        self.label_35.setObjectName("label_35")
        self.label_36 = QtWidgets.QLabel(widget)
        self.label_36.setGeometry(QtCore.QRect(520, 370, 431, 21))
        self.label_36.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_36.setText("")
        self.label_36.setObjectName("label_36")
        self.label_33.raise_()
        self.label_29.raise_()
        self.label_28.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.proces.raise_()
        self.iniciar.raise_()
        self.label_3.raise_()
        self.Nuevos.raise_()
        self.label_4.raise_()
        self.tablaListos.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.ID.raise_()
        self.oper.raise_()
        self.label_9.raise_()
        self.label_10.raise_()
        self.tme.raise_()
        self.tt.raise_()
        self.tr.raise_()
        self.label_11.raise_()
        self.bloqueados.raise_()
        self.label_12.raise_()
        self.Terminados.raise_()
        self.label_13.raise_()
        self.reloj.raise_()
        self.quant.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.quantLab.raise_()
        self.valorQuant.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.Nuevos_2.raise_()
        self.Nuevos_3.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.tableWidget.raise_()
        self.tableWidget_2.raise_()
        self.label_20.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.Nuevos_4.raise_()
        self.label_23.raise_()
        self.label_24.raise_()
        self.disco3.raise_()
        self.disco2.raise_()
        self.label_25.raise_()
        self.disco4.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.disco1.raise_()
        self.label_30.raise_()
        self.label_31.raise_()
        self.label_32.raise_()
        self.label_34.raise_()
        self.label_35.raise_()
        self.label_36.raise_()

        self.retranslateUi(widget)
        QtCore.QMetaObject.connectSlotsByName(widget)

    def retranslateUi(self, widget):
        _translate = QtCore.QCoreApplication.translate
        widget.setWindowTitle(_translate("widget", "Form"))
        self.label.setText(_translate("widget", "PS Suspendidos"))
        self.label_2.setText(_translate("widget", "Número de procesos:"))
        self.iniciar.setText(_translate("widget", "Iniciar"))
        self.label_3.setText(_translate("widget", "Procesos nuevos:"))
        self.label_4.setText(_translate("widget", "Cola de listos"))
        item = self.tablaListos.horizontalHeaderItem(0)
        item.setText(_translate("widget", "ID"))
        item = self.tablaListos.horizontalHeaderItem(1)
        item.setText(_translate("widget", "TME"))
        item = self.tablaListos.horizontalHeaderItem(2)
        item.setText(_translate("widget", "TT"))
        self.label_5.setText(_translate("widget", "Proceso en ejecución"))
        self.label_6.setText(_translate("widget", "Número de programa (ID):"))
        self.label_7.setText(_translate("widget", "Operación a realizar:"))
        self.label_8.setText(_translate("widget", "Tiempo maximo estimado:"))
        self.label_9.setText(_translate("widget", "Tiempo transcurrido:"))
        self.label_10.setText(_translate("widget", "Tiempo restante:"))
        self.label_11.setText(_translate("widget", "Procesos Bloqueados"))
        item = self.bloqueados.horizontalHeaderItem(0)
        item.setText(_translate("widget", "ID"))
        item = self.bloqueados.horizontalHeaderItem(1)
        item.setText(_translate("widget", "TT"))
        self.label_12.setText(_translate("widget", "Procesos terminados"))
        item = self.Terminados.horizontalHeaderItem(0)
        item.setText(_translate("widget", "ID"))
        item = self.Terminados.horizontalHeaderItem(1)
        item.setText(_translate("widget", "Operación"))
        item = self.Terminados.horizontalHeaderItem(2)
        item.setText(_translate("widget", "Resultado"))
        self.label_13.setText(_translate("widget", "Reloj:"))
        self.label_14.setText(_translate("widget", "Quantum:"))
        self.label_15.setText(_translate("widget", "Quantum:"))
        self.label_16.setText(_translate("widget", "Valor del Quantum:"))
        self.label_17.setText(_translate("widget", "Proceso a entrar"))
        self.label_18.setText(_translate("widget", "ID:"))
        self.label_19.setText(_translate("widget", "Tamaño:"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("widget", "0"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("widget", "1"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("widget", "2"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("widget", "3"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("widget", "4"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("widget", "5"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("widget", "6"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("widget", "7"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("widget", "8"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("widget", "9"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("widget", "10"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("widget", "11"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("widget", "12"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("widget", "13"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("widget", "14"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("widget", "15"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("widget", "16"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("widget", "17"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("widget", "18"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("widget", "19"))
        item = self.tableWidget.verticalHeaderItem(20)
        item.setText(_translate("widget", "20"))
        item = self.tableWidget.verticalHeaderItem(21)
        item.setText(_translate("widget", "21"))
        item = self.tableWidget.verticalHeaderItem(22)
        item.setText(_translate("widget", "22"))
        item = self.tableWidget.verticalHeaderItem(23)
        item.setText(_translate("widget", "23"))
        item = self.tableWidget.verticalHeaderItem(24)
        item.setText(_translate("widget", "24"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("widget", "Tamaño"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("widget", "ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("widget", "Estado"))
        item = self.tableWidget_2.verticalHeaderItem(0)
        item.setText(_translate("widget", "25"))
        item = self.tableWidget_2.verticalHeaderItem(1)
        item.setText(_translate("widget", "26"))
        item = self.tableWidget_2.verticalHeaderItem(2)
        item.setText(_translate("widget", "27"))
        item = self.tableWidget_2.verticalHeaderItem(3)
        item.setText(_translate("widget", "28"))
        item = self.tableWidget_2.verticalHeaderItem(4)
        item.setText(_translate("widget", "29"))
        item = self.tableWidget_2.verticalHeaderItem(5)
        item.setText(_translate("widget", "30"))
        item = self.tableWidget_2.verticalHeaderItem(6)
        item.setText(_translate("widget", "31"))
        item = self.tableWidget_2.verticalHeaderItem(7)
        item.setText(_translate("widget", "32"))
        item = self.tableWidget_2.verticalHeaderItem(8)
        item.setText(_translate("widget", "33"))
        item = self.tableWidget_2.verticalHeaderItem(9)
        item.setText(_translate("widget", "34"))
        item = self.tableWidget_2.verticalHeaderItem(10)
        item.setText(_translate("widget", "35"))
        item = self.tableWidget_2.verticalHeaderItem(11)
        item.setText(_translate("widget", "36"))
        item = self.tableWidget_2.verticalHeaderItem(12)
        item.setText(_translate("widget", "37"))
        item = self.tableWidget_2.verticalHeaderItem(13)
        item.setText(_translate("widget", "38"))
        item = self.tableWidget_2.verticalHeaderItem(14)
        item.setText(_translate("widget", "39"))
        item = self.tableWidget_2.verticalHeaderItem(15)
        item.setText(_translate("widget", "40"))
        item = self.tableWidget_2.verticalHeaderItem(16)
        item.setText(_translate("widget", "41"))
        item = self.tableWidget_2.verticalHeaderItem(17)
        item.setText(_translate("widget", "42"))
        item = self.tableWidget_2.verticalHeaderItem(18)
        item.setText(_translate("widget", "43"))
        item = self.tableWidget_2.horizontalHeaderItem(0)
        item.setText(_translate("widget", "Tamaño"))
        item = self.tableWidget_2.horizontalHeaderItem(1)
        item.setText(_translate("widget", "ID"))
        item = self.tableWidget_2.horizontalHeaderItem(2)
        item.setText(_translate("widget", "Estado"))
        self.label_20.setText(_translate("widget", "Marco"))
        self.label_21.setText(_translate("widget", "Marco"))
        self.label_22.setText(_translate("widget", "Marcos:"))
        self.label_23.setText(_translate("widget", "Procesos en Disco"))
        self.label_24.setText(_translate("widget", "ID:"))
        self.label_25.setText(_translate("widget", "Marcos:"))
        self.label_26.setText(_translate("widget", "Tamaño:"))
        self.label_27.setText(_translate("widget", "Cantidad en disco"))

    def __init__(self):
        self.step = 0                                           
 
        self.timer = QTimer(self)                              
        self.timer.timeout.connect(self.ejecucion)
        
    
    def start_stop_func(self):                      
        if not self.timer.isActive():
            self.timer.start(800)
        else:
            self.timer.stop()
    
    
    bandera = 0
    
    contPros = 0
    
    contTerminados = 1
    terminados = []
    
    contadorGlobal = -1
    otraLista = []
    lisd = []
    cont = 1
    
    listaAux = []
    
    prosBloq = []
    
    
    suspen = []
    
    ids = 1
    
    terminador = 0
    
    listaLotes = []
    
    quantum = 0
    quantum2 = 1
    suma = 0
    suma2 = 0
    memor = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    memor1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    memor2 = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],["5/5","SO","SO"],["5/5","SO","SO"],["5/5","SO","SO"],["5/5","SO","SO"]]
    posicion = 0
    posicion1 = 0
        
    def pedirProcesos(self):
        try:
            proses = int(self.proces.text())
            self.quantum = int(self.quant.text())
            _translate = QtCore.QCoreApplication.translate
            self.proces.setText(_translate("Dialog", ""))
            self.quant.setText(_translate("Dialog", ""))
            
        except ValueError:
            print("El valor ingresado no es un número, vuelva a ingresar")
        contador = 0
        
        tme = 0
        oper = 0
        
        _translate = QtCore.QCoreApplication.translate
        self.valorQuant.setText(_translate("Dialog", str(self.quantum)))
        
        while contador < proses:
            lista = []    
            
            lista.append(self.ids)
            
            tme = random.randint(6, 16)
            lista.append(tme)
            
            lista.append(0)
            
            oper = random.randint(1, 6)
            if oper == 1:
                num1 = random.randint(0, 1000)
                num2 = random.randint(0, 1000)
                operacion = str(num1) + "+" + str(num2)
                resultado = num1 + num2
            elif oper == 2:
                num1 = random.randint(0, 1000)
                num2 = random.randint(0, 1000)
                operacion = str(num1) + "-" + str(num2)
                resultado = num1 - num2
            elif oper == 3:
                num1 = random.randint(-1000, 1000)
                num2 = random.randint(-1000, 1000)
                operacion = str(num1) + "*" + str(num2)
                resultado = num1 * num2
            elif oper == 4:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "/" + str(num2)
                        resultado = round(num1 / num2, 2)
                        break
            elif oper == 5:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "MOD" + str(num2)
                        resultado = num1 % num2
                        break
            elif oper == 6:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "/" + str(num2)
                        resultado = (num1 * num2)/100
                        break


                    
            lista.append(operacion)
            lista.append(resultado)
            
            lista.append(0)
            lista.append(0)
            lista.append(0)
            lista.append("Nuevo")
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
            lista.append(tme)
            
            tamano = random.randint(6, 26)
            lista.append(tamano)
            
            tamano2 = int(tamano/5)
            tamano3 = tamano2
            self.suma = self.suma + tamano2
            if tamano%5 != 0:
                modulo = tamano%5
                self.suma = self.suma + 1
                tamano2 += 1
            else:
                modulo = 0
            lista.append(tamano2)
            
            self.listaLotes.append(lista)
            self.otraLista.append(lista)
            
            if self.suma <= 40:
                self.suma2 = self.suma
                self.listaAux.append(self.otraLista.pop(0))
                while tamano2 > 0:
                    self.memor[self.posicion] = self.ids
                    self.posicion += 1
                    tamano2 -= 1
                
                while tamano3 > 0:
                    self.memor1[self.posicion1] = 5
                    self.posicion1 += 1
                    tamano3 -= 1
                if modulo != 0:
                    self.memor1[self.posicion1] = modulo
                    self.posicion1 += 1

            
            self.ids += 1
            contador += 1
        
            
        
    def terminadoProceso(self):
        if self.lisd == [] and len(self.listaAux) > 0:
            self.quantum2 = 1
            self.lisd = self.listaAux.pop(0)
            try:
                if self.lisd[7] == 0:
                    self.lisd[7] = 1
                    self.lisd[6] = self.contadorGlobal
            except IndexError:
                pass
            
        try:
            if self.lisd[2] != 0:
                self.cont = self.lisd[2] + 1
            else:
                self.cont = 1
        except IndexError:
            pass
        self.terminador = 1
        
        if len(self.listaLotes) == self.contPros:
            self.bcp=QtWidgets.QDialog()
            self.ui=Ui_Form()
            self.ui.setupUi(self.bcp)
            self.bcp.show()
            cuenta = 0
            
            self.ui.BCP.setRowCount(len(self.terminados))
            for i in self.terminados:
                self.ui.BCP.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.ui.BCP.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
                self.ui.BCP.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                self.ui.BCP.setItem(cuenta, 3, QtWidgets.QTableWidgetItem(str(i[3])))
                self.ui.BCP.setItem(cuenta, 4, QtWidgets.QTableWidgetItem(str(i[4])))
                self.ui.BCP.setItem(cuenta, 5, QtWidgets.QTableWidgetItem(str(i[5])))
                self.ui.BCP.setItem(cuenta, 6, QtWidgets.QTableWidgetItem(str(i[6])))
                self.ui.BCP.setItem(cuenta, 7, QtWidgets.QTableWidgetItem(str(i[7])))
                self.ui.BCP.setItem(cuenta, 8, QtWidgets.QTableWidgetItem(str(i[8])))
                self.ui.BCP.setItem(cuenta, 9, QtWidgets.QTableWidgetItem(str(i[9])))
                self.ui.BCP.setItem(cuenta, 10, QtWidgets.QTableWidgetItem(str(i[10])))
                self.ui.BCP.setItem(cuenta, 11, QtWidgets.QTableWidgetItem(str(i[11])))
                cuenta += 1
            self.start_stop_func()
    
    def inicio(self):
        try:
            if self.lisd[2] != 0:
                self.cont = self.lisd[2]
            else:
                self.cont = 1
        except IndexError:
            pass
        self.terminador = 1
        
    def paginacion(self):
        try:
            for x in range(len(self.memor)):
                if self.memor[x] == self.lisd[0]:
                    lisAyuda = []
                    lisAyuda.append(str(self.memor1[x]) +"/5")
                    lisAyuda.append(self.memor[x])
                    lisAyuda.append("Ejecucion")
                    self.memor2[x] = lisAyuda
        except IndexError:
            pass
        try:
            for x in range(len(self.memor)):
                for i in self.listaAux:
                    if self.memor[x] == i[0]:
                        lisAyuda = []
                        lisAyuda.append(str(self.memor1[x]) +"/5")
                        lisAyuda.append(self.memor[x])
                        lisAyuda.append("Listo")
                        self.memor2[x] = lisAyuda
        except IndexError:
            pass
        try:
            for x in range(len(self.memor)):
                for i in self.prosBloq:
                    if self.memor[x] == i[0]:
                        lisAyuda = []
                        lisAyuda.append(str(self.memor1[x]) +"/5")
                        lisAyuda.append(self.memor[x])
                        lisAyuda.append("Bloqueado")
                        self.memor2[x] = lisAyuda
        except IndexError:
            pass
        try:
            for x in range(len(self.memor)):
                if self.memor[x] == 0:
                    lisAyuda = []
                    lisAyuda.append("Libre")
                    lisAyuda.append("Libre")
                    lisAyuda.append("Libre")
                    self.memor2[x] = lisAyuda
        except IndexError:
            pass
            
        #print(self.memor2)
                
        mitad1 = self.memor2[0:25]
        cuenta = 0
        self.tableWidget.setRowCount(len(mitad1))
        for i in mitad1:
            self.tableWidget.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            cuenta += 1
        
        mitad2 = self.memor2[25:]
        cuenta = 0
        self.tableWidget_2.setRowCount(len(mitad2))
        for i in mitad2:
            self.tableWidget_2.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tableWidget_2.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tableWidget_2.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            cuenta += 1
        
    def suspendido(self):
        try:
            listaP = self.prosBloq.pop(0)
            self.suma2 = self.suma2 - listaP[14]
            self.suspen.append(listaP)
            for x in range(len(self.memor)):
                if self.memor[x] == listaP[0]:
                    self.memor[x] = 0
                    self.memor1[x] = 0
            try:
                while True:
                    nuevalis = self.otraLista.pop(0)
                    print(nuevalis)
                    if nuevalis[14] <= 40 - self.suma2:
                        memoria3 = nuevalis[14]
                        memoria4 = nuevalis[13]
                        memoria5 = int(memoria4/5)
                        memoria4 = memoria4%5
                        for x in range(len(self.memor)):
                            if memoria3 == 0:
                                break
                            if self.memor[x] == 0:
                                self.memor[x] = nuevalis[0]
                                if memoria5 > 0:
                                    self.memor1[x] = 5
                                    memoria5 -= 1
                                else:
                                    self.memor1[x] = memoria4
                                memoria3 -= 1

                        self.suma2 = self.suma2 + nuevalis[14]
                        nuevalis[5] = self.contadorGlobal
                        self.listaAux.append(nuevalis)
                    else:
                        self.otraLista = [nuevalis] + self.otraLista
                        break
            except IndexError:
                pass
        except IndexError:
            pass
        
        archivo = open("Procesos en Disco.txt", "w", encoding='utf8')
        try:
            for c in self.suspen:
                archivo.write("ID: ")
                archivo.write(str(c[0]))
                archivo.write("\n")
            archivo.close()
        except:
            pass
        
    def regresar(self):
        try:
            lista = self.suspen.pop(0)
            print(lista)
            
            tamano2 = int(lista[13]/5)
            tamano3 = tamano2
            tamano4 = lista[13]%5
            print(tamano2)
            self.suma = self.suma2
            self.suma = self.suma + tamano2
            if tamano4 != 0:
                self.suma = self.suma + 1
                tamano2 += 1
            if self.suma <= 40:
                self.suma2 = self.suma
                self.prosBloq.append(lista)
                for x in range(len(self.memor)):
                    if tamano2 == 0:
                        break
                    if self.memor[x] == 0:
                        self.memor[x] = lista[0]
                        if tamano3 > 0:
                            self.memor1[x] = 5
                            tamano3 -= 1
                        else:
                            self.memor1[x] = tamano4
                        tamano2 -= 1
            else:
                self.suspen = [lista] + self.suspen
        except IndexError:
            pass
        
        archivo = open("Procesos en Disco.txt", "w", encoding='utf8')
        try:
            for c in self.suspen:
                archivo.write("ID: ")
                archivo.write(str(c[0]))
                archivo.write("\n")
            archivo.close()
        except:
            pass
    
    def ejecucion(self):
        _translate = QtCore.QCoreApplication.translate
        self.step += 1
        if self.bandera == 3:
            self.bandera = 0
            self.start_stop_func()
        elif self.bandera == 6:
            self.bandera = 0
            self.suspendido()
        elif self.bandera == 7:
            self.bandera = 0
            self.regresar()
            
        try:
            listoentrar = self.otraLista[0]
            self.Nuevos_2.setText(_translate("widget", str(listoentrar[0])))
            self.Nuevos_3.setText(_translate("widget", str(listoentrar[13])))
            self.Nuevos_4.setText(_translate("widget", str(listoentrar[14])))
        except IndexError:
            self.Nuevos_2.setText(_translate("widget", str(0)))
            self.Nuevos_3.setText(_translate("widget", str(0)))
            self.Nuevos_4.setText(_translate("widget", str(0)))
            
        try:
            listoentrar = self.suspen[0]
            medida = len(self.suspen)
            self.disco1.setText(_translate("widget", str(medida)))
            self.disco2.setText(_translate("widget", str(listoentrar[0])))
            self.disco3.setText(_translate("widget", str(listoentrar[13])))
            self.disco4.setText(_translate("widget", str(listoentrar[14])))
        except IndexError:
            self.disco1.setText(_translate("widget", str(0)))
            self.disco2.setText(_translate("widget", str(0)))
            self.disco3.setText(_translate("widget", str(0)))
            self.disco4.setText(_translate("widget", str(0)))
            
        for p in self.prosBloq:
            if p[15] == 8:
                p.pop(8)
                self.listaAux.append(p)
                for n in self.prosBloq:
                    if n[0] == p[0]:
                        self.prosBloq.remove(n)
                
        trabajos = len(self.otraLista)
        self.Nuevos.setText(_translate("widget", str(trabajos)))
        
        cuenta = 0
        self.tablaListos.setRowCount(len(self.listaAux))
        for i in self.listaAux:
            self.tablaListos.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
            self.tablaListos.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
            self.tablaListos.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
            cuenta += 1
         
        try:
            self.terminador = self.lisd[1]
            self.ID.setText(_translate("widget", str(self.lisd[0])))
            self.oper.setText(_translate("widget", str(self.lisd[3])))
            self.tme.setText(_translate("widget", str(self.lisd[1])))
            self.tt.setText(_translate("widget", str(self.cont)))
            self.tr.setText(_translate("widget", str(self.lisd[1] - self.cont)))
            self.quantLab.setText(_translate("widget", str(self.quantum2)))
            
            self.contadorGlobal += 1
            if self.cont == self.lisd[1]:
                self.lisd[2] = self.cont
                self.contPros += 1

        except IndexError:
            self.ID.setText(_translate("widget", "Null"))
            self.oper.setText(_translate("widget", "Null"))
            self.tme.setText(_translate("widget", "Null"))
            self.tt.setText(_translate("widget", "Null"))
            self.tr.setText(_translate("widget", "Null"))
            self.quantLab.setText(_translate("widget", "Null"))
            self.contadorGlobal += 1
            
        if self.contPros == self.contTerminados:
            self.quantum2 = 1
            lista = []
            lista.append(self.lisd[0])  
            lista.append(self.lisd[3])  
            lista.append(self.lisd[4])  
            lista.append('Terminado')  
            lista.append(self.lisd[1])  
            lista.append(self.lisd[5])  
            lista.append(self.contadorGlobal)  
            lista.append(lista[6] - lista[5]) 
            lista.append(self.lisd[6] - lista[5])  
            lista.append(self.cont) 
            lista.append(lista[7]-lista[9]) 
            lista.append(lista[4]-lista[9]) 
            
            self.suma2 = self.suma2 - self.lisd[14]
            
            for x in range(len(self.memor)):
                if self.memor[x] == self.lisd[0]:
                    self.memor[x] = 0
                    self.memor1[x] = 0
            
            self.terminados.append(lista)
            try:
                self.lisd = self.listaAux.pop(0)
                if self.lisd[7] == 0:
                    self.lisd[7] = 1
                    self.lisd[6] = self.contadorGlobal
            except IndexError:
                self.lisd = []
            try:
                while True:
                    nuevalis = self.otraLista.pop(0)
                    if nuevalis[14] <= 40 - self.suma2:
                        memoria3 = nuevalis[14]
                        memoria4 = nuevalis[13]
                        memoria5 = int(memoria4/5)
                        memoria4 = memoria4%5
                        for x in range(len(self.memor)):
                            if memoria3 == 0:
                                break
                            if self.memor[x] == 0:
                                self.memor[x] = nuevalis[0]
                                if memoria5 > 0:
                                    self.memor1[x] = 5
                                    memoria5 -= 1
                                else:
                                    self.memor1[x] = memoria4
                                memoria3 -= 1

                        
                        self.suma2 = self.suma2 + nuevalis[14]
                        nuevalis[5] = self.contadorGlobal
                        self.listaAux.append(nuevalis)
                    else:
                        self.otraLista = [nuevalis] + self.otraLista
                        break
            except IndexError:
                pass
            
            self.contTerminados += 1
        elif self.quantum == self.quantum2:
            try:
                listaAgrega = []
                self.lisd[2] = self.cont
                self.quantum2 = 1
                listaAgrega.append(self.lisd[0])
                listaAgrega.append(self.lisd[1])
                listaAgrega.append(self.lisd[2])
                listaAgrega.append(self.lisd[3])
                listaAgrega.append(self.lisd[4])
                listaAgrega.append(self.lisd[5])
                listaAgrega.append(self.lisd[6])
                listaAgrega.append(self.lisd[7])
                listaAgrega.append(self.lisd[8])
                listaAgrega.append(self.lisd[9])
                listaAgrega.append(self.lisd[10])
                listaAgrega.append(self.lisd[11])
                listaAgrega.append(self.lisd[12])
                listaAgrega.append(self.lisd[13])
                listaAgrega.append(self.lisd[14])
                self.listaAux.append(listaAgrega)  
                self.lisd = []
                self.terminadoProceso()
            except IndexError:
                pass
        else:
            self.quantum2 += 1
        
        
        if self.bandera == 4:
            self.bandera = 0
            lista = []    
            lista.append(self.ids)
            
            tme = random.randint(6, 16)
            lista.append(tme)
            
            lista.append(0)
            
            oper = random.randint(1, 6)
            if oper == 1:
                num1 = random.randint(0, 1000)
                num2 = random.randint(0, 1000)
                operacion = str(num1) + "+" + str(num2)
                resultado = num1 + num2
            elif oper == 2:
                 num1 = random.randint(0, 1000)
                 num2 = random.randint(0, 1000)
                 operacion = str(num1) + "-" + str(num2)
                 resultado = num1 - num2
            elif oper == 3:
                num1 = random.randint(-1000, 1000)
                num2 = random.randint(-1000, 1000)
                operacion = str(num1) + "*" + str(num2)
                resultado = num1 * num2
            elif oper == 4:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "/" + str(num2)
                        resultado = round(num1 / num2, 2)
                        break
            elif oper == 5:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "%" + str(num2)
                        resultado = num1 % num2
                        break
            elif oper == 6:
                while True:
                    num1 = random.randint(-1000, 1000)
                    num2 = random.randint(-1000, 1000)
                    if num2 != 0:    
                        operacion = str(num1) + "/" + str(num2)
                        resultado = (num1 * num2)/100
                        break
                    
            lista.append(operacion)
            lista.append(resultado)
            
            lista.append(0)
            lista.append(0)
            lista.append(0)
            lista.append("Nuevo")
            lista.append(" ")
            lista.append(" ")
            lista.append(" ")
            lista.append(tme)
            
            tamano = random.randint(6, 26)
            lista.append(tamano)
            
            tamano2 = int(tamano/5)
            tamano3 = tamano2
            tamano4 = tamano%5
            self.suma = self.suma2
            self.suma = self.suma + tamano2
            if tamano%5 != 0:
                self.suma = self.suma + 1
                tamano2 += 1
            lista.append(tamano2)
            
            if self.suma <= 40 and self.otraLista == []:
                self.suma2 = self.suma
                lista[5] = self.contadorGlobal
                self.listaAux.append(lista)
                self.listaLotes.append(lista)
                for x in range(len(self.memor)):
                    if tamano2 == 0:
                        break
                    if self.memor[x] == 0:
                        self.memor[x] = lista[0]
                        if tamano3 > 0:
                            self.memor1[x] = 5
                            tamano3 -= 1
                        else:
                            self.memor1[x] = tamano4
                        tamano2 -= 1
            else:
                self.otraLista.append(lista)
                self.listaLotes.append(lista)
            
            self.ids += 1
            

        elif self.bandera == 5:
            self.bandera = 0
            self.bcp=QtWidgets.QDialog()
            self.ui=Ui_Form()
            self.ui.setupUi(self.bcp)
            self.bcp.show()
            cuenta = 0
            listaBcp = self.terminados[0:]
            for i in self.otraLista:
                listo = []
                listo.append(i[0])
                listo.append(i[3])
                listo.append("Null")
                listo.append("Nuevo")
                listo.append(i[1])
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append("Null")
                listo.append(i[12])
                listaBcp.append(listo)
            for i in self.listaAux:
                listo = []
                listo.append(i[0])
                listo.append(i[3])
                listo.append("Null")
                listo.append("Listo")
                listo.append(i[1])
                listo.append(i[5])
                listo.append("Null")
                listo.append("Null")
                if i[7] == 0:
                    listo.append("Null")
                elif i[7] == 1:
                    listo.append(i[6] - listo[5])
                listo.append(i[2])
                listo.append((self.contadorGlobal - i[5]) - i[2])
                listo.append(listo[4] - listo[9])
                listaBcp.append(listo)
            for i in self.prosBloq:
                listo = []
                listo.append(i[0])
                listo.append(i[3])
                listo.append("Null")
                listo.append("Bloqueado, rest: " + str((8 - i[-1]) - 1))
                listo.append(i[1])
                listo.append(i[5])
                listo.append("Null")
                listo.append("Null")
                listo.append(i[6] - listo[5])
                listo.append(i[2])
                listo.append((self.contadorGlobal - i[5]) - i[2])
                listo.append(listo[4] - listo[9])
                listaBcp.append(listo)
            #Suspendidos en bcp
            for i in self.suspen:
                listo = []
                listo.append(i[0])
                listo.append(i[3])
                listo.append("Null")
                listo.append("Suspendido")
                listo.append(i[1])
                listo.append(i[5])
                listo.append("Null")
                listo.append("Null")
                listo.append(i[6] - listo[5])
                listo.append(i[2])
                listo.append((self.contadorGlobal - i[5]) - i[2])
                listo.append(listo[4] - listo[9])
                listaBcp.append(listo)
            try:
                listo = []
                listo.append(self.lisd[0])
                listo.append(self.lisd[3])
                listo.append("Null")
                listo.append("Ejecución")
                listo.append(self.lisd[1])
                listo.append(self.lisd[5])
                listo.append("Null")
                listo.append("Null")
                listo.append(self.lisd[6] - listo[5])
                listo.append(self.cont)
                listo.append((self.contadorGlobal - self.lisd[5]) - self.cont)
                listo.append(listo[4] - listo[9])
                listaBcp.append(listo)
            except IndexError:
                pass
                
                
            self.ui.BCP.setRowCount(len(listaBcp))
            for i in listaBcp:
                self.ui.BCP.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.ui.BCP.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1])))
                self.ui.BCP.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                self.ui.BCP.setItem(cuenta, 3, QtWidgets.QTableWidgetItem(str(i[3])))
                self.ui.BCP.setItem(cuenta, 4, QtWidgets.QTableWidgetItem(str(i[4])))
                self.ui.BCP.setItem(cuenta, 5, QtWidgets.QTableWidgetItem(str(i[5])))
                self.ui.BCP.setItem(cuenta, 6, QtWidgets.QTableWidgetItem(str(i[6])))
                self.ui.BCP.setItem(cuenta, 7, QtWidgets.QTableWidgetItem(str(i[7])))
                self.ui.BCP.setItem(cuenta, 8, QtWidgets.QTableWidgetItem(str(i[8])))
                self.ui.BCP.setItem(cuenta, 9, QtWidgets.QTableWidgetItem(str(i[9])))
                self.ui.BCP.setItem(cuenta, 10, QtWidgets.QTableWidgetItem(str(i[10])))
                self.ui.BCP.setItem(cuenta, 11, QtWidgets.QTableWidgetItem(str(i[11])))
                cuenta += 1
                
            self.start_stop_func()
        self.paginacion()
        
        if self.bandera == 2: 
            self.bandera = 0
            self.quantum2 = 1
            lista = []
            lista.append(self.lisd[0])
            lista.append(self.lisd[3])  
            lista.append('ERROR') 
            lista.append('Terminado E')  
            lista.append(self.lisd[1])  
            lista.append(self.lisd[5])  
            lista.append(self.contadorGlobal)  
            lista.append(lista[6] - lista[5]) 
            lista.append(self.lisd[6] - lista[5])  
            lista.append(self.cont)  
            lista.append(lista[7]-lista[9]) 
            lista.append(lista[4]-lista[9])
            
            self.terminados.append(lista)
            self.contPros += 1
            self.contTerminados += 1
            
            cuenta = 0
            self.Terminados.setRowCount(len(self.terminados))
            for i in self.terminados:
                self.Terminados.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.Terminados.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1] + " =")))
                self.Terminados.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                cuenta += 1
            

            self.reloj.setText(_translate("widget", str(self.contadorGlobal)))
            
            self.suma2 = self.suma2 - self.lisd[14]
            for x in range(len(self.memor)):
                if self.memor[x] == self.lisd[0]:
                    self.memor[x] = 0
                    self.memor1[x] = 0
            try:
                while True:
                    nuevalis = self.otraLista.pop(0)
                    if nuevalis[14] <= 40 - self.suma2:
                        memoria3 = nuevalis[14]
                        memoria4 = nuevalis[13]
                        memoria5 = int(memoria4/5)
                        memoria4 = memoria4%5
                        for x in range(len(self.memor)):
                            if memoria3 == 0:
                                break
                            if self.memor[x] == 0:
                                self.memor[x] = nuevalis[0]
                                if memoria5 > 0:
                                    self.memor1[x] = 5
                                    memoria5 -= 1
                                else:
                                    self.memor1[x] = memoria4
                                memoria3 -= 1

                        self.suma2 = self.suma2 + nuevalis[14]
                        nuevalis[5] = self.contadorGlobal
                        self.listaAux.append(nuevalis)
                    else:
                        self.otraLista = [nuevalis] + self.otraLista
                        break
            except IndexError:
                pass
            
            self.lisd = []
            self.terminadoProceso()
        else:
            cuenta = 0
            self.Terminados.setRowCount(len(self.terminados))
            for i in self.terminados:
                self.Terminados.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.Terminados.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[1] + "=")))
                self.Terminados.setItem(cuenta, 2, QtWidgets.QTableWidgetItem(str(i[2])))
                cuenta += 1
            
            if self.contadorGlobal >= 0:
                self.reloj.setText(_translate("widget", str(self.contadorGlobal)))
                    
            for p in self.prosBloq:
                p[15] += 1
                
            cuenta = 0
            self.bloqueados.setRowCount(len(self.prosBloq))
            for i in self.prosBloq:
                self.bloqueados.setItem(cuenta, 0, QtWidgets.QTableWidgetItem(str(i[0])))
                self.bloqueados.setItem(cuenta, 1, QtWidgets.QTableWidgetItem(str(i[15])))
                cuenta += 1
            
            if self.bandera == 1: 
                self.bandera = 0
                try:
                    self.lisd[2] = self.cont
                    listaAgrega = []
                    listaAgrega.append(self.lisd[0])
                    listaAgrega.append(self.lisd[1])
                    listaAgrega.append(self.lisd[2])
                    listaAgrega.append(self.lisd[3])
                    listaAgrega.append(self.lisd[4])
                    listaAgrega.append(self.lisd[5])
                    listaAgrega.append(self.lisd[6])
                    listaAgrega.append(self.lisd[7])
                    listaAgrega.append(self.lisd[8])
                    listaAgrega.append(self.lisd[9])
                    listaAgrega.append(self.lisd[10])
                    listaAgrega.append(self.lisd[11])
                    listaAgrega.append(self.lisd[12])
                    listaAgrega.append(self.lisd[13])
                    listaAgrega.append(self.lisd[14])
                    listaAgrega.append(0)
                    self.prosBloq.append(listaAgrega)                    
                    try:
                        self.lisd = self.listaAux.pop(0)
                        self.quantum2 = 1
                        if self.lisd[7] == 0:
                            self.lisd[7] = 1
                            self.lisd[6] = self.contadorGlobal
                            
                    except IndexError:
                        self.lisd = []
                    self.terminadoProceso()
                except IndexError:
                    pass
            else:
                self.cont += 1
                
                if self.cont > self.terminador:
                      self.terminadoProceso()  
        
class MainWindow(QtWidgets.QWidget, Ui_widget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_I:
            self.bandera = 1
            print("Usted a presionado I")
        elif event.key() == Qt.Key_E:
            self.bandera = 2
            print("Usted a presionado E")
        elif event.key() == Qt.Key_P:
            self.bandera = 3
            print("Usted a presionado P")
        elif event.key() == Qt.Key_T:
            self.bandera = 3
            print("Usted a presionado T")
        elif event.key() == Qt.Key_N:
            self.bandera = 4
            print("Usted a presionado N")
        elif event.key() == Qt.Key_B:
            self.bandera = 5
            print("Usted a presionado B")
        elif event.key() == Qt.Key_C:
            self.start_stop_func()
            print("Usted a presionado C")
        elif event.key() == Qt.Key_S:
            self.bandera = 6
            print("Usted a presionado S")
        elif event.key() == Qt.Key_R:
            self.bandera = 7
            print("Usted a presionado R")
        else:
            print("Usted a presionado una tecla invalida")
            self.bandera = 0

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())