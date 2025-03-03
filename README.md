# FrameExtractor 🎥🖼️

FrameExtractor is a simple and efficient tool for extracting frames from videos using Python and OpenCV. It allows capturing and storing images from a video in a specific folder, making it useful for video analysis, machine learning, and image processing.

This README is available in **Spanish** and **English**. Expand the corresponding section to view the documentation in your preferred language.

<details>
  <summary>FrameExtractor 🎥🖼️  English</summary>

  # FrameExtractor 🎥🖼️

Extract frames from videos easily with Python and OpenCV.

## 📌 Description

FrameExtractor is a simple tool to extract frames from a video and save them as images in a specific folder.
Ideal for video analysis, machine learning, and image processing.

## 📁 Project Structure

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


# 🚀 Installation and Usage

## 📌 1. Clone the repository

```sh
git clone [https://github.com/tu_usuario/FrameExtractor.git](https://github.com/camilotenorio1234/FrameExtractor-/tree/main)
cd FrameExtractor
```

## 📌 2. Install dependencies

Make sure you have Python 3 installed. Then, run:

```sh
pip install -r requirements.txt
```

## 📌 3. Run the extractor

Run main.py to extract frames from a video:

```sh
python src/main.py
```

The extracted frames will be saved in the frames/ folder.

## ⚙️ Usage in code

You can use the FrameExtractor class in your own Python scripts:

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

## ✅ Unit Tests

This project uses pytest for automated testing.
To run the tests, use:

```sh
pytest src/
```

If you want more details:

```sh
pytest -v
```

## 📊 Test Results

The tests were run on Python 3.9 with pytest 8.3.4.
Here are the results:

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

</details>


---

FrameExtractor es una herramienta simple y eficiente para extraer frames de videos usando Python y OpenCV. Permite capturar y almacenar imágenes de un video en una carpeta específica, facilitando el análisis de video, aprendizaje automático y procesamiento de imágenes. 

Este README está disponible en **español** e **inglés**. Despliega la sección correspondiente para ver la documentación en tu idioma.


<details>
  <summary>FrameExtractor 🎥🖼️  Español</summary>

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

</details>

