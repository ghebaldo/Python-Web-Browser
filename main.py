#[Python; Navegador minimalista].
import sys
import os
from os import system
from colorama import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

#[Corpus; Start].
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()

        Orson_navBar = QToolBar()
        self.addToolBar(Orson_navBar)


        back_btn = QAction('Regresar', self)
        back_btn.triggered.connect(self.browser.back)
        Orson_navBar.addAction(back_btn)

        forward_btn = QAction('Siguiente', self)
        forward_btn.triggered.connect(self.browser.forward)
        Orson_navBar.addAction(forward_btn)

        reload_btn = QAction('Recargar', self)
        reload_btn.triggered.connect(self.browser.reload)
        Orson_navBar.addAction(reload_btn)

        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        Orson_navBar.addAction(home_btn)

        google_btn = QAction('[Sitio: Google]', self)
        google_btn.triggered.connect(self.google_site)
        Orson_navBar.addAction(google_btn)

        duckduckgo_btn = QAction('[Sitio: DuckDuckGo]', self)
        duckduckgo_btn.triggered.connect(self.duckduckgo_site)
        Orson_navBar.addAction(duckduckgo_btn)

        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        Orson_navBar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)

    def navigate_home(self):
        self.browser.setUrl(QUrl('https://github.com/ghebaldo'))

    def google_site(self):
    	self.browser.setUrl(QUrl('https://www.google.com/'))
    def duckduckgo_site(self):
    	self.browser.setUrl(QUrl('https://duckduckgo.com/'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('[Python; Navegador privado].')
window = MainWindow()
app.exec_()