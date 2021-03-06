# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_page.ui'
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
        self.gridLayout = QtWidgets.QGridLayout(form)
        self.gridLayout.setObjectName("gridLayout")
        self.back_button = QtWidgets.QPushButton(form)
        self.back_button.setObjectName("back_button")
        self.gridLayout.addWidget(self.back_button, 0, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.tab_widget = QtWidgets.QTabWidget(form)
        self.tab_widget.setObjectName("tab_widget")
        self.control = QtWidgets.QWidget()
        self.control.setAccessibleName("")
        self.control.setObjectName("control")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.control)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.left_rotate_line_edit = QtWidgets.QLineEdit(self.control)
        self.left_rotate_line_edit.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.left_rotate_line_edit.setPalette(palette)
        self.left_rotate_line_edit.setObjectName("left_rotate_line_edit")
        self.gridLayout_3.addWidget(self.left_rotate_line_edit, 1, 1, 1, 1)
        self.left_rotate_push_button = QtWidgets.QPushButton(self.control)
        self.left_rotate_push_button.setObjectName("left_rotate_push_button")
        self.control_settings_button_group = QtWidgets.QButtonGroup(form)
        self.control_settings_button_group.setObjectName("control_settings_button_group")
        self.control_settings_button_group.addButton(self.left_rotate_push_button)
        self.gridLayout_3.addWidget(self.left_rotate_push_button, 1, 3, 1, 1)
        self.move_left_line_edit = QtWidgets.QLineEdit(self.control)
        self.move_left_line_edit.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.move_left_line_edit.setPalette(palette)
        self.move_left_line_edit.setObjectName("move_left_line_edit")
        self.gridLayout_3.addWidget(self.move_left_line_edit, 2, 1, 1, 1)
        self.control_settings_state_label = QtWidgets.QLabel(self.control)
        self.control_settings_state_label.setText("")
        self.control_settings_state_label.setObjectName("control_settings_state_label")
        self.gridLayout_3.addWidget(self.control_settings_state_label, 9, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.one_block_down_line_edit = QtWidgets.QLineEdit(self.control)
        self.one_block_down_line_edit.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.one_block_down_line_edit.setPalette(palette)
        self.one_block_down_line_edit.setObjectName("one_block_down_line_edit")
        self.gridLayout_3.addWidget(self.one_block_down_line_edit, 4, 1, 1, 1)
        self.move_right_line_edit = QtWidgets.QLineEdit(self.control)
        self.move_right_line_edit.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.move_right_line_edit.setPalette(palette)
        self.move_right_line_edit.setObjectName("move_right_line_edit")
        self.gridLayout_3.addWidget(self.move_right_line_edit, 3, 1, 1, 1)
        self.one_block_down_push_button = QtWidgets.QPushButton(self.control)
        self.one_block_down_push_button.setObjectName("one_block_down_push_button")
        self.control_settings_button_group.addButton(self.one_block_down_push_button)
        self.gridLayout_3.addWidget(self.one_block_down_push_button, 4, 3, 1, 1)
        self.move_right_label = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.move_right_label.setFont(font)
        self.move_right_label.setObjectName("move_right_label")
        self.gridLayout_3.addWidget(self.move_right_label, 3, 0, 1, 1)
        self.move_left_push_button = QtWidgets.QPushButton(self.control)
        self.move_left_push_button.setObjectName("move_left_push_button")
        self.control_settings_button_group.addButton(self.move_left_push_button)
        self.gridLayout_3.addWidget(self.move_left_push_button, 2, 3, 1, 1)
        self.one_block_down_label = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.one_block_down_label.setFont(font)
        self.one_block_down_label.setObjectName("one_block_down_label")
        self.gridLayout_3.addWidget(self.one_block_down_label, 4, 0, 1, 1)
        self.move_left_label = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.move_left_label.setFont(font)
        self.move_left_label.setObjectName("move_left_label")
        self.gridLayout_3.addWidget(self.move_left_label, 2, 0, 1, 1)
        self.move_right_push_button = QtWidgets.QPushButton(self.control)
        self.move_right_push_button.setObjectName("move_right_push_button")
        self.control_settings_button_group.addButton(self.move_right_push_button)
        self.gridLayout_3.addWidget(self.move_right_push_button, 3, 3, 1, 1)
        self.left_rotate_label = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.left_rotate_label.setFont(font)
        self.left_rotate_label.setObjectName("left_rotate_label")
        self.gridLayout_3.addWidget(self.left_rotate_label, 1, 0, 1, 1)
        self.right_rotate_push_button = QtWidgets.QPushButton(self.control)
        self.right_rotate_push_button.setObjectName("right_rotate_push_button")
        self.control_settings_button_group.addButton(self.right_rotate_push_button)
        self.gridLayout_3.addWidget(self.right_rotate_push_button, 0, 3, 1, 1)
        self.right_rotate_line_edit = QtWidgets.QLineEdit(self.control)
        self.right_rotate_line_edit.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.right_rotate_line_edit.setPalette(palette)
        self.right_rotate_line_edit.setObjectName("right_rotate_line_edit")
        self.gridLayout_3.addWidget(self.right_rotate_line_edit, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem, 7, 1, 1, 1)
        self.drop_piece_label = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.drop_piece_label.setFont(font)
        self.drop_piece_label.setObjectName("drop_piece_label")
        self.gridLayout_3.addWidget(self.drop_piece_label, 5, 0, 1, 1)
        self.drop_piece_line_edit = QtWidgets.QLineEdit(self.control)
        self.drop_piece_line_edit.setEnabled(False)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        self.drop_piece_line_edit.setPalette(palette)
        self.drop_piece_line_edit.setObjectName("drop_piece_line_edit")
        self.gridLayout_3.addWidget(self.drop_piece_line_edit, 5, 1, 1, 1)
        self.drop_piece_push_button = QtWidgets.QPushButton(self.control)
        self.drop_piece_push_button.setObjectName("drop_piece_push_button")
        self.control_settings_button_group.addButton(self.drop_piece_push_button)
        self.gridLayout_3.addWidget(self.drop_piece_push_button, 5, 3, 1, 1)
        self.right_rotate_label = QtWidgets.QLabel(self.control)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.right_rotate_label.setFont(font)
        self.right_rotate_label.setObjectName("right_rotate_label")
        self.gridLayout_3.addWidget(self.right_rotate_label, 0, 0, 1, 1)
        self.tab_widget.addTab(self.control, "")
        self.board = QtWidgets.QWidget()
        self.board.setObjectName("board")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.board)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.width_push_button = QtWidgets.QPushButton(self.board)
        self.width_push_button.setObjectName("width_push_button")
        self.board_settings_button_group = QtWidgets.QButtonGroup(form)
        self.board_settings_button_group.setObjectName("board_settings_button_group")
        self.board_settings_button_group.addButton(self.width_push_button)
        self.gridLayout_4.addWidget(self.width_push_button, 0, 2, 1, 1)
        self.width_line_edit = QtWidgets.QLineEdit(self.board)
        self.width_line_edit.setObjectName("width_line_edit")
        self.gridLayout_4.addWidget(self.width_line_edit, 0, 1, 1, 1)
        self.width_label = QtWidgets.QLabel(self.board)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.width_label.setFont(font)
        self.width_label.setObjectName("width_label")
        self.gridLayout_4.addWidget(self.width_label, 0, 0, 1, 1)
        self.height_push_button = QtWidgets.QPushButton(self.board)
        self.height_push_button.setObjectName("height_push_button")
        self.board_settings_button_group.addButton(self.height_push_button)
        self.gridLayout_4.addWidget(self.height_push_button, 1, 2, 1, 1)
        self.height_line_edit = QtWidgets.QLineEdit(self.board)
        self.height_line_edit.setObjectName("height_line_edit")
        self.gridLayout_4.addWidget(self.height_line_edit, 1, 1, 1, 1)
        self.height_label = QtWidgets.QLabel(self.board)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.height_label.setFont(font)
        self.height_label.setObjectName("height_label")
        self.gridLayout_4.addWidget(self.height_label, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem1, 2, 1, 1, 1)
        self.board_settings_state_label = QtWidgets.QLabel(self.board)
        self.board_settings_state_label.setText("")
        self.board_settings_state_label.setObjectName("board_settings_state_label")
        self.gridLayout_4.addWidget(self.board_settings_state_label, 3, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.tab_widget.addTab(self.board, "")
        self.back_to_default = QtWidgets.QWidget()
        self.back_to_default.setObjectName("back_to_default")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.back_to_default)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.back_to_default_button = QtWidgets.QPushButton(self.back_to_default)
        self.back_to_default_button.setObjectName("back_to_default_button")
        self.gridLayout_5.addWidget(self.back_to_default_button, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_5.addItem(spacerItem2, 1, 0, 1, 1)
        self.tab_widget.addTab(self.back_to_default, "")
        self.gridLayout.addWidget(self.tab_widget, 1, 0, 1, 1)

        self.retranslateUi(form)
        self.tab_widget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(form)

    def retranslateUi(self, form):
        _translate = QtCore.QCoreApplication.translate
        form.setWindowTitle(_translate("form", "Form"))
        self.back_button.setText(_translate("form", "Back"))
        self.left_rotate_push_button.setText(_translate("form", "Remap key"))
        self.one_block_down_push_button.setText(_translate("form", "Remap key"))
        self.move_right_label.setText(_translate("form", "Move Right"))
        self.move_left_push_button.setText(_translate("form", "Remap key"))
        self.one_block_down_label.setText(_translate("form", "One block down"))
        self.move_left_label.setText(_translate("form", "Move Left"))
        self.move_right_push_button.setText(_translate("form", "Remap key"))
        self.left_rotate_label.setText(_translate("form", "Left Rotate"))
        self.right_rotate_push_button.setText(_translate("form", "Remap key"))
        self.drop_piece_label.setText(_translate("form", "Drop Piece"))
        self.drop_piece_push_button.setText(_translate("form", "Remap key"))
        self.right_rotate_label.setText(_translate("form", "Right Rotate"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.control), _translate("form", "Control"))
        self.width_push_button.setText(_translate("form", "Set width"))
        self.width_label.setText(_translate("form", "Width"))
        self.height_push_button.setText(_translate("form", "Set heigth"))
        self.height_label.setText(_translate("form", "Heidht"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.board), _translate("form", "Board"))
        self.back_to_default_button.setText(_translate("form", "Back to default settings"))
        self.tab_widget.setTabText(self.tab_widget.indexOf(self.back_to_default), _translate("form", "Back to default"))
