# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bcp.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# Creadores: Jaime Adalberto Lomeli Navarro, Luis Fernando Monjaraz Briseño
# Maestra: Violeta del Rocío Beceera Velázquez
# Materia: Sistemas Operativos

from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1535, 596)
        Form.setStyleSheet("background-color: rgb(255, 239, 213);")
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("font: 20pt \"Algerian\";")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.BCP = QtWidgets.QTableWidget(Form)
        self.BCP.setStyleSheet("font: 10pt \"Times New Roman\";")
        self.BCP.setObjectName("BCP")
        self.BCP.setColumnCount(12)
        self.BCP.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.BCP.setHorizontalHeaderItem(11, item)
        self.verticalLayout.addWidget(self.BCP)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Tabla de procesos"))
        item = self.BCP.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID"))
        item = self.BCP.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Operación"))
        item = self.BCP.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Resultado"))
        item = self.BCP.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Estado"))
        item = self.BCP.horizontalHeaderItem(4)
        item.setText(_translate("Form", "TME"))
        item = self.BCP.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Llegada"))
        item = self.BCP.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Finalización"))
        item = self.BCP.horizontalHeaderItem(7)
        item.setText(_translate("Form", "Retorno"))
        item = self.BCP.horizontalHeaderItem(8)
        item.setText(_translate("Form", "Respuesta"))
        item = self.BCP.horizontalHeaderItem(9)
        item.setText(_translate("Form", "Servicio"))
        item = self.BCP.horizontalHeaderItem(10)
        item.setText(_translate("Form", "Espera"))
        item = self.BCP.horizontalHeaderItem(11)
        item.setText(_translate("Form", "Restante"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())