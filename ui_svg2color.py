# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_svg2color.ui'
#
# Created: Wed Jul 09 00:20:52 2014
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_SVG2ColoR(object):
    def setupUi(self, SVG2ColoR):
        SVG2ColoR.setObjectName(_fromUtf8("SVG2ColoR"))
        SVG2ColoR.resize(558, 359)
        self.lineEdit = QtGui.QLineEdit(SVG2ColoR)
        self.lineEdit.setGeometry(QtCore.QRect(30, 70, 401, 20))
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(SVG2ColoR)
        self.pushButton.setGeometry(QtCore.QRect(460, 70, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(SVG2ColoR)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QtCore.QRect(434, 280, 101, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_2 = QtGui.QLabel(SVG2ColoR)
        self.label_2.setGeometry(QtCore.QRect(40, 290, 46, 13))
        self.label_2.setStyleSheet(_fromUtf8("color:blue"))
        self.label_2.setOpenExternalLinks(True)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.graphicsView = QtGui.QGraphicsView(SVG2ColoR)
        self.graphicsView.setGeometry(QtCore.QRect(30, 130, 499, 99))
        self.graphicsView.setStyleSheet(_fromUtf8(""))
        self.graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.radioButton = QtGui.QRadioButton(SVG2ColoR)
        self.radioButton.setGeometry(QtCore.QRect(30, 30, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(SVG2ColoR)
        self.radioButton_2.setGeometry(QtCore.QRect(130, 30, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))

        self.retranslateUi(SVG2ColoR)
        QtCore.QMetaObject.connectSlotsByName(SVG2ColoR)

    def retranslateUi(self, SVG2ColoR):
        SVG2ColoR.setWindowTitle(_translate("SVG2ColoR", "SVG2ColoR", None))
        self.pushButton.setText(_translate("SVG2ColoR", "Browse...", None))
        self.pushButton_2.setText(_translate("SVG2ColoR", "Export as Style", None))
        self.label_2.setText(_translate("SVG2ColoR", "<a href=\"http://cbsuygulama.wordpress.com/2014/06/26/svg2color-qgis-color-ramp-plugin/\">Help...</a>", None))
        self.radioButton.setText(_translate("SVG2ColoR", "Local File", None))
        self.radioButton_2.setText(_translate("SVG2ColoR", "URL", None))

