# FrameExtractor 🎥🖼️

Extrae frames de videos fácilmente con Python y OpenCV.

## 📌 Descripción

FrameExtractor es una herramienta sencilla para extraer frames de un video y guardarlos como imágenes en una carpeta específica.
Ideal para análisis de video, aprendizaje automático y procesamiento de imágenes.

## 📁 Estructura del Proyecto

```sh
FrameExtractor/
├── data/                           
│   ├── ejemplo_video.mp4           
├── frames/                        
│   ├── frame_0000.png              
│   ├── frame_0001.png
│   ├── ...
├── src/                            
│   ├── frame_extractor.py          
│   ├── main.py                     
│   ├── utils.py                    
│   ├── test_frame_extractor.py     
├── requirements.txt                 
├── .gitignore                      
├── README.md                       
```


# 🚀 Instalación y Uso

## 📌 1. Clonar el repositorio

```sh
git clone [https://github.com/tu_usuario/FrameExtractor.git](https://github.com/camilotenorio1234/FrameExtractor-/tree/main)
cd FrameExtractor
```

## 📌 2. Instalar dependencias

Asegúrate de tener Python 3 instalado. Luego, ejecuta:

```sh
pip install -r requirements.txt
```

## 📌 3. Ejecutar el extractor

Ejecuta main.py para extraer los frames de un video:

```sh
python src/main.py
```

Los frames extraídos se guardarán en la carpeta frames/.

## ⚙️ Uso en código

Puedes usar la clase FrameExtractor en tus propios scripts de Python:

```sh
from src.frame_extractor import FrameExtractor

# Ruta del video
video_path = "data/ejemplo_video.mp4"

# Inicializar extractor
extractor = FrameExtractor(video_path)

# Extraer frames
extractor.extract_frames()

# Obtener número total de frames
total_frames = extractor.get_total_frames()
print(f"Total de frames: {total_frames}")
```

## ✅ Pruebas Unitarias

Este proyecto usa pytest para pruebas automatizadas.
Para ejecutar las pruebas, usa:

```sh
pytest src/
```

Si quieres ver más detalles:

```sh
pytest -v
```

## 📊 Resultados de las pruebas

Las pruebas se ejecutaron en Python 3.9 con pytest 8.3.4.
Aquí están los resultados:

```sh
======================================================================== test session starts =========================================================================
platform win32 -- Python 3.9.19, pytest-8.3.4, pluggy-1.5.0 -- C:\Users\JuanC\anaconda3\envs\env_tesis_3_9\python.exe
cachedir: .pytest_cache
rootdir: C:\Users\JuanC\OneDrive\Escritorio\codigos python\codigo en desarrollo\FrameExtractor
plugins: anyio-4.3.0, dash-2.16.1
collected 6 items

src/test_frame_extractor.py::test_initialization PASSED                                                                                                         [ 16%]
src/test_frame_extractor.py::test_extract_frames PASSED                                                                                                         [ 33%]
src/test_frame_extractor.py::test_get_total_frames PASSED                                                                                                       [ 50%]
src/test_frame_extractor.py::test_invalid_video PASSED                                                                                                          [ 66%]
src/test_frame_extractor.py::test_frame_saving PASSED                                                                                                           [ 83%]
src/test_frame_extractor.py::test_cleanup PASSED                                                                                                                [100%]

========================================================================= 6 passed in 0.68s ========================================================================== 
```
