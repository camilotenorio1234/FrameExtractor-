import pytest
import os
import cv2
import shutil
import numpy as np
from frame_extractor import FrameExtractor  #  Importación corregida

# Obtener la ruta base del proyecto de manera dinámica
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))  #  Ajustado para encontrar la raíz del proyecto

# Ruta del video de prueba
TEST_VIDEO_PATH = os.path.join(BASE_DIR, "data", "asi-se-realiza-un-estudio-de-la-pisada.mp4")

# Carpeta de salida de los frames
TEST_OUTPUT_DIR = os.path.join(BASE_DIR, "tests", "test_frames")

# Asegurar que el directorio de salida existe
os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)

# Crear un video de prueba si no existe
def create_test_video(video_path):
    """ Crea un video de prueba si no existe en la carpeta de datos """
    if not os.path.exists(video_path):
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Formato MP4
        out = cv2.VideoWriter(video_path, fourcc, 30.0, (640, 480))

        for _ in range(30):  # Crear 30 frames de color blanco
            frame = np.ones((480, 640, 3), dtype=np.uint8) * 255
            out.write(frame)

        out.release()

# Asegurar que el video de prueba exista antes de las pruebas
create_test_video(TEST_VIDEO_PATH)

@pytest.fixture
def frame_extractor():
    """Fixture para inicializar el extractor antes de cada prueba."""
    return FrameExtractor(TEST_VIDEO_PATH, TEST_OUTPUT_DIR)

def test_initialization(frame_extractor):
    """Prueba que la inicialización de la clase sea correcta."""
    assert os.path.exists(frame_extractor.output_directory), " El directorio de salida no se creó correctamente"
    assert os.path.isfile(frame_extractor.video_path), "El archivo de video no existe"

def test_extract_frames(frame_extractor):
    """Prueba la extracción de frames y verifica que al menos un frame se haya guardado."""
    frame_extractor.extract_frames()
    files = os.listdir(TEST_OUTPUT_DIR)
    assert len(files) > 0, "No se guardaron frames en la carpeta de salida"

def test_get_total_frames(frame_extractor):
    """Prueba que el método get_total_frames() devuelva un número mayor que cero."""
    total_frames = frame_extractor.get_total_frames()
    assert total_frames > 0, f"El total de frames devuelto es incorrecto. Se obtuvo: {total_frames}"

def test_invalid_video():
    """Prueba cómo maneja la clase un video inexistente."""
    fake_video_path = os.path.join(BASE_DIR, "data", "fake_video.mp4")

    # Asegurarse de que el archivo no existe
    if os.path.exists(fake_video_path):
        os.remove(fake_video_path)

    extractor = FrameExtractor(fake_video_path, TEST_OUTPUT_DIR)
    total_frames = extractor.get_total_frames()
    
    assert total_frames == 0, " El método get_total_frames() debería devolver 0 para un video inexistente"

def test_frame_saving():
    """Prueba que los archivos guardados son imágenes válidas."""
    frame_extractor = FrameExtractor(TEST_VIDEO_PATH, TEST_OUTPUT_DIR)
    frame_extractor.extract_frames()
    
    files = os.listdir(TEST_OUTPUT_DIR)
    if files:
        first_frame_path = os.path.join(TEST_OUTPUT_DIR, files[0])
        image = cv2.imread(first_frame_path)
        assert image is not None, f" El frame guardado no es una imagen válida en {first_frame_path}"

def test_cleanup():
    """Limpia la carpeta de test después de la ejecución de las pruebas."""
    if os.path.exists(TEST_OUTPUT_DIR):
        shutil.rmtree(TEST_OUTPUT_DIR)  # Borra todo el contenido de la carpeta
