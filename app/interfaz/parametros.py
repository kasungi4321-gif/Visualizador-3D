"""Panel de campos numéricos generado a partir de las especificaciones del catálogo."""
from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDoubleSpinBox, QFormLayout, QWidget


class PanelParametros(QWidget):
    """Campos numéricos generados desde (etiqueta, mínimo, máximo, valor[, paso])."""
    cambio = Signal()

    def __init__(self, specs):
        super().__init__()
        form = QFormLayout(self)
        form.setContentsMargins(0, 0, 0, 0)
        self.spins = []
        for etiqueta, minimo, maximo, valor, *paso in specs:
            paso = paso[0] if paso else 0.1
            spin = QDoubleSpinBox()
            spin.setDecimals(0 if paso >= 1 else 2)
            spin.setRange(minimo, maximo)
            spin.setSingleStep(paso)
            spin.setValue(valor)
            spin.valueChanged.connect(lambda *_: self.cambio.emit())
            form.addRow(etiqueta, spin)
            self.spins.append(spin)

    def valores(self):
        return [int(s.value()) if s.decimals() == 0 else s.value() for s in self.spins]