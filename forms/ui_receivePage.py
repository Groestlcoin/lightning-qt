# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/receivepage.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ReceivePage(object):
    def setupUi(self, ReceivePage):
        ReceivePage.setObjectName("ReceivePage")
        ReceivePage.resize(750, 350)
        self.verticalLayout = QtWidgets.QVBoxLayout(ReceivePage)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(ReceivePage)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.spinValue = QtWidgets.QSpinBox(ReceivePage)
        self.spinValue.setSuffix("")
        self.spinValue.setMinimum(1)
        self.spinValue.setMaximum(1680000000)
        self.spinValue.setObjectName("spinValue")
        self.horizontalLayout_2.addWidget(self.spinValue)
        self.labelUnit = QtWidgets.QLabel(ReceivePage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.labelUnit.setFont(font)
        self.labelUnit.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.labelUnit.setText("MGRO")
        self.labelUnit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.labelUnit.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.labelUnit.setObjectName("labelUnit")
        self.horizontalLayout_2.addWidget(self.labelUnit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtWidgets.QLabel(ReceivePage)
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(ReceivePage)
        self.label_3.setMidLineWidth(0)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineDescription = QtWidgets.QLineEdit(ReceivePage)
        self.lineDescription.setObjectName("lineDescription")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineDescription)
        self.label_4 = QtWidgets.QLabel(ReceivePage)
        self.label_4.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.spinExpiry = QtWidgets.QSpinBox(ReceivePage)
        self.spinExpiry.setMinimum(1)
        self.spinExpiry.setMaximum(999999)
        self.spinExpiry.setProperty("value", 604800)
        self.spinExpiry.setObjectName("spinExpiry")
        self.horizontalLayout_3.addWidget(self.spinExpiry)
        self.label_6 = QtWidgets.QLabel(ReceivePage)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.label_5 = QtWidgets.QLabel(ReceivePage)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_3.addWidget(self.label_5)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.buttonGenerate = QtWidgets.QPushButton(ReceivePage)
        self.buttonGenerate.setObjectName("buttonGenerate")
        self.horizontalLayout_4.addWidget(self.buttonGenerate)
        self.buttonClear = QtWidgets.QPushButton(ReceivePage)
        self.buttonClear.setObjectName("buttonClear")
        self.horizontalLayout_4.addWidget(self.buttonClear)
        spacerItem3 = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.formLayout.setLayout(9, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineLabel = QtWidgets.QLineEdit(ReceivePage)
        self.lineLabel.setObjectName("lineLabel")
        self.horizontalLayout.addWidget(self.lineLabel)
        spacerItem4 = QtWidgets.QSpacerItem(260, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        spacerItem5 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.FieldRole, spacerItem5)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_7 = QtWidgets.QLabel(ReceivePage)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.textResultInvoice = QtWidgets.QTextEdit(ReceivePage)
        self.textResultInvoice.setMaximumSize(QtCore.QSize(16777215, 60))
        self.textResultInvoice.setAcceptRichText(False)
        self.textResultInvoice.setTextInteractionFlags(QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textResultInvoice.setObjectName("textResultInvoice")
        self.verticalLayout_3.addWidget(self.textResultInvoice)
        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.retranslateUi(ReceivePage)
        QtCore.QMetaObject.connectSlotsByName(ReceivePage)
        ReceivePage.setTabOrder(self.lineLabel, self.lineDescription)
        ReceivePage.setTabOrder(self.lineDescription, self.buttonGenerate)
        ReceivePage.setTabOrder(self.buttonGenerate, self.buttonClear)
        ReceivePage.setTabOrder(self.buttonClear, self.textResultInvoice)

    def retranslateUi(self, ReceivePage):
        _translate = QtCore.QCoreApplication.translate
        ReceivePage.setWindowTitle(_translate("ReceivePage", "Form"))
        self.label.setToolTip(_translate("ReceivePage", "Value in millisatoshis of invoice to request."))
        self.label.setText(_translate("ReceivePage", "Value :"))
        self.spinValue.setToolTip(_translate("ReceivePage", "Value in millisatoshis of invoice to request."))
        self.labelUnit.setToolTip(_translate("ReceivePage", "Your current on channels balance"))
        self.label_2.setToolTip(_translate("ReceivePage", "A unique string or number (never revealed to other nodes on the lightning network), used to query the status of this invoice."))
        self.label_2.setText(_translate("ReceivePage", "Label :"))
        self.label_3.setToolTip(_translate("ReceivePage", "A short description of the payment purpose, e.g. \"1 flat glob and 2 dogecoins\"."))
        self.label_3.setText(_translate("ReceivePage", "Description :"))
        self.lineDescription.setToolTip(_translate("ReceivePage", "A short description of the payment purpose, e.g. \"1 flat glob and 2 dogecoins\"."))
        self.label_4.setToolTip(_translate("ReceivePage", "The time the invoice is valid for"))
        self.label_4.setText(_translate("ReceivePage", "Expiry :"))
        self.spinExpiry.setToolTip(_translate("ReceivePage", "The time the invoice is valid for."))
        self.label_6.setText(_translate("ReceivePage", "seconds"))
        self.label_5.setText(_translate("ReceivePage", "(Optional, defaults to 1 week)"))
        self.buttonGenerate.setText(_translate("ReceivePage", "Generate invoice"))
        self.buttonClear.setText(_translate("ReceivePage", "Clear"))
        self.lineLabel.setToolTip(_translate("ReceivePage", "A unique string or number (never revealed to other nodes on the lightning network), used to query the status of this invoice."))
        self.label_7.setText(_translate("ReceivePage", "Invoice :"))
