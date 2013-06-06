# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_movies.ui'
#
# Created: Thu May 30 02:46:11 2013
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MoviesWindow(object):
    def setupUi(self, MoviesWindow):
        MoviesWindow.setObjectName("MoviesWindow")
        MoviesWindow.resize(700, 400)
        self.combo_countries = QtGui.QComboBox(MoviesWindow)
        self.combo_countries.setGeometry(QtCore.QRect(50, 30, 101, 25))
        self.combo_countries.setObjectName("combo_countries")
        self.label = QtGui.QLabel(MoviesWindow)
        self.label.setGeometry(QtCore.QRect(20, 35, 31, 16))
        self.label.setObjectName("label")
        self.search_box = QtGui.QLineEdit(MoviesWindow)
        self.search_box.setGeometry(QtCore.QRect(176, 30, 421, 25))
        self.search_box.setObjectName("search_box")
        self.btn_search = QtGui.QPushButton(MoviesWindow)
        self.btn_search.setGeometry(QtCore.QRect(596, 30, 87, 27))
        self.btn_search.setObjectName("btn_search")
        self.table_movies = QtGui.QTableView(MoviesWindow)
        self.table_movies.setGeometry(QtCore.QRect(20, 63, 661, 331))
        self.table_movies.setObjectName("table_movies")

        self.retranslateUi(MoviesWindow)
        QtCore.QMetaObject.connectSlotsByName(MoviesWindow)

    def retranslateUi(self, MoviesWindow):
        MoviesWindow.setWindowTitle(QtGui.QApplication.translate("MoviesWindow", "Películas", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MoviesWindow", "País:", None, QtGui.QApplication.UnicodeUTF8))
        self.search_box.setPlaceholderText(QtGui.QApplication.translate("MoviesWindow", "Busque películas aquí", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_search.setText(QtGui.QApplication.translate("MoviesWindow", "Buscar", None, QtGui.QApplication.UnicodeUTF8))

