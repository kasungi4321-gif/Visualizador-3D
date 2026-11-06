"""Diálogo de créditos con información de contacto de cada integrante."""
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QDialog, QFrame, QLabel, QPushButton, QVBoxLayout

from app.recursos import ruta_recurso


INTEGRANTES = [
    {"nombre": "Mario Emir Aparicio Arteaga", "correo": "MarioEm057@gmail.com"},
    {"nombre": "Jorge Alberto Ortiz Garcia", "correo": "jortizg@proton.me", "github": "kasungi4321-gif"},
]

TITULO = "Visualizador 3D"
VERSION = "1.0"


def _bloque(p):
    """HTML con los datos de una persona (el GitHub es opcional)."""
    html = (
        f"<p><b>{p['nombre']}</b><br>"
        f"<a href='mailto:{p['correo']}'>{p['correo']}</a>"
    )
    if p.get("github"):
        html += f"<br><a href='https://github.com/{p['github']}'>github.com/{p['github']}</a>"
    return html + "</p>"


def _separador():
    linea = QFrame()
    linea.setFrameShape(QFrame.HLine)
    linea.setFrameShadow(QFrame.Sunken)
    return linea


class DialogoCreditos(QDialog):
    
    def __init__(self, padre=None):
        super().__init__(padre)
        self.setWindowTitle("Créditos")
        self.setFixedWidth(360)

        lay = QVBoxLayout(self)
        lay.setSpacing(8)

        icono = QIcon(ruta_recurso("assets/icono.ico")).pixmap(96, 96)
        if not icono.isNull():
            logo = QLabel()
            logo.setPixmap(icono)
            logo.setAlignment(Qt.AlignCenter)
            lay.addWidget(logo)

        titulo = QLabel(f"<h2>{TITULO}</h2><p>Versión {VERSION}</p>")
        titulo.setAlignment(Qt.AlignCenter)
        lay.addWidget(titulo)

        lay.addWidget(QLabel("<b>Desarrollado por:</b>"), alignment=Qt.AlignCenter)
        for i, persona in enumerate(INTEGRANTES):
            if i:
                lay.addWidget(_separador())
            datos = QLabel(_bloque(persona))
            datos.setAlignment(Qt.AlignCenter)
            datos.setTextFormat(Qt.RichText)
            datos.setOpenExternalLinks(True)
            datos.setTextInteractionFlags(Qt.TextBrowserInteraction)
            lay.addWidget(datos)

        cerrar = QPushButton("Cerrar")
        cerrar.clicked.connect(self.accept)
        lay.addWidget(cerrar)