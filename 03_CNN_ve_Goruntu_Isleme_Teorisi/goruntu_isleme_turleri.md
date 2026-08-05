# Görev 10: Görüntü İşleme Görevleri ve Çıktı Türleri

Bilgisayarlı görü (Computer Vision) modelleri, bir görüntüyü analiz ederken hedeflenen detay ve hassasiyet seviyesine göre farklı görevler üstlenir. Bu görevler, genel sınıflandırmadan piksel bazlı ayrıştırmaya doğru üç ana başlıkta incelenir:

## 1. Image Classification (Görüntü Sınıflandırma)
* **Amacı:** Görüntünün tamamının neyi temsil ettiğini veya hangi ana kategoriye ait olduğunu belirlemektir.
* **Çalışma Mantığı:** Model, resmin içindeki nesnelerin konumlarıyla veya detay sınırlarıyla ilgilenmez. Sadece modele giren görsele bütün olarak bakar ve eğitim sürecinde öğrendiği sınıflar arasından en yüksek olasılıklı olanı seçer.
* **Çıktı / Sonuç:** Resmin bütününe ait tek bir sınıf etiketi ve o sınıfa ait olasılık değeri (Örn: "%95 Kedi") elde edilir.
* **Uygulama Senaryoları:** Fabrika üretim hatlarında banttan geçen ürünleri "Hatalı" veya "Hatasız" olarak ayırma; e-ticaret sitelerinde yüklenen ürün görsellerini "Ayakkabı", "Gömlek" gibi kategorilere otomatik tasnif etme.

## 2. Object Detection (Nesne Tespiti)
* **Amacı:** Görüntüdeki nesnelerin hem ne olduğunu (sınıflandırma) hem de tam olarak nerede bulunduğunu (konumlandırma) tespit etmektir.
* **Çalışma Mantığı:** Model, resimdeki nesnelerin etrafına "Bounding Box" (sınır kutusu) adı verilen dikdörtgen çerçeveler çizer. Bir görüntüde birden fazla farklı nesne aynı anda tespit edilip etiketlenebilir.
* **Çıktı / Sonuç:** Tespit edilen her nesne için bir sınır kutusu koordinatı (x, y, genişlik, yükseklik), ait olduğu sınıf etiketi ve modelin bu tahmine duyduğu güven skoru (confidence score) üretilir.
* **Uygulama Senaryoları:** Otonom araçların yoldaki yayaları, diğer araçları ve trafik levhalarını anlık olarak tespit etmesi; güvenlik kameralarında izinsiz bölgeye giren insanları kutu içine alıp alarm üretmesi.

## 3. Image Segmentation (Görüntü Bölütleme)
* **Amacı:** Görüntüdeki nesneleri kaba sınır kutuları ile değil, doğrudan piksel seviyesinde hassas bir şekilde sınırlarını çizerek arka plandan veya diğer nesnelerden ayırmaktır.
* **Çalışma Mantığı:** Resmi oluşturan her bir piksel tek tek analiz edilir ve o pikselin hangi sınıfa ait olduğu belirlenir. İki alt dalı bulunur:
  * *Semantic Segmentation:* Aynı sınıftaki nesneleri tek bir bütün olarak gruplar (Örn: Resimdeki tüm arabaları aynı mavi renge boyar).
  * *Instance Segmentation:* Aynı sınıftaki nesneleri bireysel olarak ayırt eder (Örn: Yan yana duran iki arabayı farklı renklerle ayrı ayrı belirtir).
* **Çıktı / Sonuç:** Orijinal görüntüyle aynı çözünürlükte, her pikselin ait olduğu sınıfı temsil eden renkli bir maske (pixel mask) matrisi elde edilir.
* **Uygulama Senaryoları:** Tıbbi görüntülemede (MR/Röntgen vb.) tümörlü hücrelerin sınırlarının piksel hassasiyetinde çizilmesi; video konferans uygulamalarında arka planı bulanıklaştırmak için insan silüetinin arka plandan kusursuzca ayrıştırılması.