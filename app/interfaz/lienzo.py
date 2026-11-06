"""Lienzo de Matplotlib incrustado en Qt."""
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure


class Lienzo(FigureCanvasQTAgg):
    def __init__(self):
        super().__init__(Figure(figsize=(6, 5), tight_layout=True))
        self.ax = self.figure.add_subplot(projection="3d")
        self._vista = (30, -60)

    def limpiar(self):
        """Borra el gráfico conservando el ángulo de vista; devuelve los ejes."""
        self._vista = (self.ax.elev, self.ax.azim)
        self.ax.clear()
        return self.ax

    def refrescar(self):
        self.ax.view_init(*self._vista)
        self.draw_idle()

    def restablecer_vista(self):
        self.ax.view_init(30, -60)
        self.draw_idle()