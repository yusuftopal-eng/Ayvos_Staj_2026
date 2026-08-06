# Görev 11: YOLO (You Only Look Once) Teorisi ve Çalışma Mantığı

YOLO, nesne tespitini (object detection) önce bölgeleri bulup sonra sınıflandırmak gibi iki ayrı aşamada yapmak yerine, tek bir sinir ağı üzerinden tek seferde (You Only Look Once) çözen, gerçek zamanlı ve son derece hızlı bir algoritmadır.

Mimari temelde şu kavramlar üzerinden çalışır:

# 1. Grid (Izgara) Mantığı
* **Çalışma Mantığı:** YOLO, giriş görüntüsünü eşit boyutlarda (örneğin 13x13 veya 19x19) bir ızgaraya böler. 
* **Sorumluluk Alanı:** Tespit edilecek bir nesnenin merkez noktası hangi ızgara hücresinin içine düşüyorsa, o nesneyi tespit etmekten ve etrafına sınır kutusu (bounding box) çizmekten sadece o hücre sorumludur. Bu sayede tüm resmi tekrar tekrar taramak gerekmez.

# 2. Anchor Box (Referans Kutuları)
* **Amacı:** Ağın her seferinde nesnelerin boyutlarını sıfırdan tahmin etmesini engelleyerek eğitimi ve tahmini hızlandırmaktır.
* **Çalışma Mantığı:** Önceden tanımlanmış, farklı en-boy oranlarına sahip referans kutularıdır. Örneğin; bir insan için dikey bir dikdörtgen, bir araba için yatay bir dikdörtgen referans alınır. Ağ, sadece bu referans kutularını ne kadar esneteceğini veya daraltacağını hesaplar.

# 3. YOLO Versiyonlarının Gelişimi (v3 - v8 Arası Farklar)
YOLO mimarisi yıllar içinde sürekli optimize edilerek hız ve doğruluk dengesinde evrimleşmiştir:
* **YOLOv3:** Anchor box mantığının tam oturduğu, çoklu ölçek (multi-scale) tespiti sayesinde önceki versiyonlara göre küçük nesneleri bulmada çok daha başarılı olan klasikleşmiş versiyondur.
* **YOLOv4 & YOLOv5:** PyTorch entegrasyonu ve mozaik veri artırma (mosaic data augmentation) gibi tekniklerle model eğitiminin çok daha kolaylaştığı dönemdir. Özellikle YOLOv5, kullanım kolaylığı ve hafifliği ile endüstri standardı haline gelmiştir.
* **YOLOv8:** Anchor-free (referans kutusuz) yapıya geçiş yapan, günümüzün en güncel ve state-of-the-art (SOTA) modellerinden biridir. Hem nesne tespiti hem de piksel bazlı segmentasyon konularında inanılmaz hızlı ve yüksek doğruluk oranına sahiptir.