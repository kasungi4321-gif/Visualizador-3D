"""Catálogos: cada entrada es  nombre: (función de dibujo, [parámetros de la interfaz]).

Parámetro = (etiqueta, mínimo, máximo, valor[, paso]).
paso >= 1 genera un campo entero; el paso es opcional (0.1 por defecto).
Toda función de dibujo recibe (ax, *valores) y puede devolver un texto informativo.
"""
from app import dibujo, geometria


def _transf(nombre, funcion):
    """Convierte una transformación de geometria en una función de dibujo."""
    def dibujar(ax, *valores):
        resultado, texto = funcion(*valores)
        dibujo.transformacion(ax, nombre, resultado)
        return texto
    return dibujar


FIGURAS = {
    "Punto y cubo": (dibujo.punto_cubo, [("X", -10, 10, 1), ("Y", -10, 10, 2), ("Z", -10, 10, 3)]),
    "Esfera": (dibujo.esfera, [("Radio", 0.1, 10, 1), ("Resolución", 8, 200, 50, 1)]),
    "Cubo por caras": (dibujo.cubo_caras, []),
    "Esfera paramétrica": (dibujo.esfera_parametrica, [("Radio", 0.1, 10, 1), ("Resolución", 8, 200, 50, 1)]),
    "Cilindro": (dibujo.cilindro, [("Radio", 0.1, 10, 1), ("Altura", 0.1, 20, 2), ("Resolución", 8, 200, 50, 1)]),
}

TRANSFORMACIONES = {
    "Traslación": (_transf("Traslación", geometria.traslacion),
                   [("tx", -10, 10, 2), ("ty", -10, 10, 3), ("tz", -10, 10, 1)]),
    "Escalamiento": (_transf("Escalamiento", geometria.escalamiento),
                     [("sx", 0.1, 10, 2), ("sy", 0.1, 10, 0.5), ("sz", 0.1, 10, 1.5)]),
    "Rotación": (_transf("Rotación", geometria.rotacion),
                 [("Rot. X (°)", -360, 360, 0, 5), ("Rot. Y (°)", -360, 360, 0, 5),
                  ("Rot. Z (°)", -360, 360, 45, 5)]),
    "Sesgado": (_transf("Sesgado", geometria.sesgado),
                [("sh_xy", -5, 5, 1), ("sh_xz", -5, 5, 0.5)]),
    "Perspectiva": (_transf("Perspectiva", geometria.perspectiva),
                    [("Distancia d", 0.5, 50, 5, 0.5)]),
}

CATALOGOS = {"Figuras": FIGURAS, "Transformaciones": TRANSFORMACIONES}