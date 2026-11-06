"""Ventana principal (solo diseño)."""
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QComboBox, QGroupBox, QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QStackedWidget, QTabWidget, QVBoxLayout, QWidget,
)

from app.interfaz.creditos import DialogoCreditos
from app.interfaz.lienzo import Lienzo
from app.interfaz.parametros import PanelParametros


class Ventana(QMainWindow):
    cambio = Signal()

    def __init__(self, catalogos):
        super().__init__()
        self.setWindowTitle("Visualizador 3D: Figuras y transformaciones")
        self.resize(1100, 700)

        self.menuBar().addAction("Créditos").triggered.connect(self.mostrar_creditos)

        self.lienzo = Lienzo()
        self.info = QLabel()
        self.info.setStyleSheet("font-family: monospace;")
        self.selectores = []  # (combo, pila) por cada pestaña

        self.tabs = QTabWidget()
        for titulo, catalogo in catalogos.items():
            self.tabs.addTab(self._crear_tab(catalogo), titulo)
        self.tabs.currentChanged.connect(lambda *_: self.cambio.emit())

        caja_info = QGroupBox("Matriz / vector aplicado")
        QVBoxLayout(caja_info).addWidget(self.info)
        boton = QPushButton("Restablecer vista")
        boton.clicked.connect(self.lienzo.restablecer_vista)

        panel = QWidget()
        panel.setFixedWidth(320)
        lay_panel = QVBoxLayout(panel)
        for w in (self.tabs, caja_info, boton):
            lay_panel.addWidget(w)
        lay_panel.addStretch()

        grafico = QVBoxLayout()
        grafico.addWidget(NavigationToolbar2QT(self.lienzo, self))
        grafico.addWidget(self.lienzo, 1)

        central = QWidget()
        lay = QHBoxLayout(central)
        lay.addWidget(panel)
        lay.addLayout(grafico, 1)
        self.setCentralWidget(central)

    def _crear_tab(self, catalogo):
        combo = QComboBox()
        combo.addItems(list(catalogo))
        pila = QStackedWidget()
        for _, specs in catalogo.values():
            panel = PanelParametros(specs)
            panel.cambio.connect(lambda: self.cambio.emit())
            pila.addWidget(panel)
        combo.currentIndexChanged.connect(pila.setCurrentIndex)
        combo.currentIndexChanged.connect(lambda *_: self.cambio.emit())

        grupo = QGroupBox("Parámetros")
        QVBoxLayout(grupo).addWidget(pila)
        tab = QWidget()
        lay = QVBoxLayout(tab)
        lay.addWidget(combo)
        lay.addWidget(grupo)
        lay.addStretch()
        self.selectores.append((combo, pila))
        return tab

    def mostrar_creditos(self):
        DialogoCreditos(self).exec()

    def seleccion(self):
        """Devuelve (pestaña, opción elegida, valores de los parámetros)."""
        i = self.tabs.currentIndex()
        combo, pila = self.selectores[i]
        return self.tabs.tabText(i), combo.currentText(), pila.currentWidget().valores()