import cv2
from ultralytics import YOLO

# YOLOv8 nano modelinin başlatılması
model = YOLO("04_YOLO_Teorisi_ve_Insan_Tespiti/yolov8n.pt") 

# Dosyanın bulunduğu klasör yolunu ekliyoruz
cap = cv2.VideoCapture("04_YOLO_Teorisi_ve_Insan_Tespiti/test_video.mp4")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü akışı kesildi veya kaynak sonlandı.")
        break

    # Model tahmini: Sadece insan (class 0) tespiti ve %50 güven skoru (confidence) eşiği
    results = model(frame, classes=[0], conf=0.5)

    # Tespit edilen sınır kutularının (bounding box) frame üzerine çizdirilmesi
    annotated_frame = results[0].plot()

    # İşlenmiş görüntünün ekrana yansıtılması
    cv2.imshow("YOLOv8 Insan Tespiti", annotated_frame)

    # 'q' tuşu ile çıkış kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakların serbest bırakılması
cap.release()
cv2.destroyAllWindows()