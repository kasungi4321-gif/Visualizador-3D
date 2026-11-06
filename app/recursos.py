"""Rutas a recursos, tanto en desarrollo como dentro del .exe (PyInstaller), pues nos facilita mucho
al hacer el exe."""
import sys
from pathlib import Path


def ruta_recurso(relativa):
    base = Path(getattr(sys, "_MEIPASS", Path(__file__).resolve().parent.parent))
    return str(base / relativa)