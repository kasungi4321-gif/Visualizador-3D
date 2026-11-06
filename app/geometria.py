"""Datos del cubo y transformaciones."""
import numpy as np

CUBO = np.array([
    [0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0],
    [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1],
], dtype=float)

ARISTAS = [(0, 1), (1, 2), (2, 3), (3, 0), (4, 5), (5, 6),
           (6, 7), (7, 4), (0, 4), (1, 5), (2, 6), (3, 7)]

CARAS = np.array([[0, 1, 2, 3], [4, 5, 6, 7], [0, 1, 5, 4],
                  [2, 3, 7, 6], [1, 2, 6, 5], [4, 7, 3, 0]])


def _texto(m):
    return "\n".join("  ".join(f"{v:7.3f}" for v in fila) for fila in m)


def _rot(eje, grados):
    """Matriz de rotación alrededor de un eje (0=X, 1=Y, 2=Z)."""
    c, s = np.cos(np.radians(grados)), np.sin(np.radians(grados))
    i, j = [(1, 2), (2, 0), (0, 1)][eje]
    m = np.eye(3)
    m[i, i] = m[j, j] = c
    m[i, j], m[j, i] = -s, s
    return m


# Cada transformación devuelve (vértices resultantes, texto informativo)
def traslacion(tx, ty, tz):
    return CUBO + [tx, ty, tz], f"t = ({tx:g}, {ty:g}, {tz:g})"


def escalamiento(sx, sy, sz):
    return CUBO * [sx, sy, sz], _texto(np.diag([sx, sy, sz]))


def rotacion(rx, ry, rz):
    R = _rot(2, rz) @ _rot(1, ry) @ _rot(0, rx)
    return CUBO @ R.T, _texto(R)


def sesgado(xy, xz):
    Sh = np.array([[1, xy, xz], [0, 1, 0], [0, 0, 1]])
    return CUBO @ Sh.T, _texto(Sh)


def perspectiva(d):
    p = CUBO.copy()
    p[:, :2] /= CUBO[:, 2:3] / d + 1
    return p, f"x' = x / (z/d + 1)\ny' = y / (z/d + 1)\nd = {d:g}"