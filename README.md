# Visualizador 3D

Aplicación de escritorio que dibuja figuras tridimensionales (esfera, cilindro,
cubo) y aplica transformaciones geométricas a un cubo: traslación,
escalamiento, rotación, sesgado y perspectiva. Hecha con Python, PySide6,
Matplotlib y NumPy.

[Captura del programa](assets/captura.png)

## Uso

Abrir `Visualizador3D.exe` (no requiere instalar Python).

1. Elegir la pestaña Figuras o Transformaciones.
2. Seleccionar una opción y ajustar sus parámetros: el gráfico se actualiza al instante.
3. Rotar la vista con el ratón; el botón Restablecer vista vuelve al ángulo inicial.
4. La opción Créditos de la barra de menús muestra los datos del equipo.

## Ejecutar desde el código

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python main.py
```

## Regenerar el .exe (solo si se modifica el código)

Con el entorno activo:

```powershell
pip install pyinstaller
python -m PyInstaller --noconsole --onefile --name Visualizador3D --clean `
  --icon assets/icono.ico `
  --add-data "assets;assets" `
  --splash assets/carga_inicio.png `
  main.py
```

El resultado queda en `dist/Visualizador3D.exe`.

## Estructura

```
main.py              punto de entrada
requerimientos.txt   dependencias
assets/              ícono e imágenes de la pantalla de carga
app/
  aplicacion.py      arranque y pantalla de carga
  carga.py           clase PantallaCarga
  recursos.py        rutas a assets (también dentro del .exe)
  geometria.py       cubo y transformaciones (NumPy)
  dibujo.py          dibujo 3D (Matplotlib)
  catalogo.py        figuras y transformaciones disponibles
  controlador.py     conecta la interfaz con el dibujo
  interfaz/          ventana, lienzo, parámetros y créditos
```

## Agregar una figura o transformación

Escribir la función en `dibujo.py` (figuras) o `geometria.py`
(transformaciones) y registrarla en `catalogo.py`. La interfaz genera sola el
menú y los campos de parámetros.

## Autores

- Mario Emir Aparicio Arteaga
- Jorge Alberto Ortiz Garcia
