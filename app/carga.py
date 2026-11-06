"""Pantalla de carga con imagen, mensaje y barra de progreso."""
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor, QPixmap
from PySide6.QtWidgets import QApplication, QSplashScreen


class PantallaCarga(QSplashScreen):
    def __init__(self, ruta_imagen, ancho=480, color_texto="white"):
        pix = QPixmap(ruta_imagen).scaledToWidth(ancho, Qt.SmoothTransformation)
        super().__init__(pix, Qt.WindowStaysOnTopHint)
        self._progreso = 0
        self._color = QColor(color_texto)

    def avance(self, porcentaje, texto):
        """Actualiza barra y mensaje (el bucle de eventos aún no corre, por eso processEvents)."""
        self._progreso = porcentaje
        self.showMessage(texto, Qt.AlignBottom | Qt.AlignHCenter, self._color)
        self.repaint()
        QApplication.processEvents()

    def drawContents(self, painter):
        super().drawContents(painter)  # dibuja el mensaje
        w, h = self.width(), self.height()
        painter.setPen(Qt.NoPen)
        painter.setBrush(QColor(255, 255, 255, 70))
        painter.drawRect(0, h - 6, w, 6)
        painter.setBrush(QColor("#2d8cff"))
        painter.drawRect(0, h - 6, int(w * self._progreso / 100), 6)