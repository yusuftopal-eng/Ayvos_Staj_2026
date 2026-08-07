import cv2
from ultralytics import YOLO

# YOLOv8 nano modelinin başlatılması
model = YOLO("yolov8n.pt") 

# Dosyanın bulunduğu klasör yolundan video akışının alınması
cap = cv2.VideoCapture("test_video.mp4")

# Sayılan benzersiz kişilerin ID'lerini tutmak için Set (küme) tanımlanması
counted_ids = set()

# Sayım işleminin yapılacağı sanal referans çizgisinin Y koordinatı
line_y = 300

while True:
    ret, frame = cap.read()
    if not ret:
        print("Görüntü akışı kesildi veya kaynak sonlandı.")
        break

    # Model tahmini ve BoT-SORT algoritması ile nesne takibi (Sadece insan sınıfı)
    results = model.track(frame, classes=[0], tracker="botsort.yaml", persist=True, verbose=False)

    # Sanal sayım çizgisinin frame üzerine yeşil renk ile çizdirilmesi
    cv2.line(frame, (0, line_y), (frame.shape[1], line_y), (0, 255, 0), 2)

    # Frame içerisinde tespit edilen ve takip edilen bir nesne varsa işlemlerin yapılması
    if results[0].boxes is not None and results[0].boxes.id is not None:
        
        # Sınır kutusu (bounding box) koordinatlarının ve nesne ID'lerinin alınması
        boxes = results[0].boxes.xyxy.cpu().numpy()
        track_ids = results[0].boxes.id.cpu().numpy().astype(int)

        for box, track_id in zip(boxes, track_ids):
            x1, y1, x2, y2 = map(int, box)
            
            # Nesnenin merkez koordinatlarının hesaplanması
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2

            # Tespit edilen sınır kutularının ve ID bilgisinin frame üzerine çizdirilmesi
            cv2.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
            cv2.putText(frame, f"ID: {track_id}", (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
            cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)

            # Nesnenin merkez noktasının referans çizgisini kesme durumunun kontrolü ve sayıma eklenmesi
            if line_y - 10 < cy < line_y + 10:
                counted_ids.add(track_id)

    # Toplam sayılan kişi sayısının ekrana yansıtılması
    cv2.putText(frame, f"Toplam Kisi: {len(counted_ids)}", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # İşlenmiş görüntünün ekrana yansıtılması
    cv2.imshow("YOLOv8 + BoT-SORT Kisi Sayimi", frame)

    # 'q' tuşu ile çıkış kontrolü
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Kaynakların serbest bırakılması
cap.release()
cv2.destroyAllWindows()