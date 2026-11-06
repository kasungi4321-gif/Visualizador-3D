"""Conecta la ventana con el catálogo: lee la selección y redibuja."""
from app.catalogo import CATALOGOS


def redibujar(ventana):
    pestana, nombre, valores = ventana.seleccion()
    funcion = CATALOGOS[pestana][nombre][0]
    ax = ventana.lienzo.limpiar()
    ventana.info.setText(funcion(ax, *valores) or "")
    ventana.lienzo.refrescar()