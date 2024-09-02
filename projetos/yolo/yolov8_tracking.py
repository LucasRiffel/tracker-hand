import cv2
import numpy as np
from ultralytics import YOLO

# Caminho do vídeo
video_path = r"C:\Users\lucas\Videos\4K Road traffic video for object detection and tracking - free download now!.mp4"

# Carregar o modelo YOLOv8
model = YOLO('yolov8n.pt')

# Abrir o arquivo de vídeo
cap = cv2.VideoCapture(video_path)

# Inicializar o gravador de vídeo
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_video_path = video_path.split('.')[0] + '_tracked.mp4'  # Nome do arquivo de saída com sufixo '_tracked'
frame_rate = cap.get(cv2.CAP_PROP_FPS)
frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
out = cv2.VideoWriter(output_video_path, fourcc, frame_rate, frame_size)

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break

    results = model(frame)
    annotated_frame = frame.copy()

    if results[0].boxes and results[0].boxes.id is not None:
        boxes = results[0].boxes.xyxy.cpu()  # Coordenadas das caixas delimitadoras (x1, y1, x2, y2)
        track_ids = results[0].boxes.id.int().cpu().tolist()  # IDs de rastreamento

        for box, track_id in zip(boxes, track_ids):
            x1, y1, x2, y2 = map(int, box)  # Coordenadas da caixa delimitadora
            track_id = int(track_id)

            # Extrair a região de interesse (ROI) da caixa delimitadora
            roi = frame[y1:y2, x1:x2]

            # Converter a ROI para escala de cinza
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

            # Aplicar um threshold binário para segmentar a área
            _, binary_roi = cv2.threshold(gray_roi, 127, 255, cv2.THRESH_BINARY)

            # Detectar contornos na ROI binarizada
            contours, _ = cv2.findContours(binary_roi, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            # Desenhar o contorno ao redor do objeto detectado na imagem original
            for contour in contours:
                contour[:, :, 0] += x1  # Ajustar a coordenada x
                contour[:, :, 1] += y1  # Ajustar a coordenada y'
                cv2.drawContours(annotated_frame, [contour], -1, (0, 255, 0), thickness=2)

            # Adicionar o ID de rastreamento acima do retângulo
            cv2.putText(annotated_frame, f'ID: {track_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Escrever o quadro anotado no vídeo de saída
    out.write(annotated_frame)

    # Mostrar o vídeo em tempo real (opcional)
    cv2.imshow('Tracked Video', annotated_frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar os recursos
cap.release()
out.release()
cv2.destroyAllWindows()

