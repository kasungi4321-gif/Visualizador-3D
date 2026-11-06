"""Arranque de la aplicación: pantalla de carga, imports pesados y ventana principal."""
import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from app.carga import PantallaCarga
from app.recursos import ruta_recurso


try:
    import pyi_splash
except ImportError:
    pyi_splash = None


def ejecutar():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon(ruta_recurso("assets/icono.ico")))

    splash = PantallaCarga(ruta_recurso("assets/carga.png"))
    splash.show()
    if pyi_splash:
        pyi_splash.close()

    # Imports pesados DESPUÉS de mostrar el splash
    splash.avance(15, "Cargando matplotlib…")
    from app.catalogo import CATALOGOS
    splash.avance(55, "Construyendo interfaz…")
    from app.interfaz.ventana import Ventana
    from app.controlador import redibujar

    ventana = Ventana(CATALOGOS)
    ventana.cambio.connect(lambda: redibujar(ventana))

    splash.avance(85, "Dibujando primera figura…")
    redibujar(ventana)  # el primer render de matplotlib es lento; mejor con el splash visible

    splash.avance(100, "Listo")
    ventana.show()
    splash.finish(ventana)
    return app.exec()