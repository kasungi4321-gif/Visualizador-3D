"""Funciones de dibujo 3D (Matplotlib). Cada una recibe los ejes y sus parámetros."""
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

from app.geometria import ARISTAS, CARAS, CUBO


def preparar(ax, titulo, puntos):
    """Título, etiquetas y ejes con la misma escala."""
    p = np.reshape(puntos, (-1, 3))
    centro = (p.min(0) + p.max(0)) / 2
    medio = max(np.ptp(p, axis=0).max() / 2, 0.5) * 1.1
    ax.set_title(titulo)
    for eje, c in zip("xyz", centro):
        getattr(ax, f"set_{eje}label")(eje.upper())
        getattr(ax, f"set_{eje}lim")(c - medio, c + medio)
    ax.set_box_aspect((1, 1, 1))


def dibujar_cubo(ax, v, color, label):
    for a, b in ARISTAS:
        ax.plot(*zip(v[a], v[b]), c=color)
    ax.scatter(*v.T, c=color, label=label)


def _superficie(ax, titulo, x, y, z, **estilo):
    ax.plot_surface(x, y, z, **estilo)
    preparar(ax, titulo, np.column_stack([x.ravel(), y.ravel(), z.ravel()]))


def _esfera(r, n):
    u, v = np.linspace(0, 2 * np.pi, n), np.linspace(0, np.pi, n)
    return (r * np.outer(np.cos(u), np.sin(v)),
            r * np.outer(np.sin(u), np.sin(v)),
            r * np.outer(np.ones(n), np.cos(v)))


# Figuras: f(ax, *parámetros)
def punto_cubo(ax, x, y, z):
    dibujar_cubo(ax, CUBO, "b", "Cubo")
    ax.scatter(x, y, z, c="r", s=100, label=f"Punto ({x:g},{y:g},{z:g})")
    ax.legend()
    preparar(ax, "Punto y cubo", np.vstack([CUBO, [x, y, z]]))


def esfera(ax, r, n):
    _superficie(ax, "Esfera", *_esfera(r, n), color="cyan", edgecolor="k", alpha=0.6)


def esfera_parametrica(ax, r, n):
    _superficie(ax, "Esfera paramétrica", *_esfera(r, n), color="b", edgecolor="k", alpha=0.6)


def cubo_caras(ax):
    ax.add_collection3d(Poly3DCollection(
        CUBO[CARAS], facecolors="cyan", edgecolors="r", linewidths=1, alpha=0.5))
    preparar(ax, "Cubo por caras", CUBO)


def cilindro(ax, r, h, n):
    t, z = np.meshgrid(np.linspace(0, 2 * np.pi, n), np.linspace(0, h, n))
    _superficie(ax, "Cilindro", r * np.cos(t), r * np.sin(t), z,
                color="orange", edgecolor="k", alpha=0.7)


def transformacion(ax, nombre, resultado):
    dibujar_cubo(ax, CUBO, "b", "Original")
    dibujar_cubo(ax, resultado, "r", nombre)
    ax.legend()
    preparar(ax, nombre, np.vstack([CUBO, resultado]))