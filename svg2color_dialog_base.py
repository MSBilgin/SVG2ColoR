# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'svg2color_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SVG2ColoRDialogBase(object):
    def setupUi(self, SVG2ColoRDialogBase):
        SVG2ColoRDialogBase.setObjectName("SVG2ColoRDialogBase")
        SVG2ColoRDialogBase.resize(560, 330)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(SVG2ColoRDialogBase.sizePolicy().hasHeightForWidth())
        SVG2ColoRDialogBase.setSizePolicy(sizePolicy)
        self.graphicsView = QtWidgets.QGraphicsView(SVG2ColoRDialogBase)
        self.graphicsView.setGeometry(QtCore.QRect(30, 130, 499, 99))
        self.graphicsView.setStyleSheet("")
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton_3 = QtWidgets.QPushButton(SVG2ColoRDialogBase)
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QtCore.QRect(430, 270, 101, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(SVG2ColoRDialogBase)
        self.label.setEnabled(False)
        self.label.setGeometry(QtCore.QRect(390, 275, 51, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(SVG2ColoRDialogBase)
        self.label_2.setGeometry(QtCore.QRect(30, 275, 91, 16))
        self.label_2.setStyleSheet("color:blue")
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(SVG2ColoRDialogBase)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(260, 270, 101, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.radioButton_2 = QtWidgets.QRadioButton(SVG2ColoRDialogBase)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 30, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.pushButton = QtWidgets.QPushButton(SVG2ColoRDialogBase)
        self.pushButton.setGeometry(QtCore.QRect(455, 70, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(SVG2ColoRDialogBase)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 401, 20))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.radioButton = QtWidgets.QRadioButton(SVG2ColoRDialogBase)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 101, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(SVG2ColoRDialogBase)
        QtCore.QMetaObject.connectSlotsByName(SVG2ColoRDialogBase)

    def retranslateUi(self, SVG2ColoRDialogBase):
        _translate = QtCore.QCoreApplication.translate
        SVG2ColoRDialogBase.setWindowTitle(_translate("SVG2ColoRDialogBase", "SVG2ColoR"))
        self.pushButton_3.setText(_translate("SVG2ColoRDialogBase", "Import"))
        self.label.setText(_translate("SVG2ColoRDialogBase", "OR"))
        self.label_2.setText(_translate("SVG2ColoRDialogBase", "<a href=\"http://cbsuygulama.wordpress.com/2014/06/26/svg2color-qgis-color-ramp-plugin/\">Help...</a>"))
        self.pushButton_2.setText(_translate("SVG2ColoRDialogBase", "Save as..."))
        self.radioButton_2.setText(_translate("SVG2ColoRDialogBase", "URL"))
        self.pushButton.setText(_translate("SVG2ColoRDialogBase", "Browse..."))
        self.radioButton.setText(_translate("SVG2ColoRDialogBase", "Local File"))

