#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys

from PySide import QtGui, QtCore
import controller
from ui_movies import Ui_MoviesWindow


class MoviesApp(QtGui.QWidget):

    def __init__(self):
        super(MoviesApp, self).__init__()
        self.ui =  Ui_MoviesWindow()
        self.ui.setupUi(self)
        self.load_countries()
        self.load_movies()
        self.show()
        self.set_listeners()


    def set_listeners(self):
        self.ui.combo_countries.activated[int].connect(self.load_movies_by_country)
        self.ui.btn_search.clicked.connect(self.load_movies_by_search)


    def load_countries(self):
        countries = controller.get_countries()
        self.ui.combo_countries.addItem("Todos", -1)
        for country in countries:
            self.ui.combo_countries.addItem(country["name"], country["id_country"])

        # self.ui.combo_countries.setEditable(True)
        # completer = QtGui.QCompleter(map(lambda c: c["name"], countries), self)
        # completer.setCaseSensitivity(QtCore.Qt.CaseInsensitive)
        # self.ui.combo_countries.setCompleter(completer)


    def load_movies_by_country(self, index):
        id_country = self.ui.combo_countries.itemData(self.ui.combo_countries.currentIndex())
        if id_country == -1:
            movies = controller.get_movies()
        else:
            movies = controller.get_movies_by_country(id_country)
        self.load_movies(movies)

    def load_movies_by_search(self):
        word = self.ui.search_box.text()
        movies = controller.search_movies(word)
        self.load_movies(movies)

    def load_movies(self, movies=None):
        if movies is None:
            movies = controller.get_movies()

        #Creamos el modelo asociado a la tabla
        self.model = QtGui.QStandardItemModel(len(movies), 4)
        self.model.setHorizontalHeaderItem(0, QtGui.QStandardItem(u"Título"))
        self.model.setHorizontalHeaderItem(1, QtGui.QStandardItem(u"Año"))
        self.model.setHorizontalHeaderItem(2, QtGui.QStandardItem(u"Director"))
        self.model.setHorizontalHeaderItem(3, QtGui.QStandardItem(u"País"))

        r = 0
        for row in movies:
            index = self.model.index(r, 0, QtCore.QModelIndex()); 
            self.model.setData(index, row['title'])
            index = self.model.index(r, 1, QtCore.QModelIndex()); 
            self.model.setData(index, row['year_of_release'])
            index = self.model.index(r, 2, QtCore.QModelIndex()); 
            self.model.setData(index, row['director'])
            index = self.model.index(r, 3, QtCore.QModelIndex()); 
            self.model.setData(index, row['country'])
            r = r+1

        self.ui.table_movies.setModel(self.model)
        self.ui.table_movies.setColumnWidth(0, 270)
        self.ui.table_movies.setColumnWidth(1, 50)
        self.ui.table_movies.setColumnWidth(2, 150)
        self.ui.table_movies.setColumnWidth(3, 150)



def run():
    app = QtGui.QApplication(sys.argv)
    main = MoviesApp()
    sys.exit(app.exec_())

if __name__ == '__main__':
    run()