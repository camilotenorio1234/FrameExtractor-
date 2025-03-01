from frame_extractor import FrameExtractor
import os

# Definir la ruta absoluta del video dentro del proyecto
video_path = os.path.abspath(r"codigo en desarrollo/FrameExtractor/data/asi-se-realiza-un-estudio-de-la-pisada-recomendado-por-los-medicos-para-correr-y-caminar.mp4")

if __name__ == "__main__":
    extractor = FrameExtractor(video_path)
    extractor.extract_frames()

    total_frames = extractor.get_total_frames()
    print(f"🔢 El video tiene un total de {total_frames} frames extraídos.")
