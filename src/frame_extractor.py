import cv2
import os

class FrameExtractor:
    def __init__(self, video_path: str, output_directory: str = None):
        """
        Clase para extraer frames de un video y guardarlos como imágenes.

        :param video_path: Ruta del video de entrada.
        :param output_directory: Carpeta donde se guardarán los frames extraídos.
        """
        # Convertir la ruta del video en una ruta absoluta
        self.video_path = os.path.abspath(video_path)

        # Ruta base del proyecto
        base_project_path = os.path.abspath(r'codigo en desarrollo\FrameExtractor')

        # Definir la carpeta de salida dentro de la ruta específica
        if output_directory is None:
            self.output_directory = os.path.join(base_project_path, "frames")
        else:
            self.output_directory = os.path.join(base_project_path, output_directory)

        # Crear directorio si no existe
        os.makedirs(self.output_directory, exist_ok=True)

    def extract_frames(self):
        """
        Extrae frames del video y los guarda en el directorio especificado.
        """
        cap = cv2.VideoCapture(self.video_path)

        # Verifica si el video se abrió correctamente
        if not cap.isOpened():
            print(f"❌ No se pudo abrir el video: {self.video_path}")
            return

        frame_count = 0

        while True:
            ret, frame = cap.read()

            if not ret:
                print(f"⚠️ Fin del video o error al leer el frame #{frame_count}")
                break

            # Verificar que el frame sea válido
            if frame is None or frame.size == 0:
                print(f"⚠️ Frame #{frame_count} es inválido.")
                continue

            # Guarda el frame como imagen en el directorio
            frame_filename = os.path.join(self.output_directory, f'frame_{frame_count:04d}.png')

            # Intentar guardar el frame y verificar si se guardó correctamente
            saved = cv2.imwrite(frame_filename, frame)

            if not saved:
                print(f"❌ No se pudo guardar el frame #{frame_count} en {frame_filename}")
            else:
                print(f"✅ Frame #{frame_count} guardado correctamente en {frame_filename}")

            frame_count += 1

        # Libera el objeto de captura
        cap.release()

        print(f"✅ Se han guardado {frame_count} frames en '{self.output_directory}'.")

    def get_total_frames(self):
        """
        Obtiene el número total de frames en el video.

        :return: Número total de frames del video.
        """
        cap = cv2.VideoCapture(self.video_path)

        # Verificar si el video se abrió correctamente
        if not cap.isOpened():
            print(f"❌ No se pudo abrir el video para contar los frames: {self.video_path}")
            return 0

        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        cap.release()  # Cerrar correctamente

        return total_frames
