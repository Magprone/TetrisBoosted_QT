# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_mode_page.ui'
#
# Created by: PyQt5 UI code generator 5.15.5
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_form(object):
    def setupUi(self, form):
        form.setObjectName("form")
        form.resize(600, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.back_button = QtWidgets.QPushButton(form)
        self.back_button.setObjectName("back_button")
        self.verticalLayout.addWidget(self.back_button, 0, QtCore.Qt.AlignLeft)
        spacerItem = QtWidgets.QSpacerItem(20, 227, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.default_mode_button = QtWidgets.QPushButton(form)
        self.default_mode_button.setObjectName("default_mode_button")
        self.verticalLayout.addWidget(self.default_mode_button, 0, QtCore.Qt.AlignHCenter)
        self.extra_mode_button = QtWidgets.QPushButton(form)
        self.extra_mode_button.setObjectName("extra_mode_button")
        self.verticalLayout.addWidget(self.extra_mode_button, 0, QtCore.Qt.AlignHCenter)
        spacerItem1 = QtWidgets.QSpacerItem(20, 227, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(form)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.back_button.setText(_translate("form", "Back"))
        self.default_mode_button.setText(_translate("form", "Default mode"))
        self.extra_mode_button.setText(_translate("form", "Extra mode"))
