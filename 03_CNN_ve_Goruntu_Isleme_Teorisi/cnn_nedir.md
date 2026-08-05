# Görev 9: CNN (Convolutional Neural Network) Nedir ve Nasıl Çalışır?

CNN (Evrişimli Sinir Ağı), özellikle görüntü ve video işleme konularında insan beyninin görme merkezini taklit eden, görsel verileri analiz etmek için kullanılan bir derin öğrenme mimarisidir. Bir görüntüyü standart bir veri yığını olarak işlemek yerine, hiyerarşik bir şekilde parçalara bölerek anlamlandırır.

Bu ağ mimarisi temel olarak dört aşamadan oluşur:

# 1. Convolution (Evrişim) Katmanı
* **Amacı:** Görüntüden belirleyici özellikleri (features) ve örüntüleri çıkarmaktır.
* **Çalışma Mantığı:** Resmin üzerinde belirli boyutlarda filtreler (kernel/çekirdek matrisleri) gezdirilir. Eğitim aşamasında ağ, yatay çizgileri, köşeleri veya renk geçişlerini bulmak için bu filtrelerin ağırlıklarını otomatik olarak günceller.
* **Matematiksel Mantığı:** Görüntü Matrisi × Filtre (Kernel) Matrisi = Özellik Haritası (Feature Map)
* **Çıktı / Sonuç:** Görüntüdeki önemli detayların vurgulandığı "Özellik Haritası" (Feature Map) adı verilen yeni bir matris elde edilir.

# 2. Activation (Aktivasyon - ReLU) Katmanı
* **Amacı:** Modele doğrusal olmayan (non-linear) özellikler kazandırmaktır.
* **Çalışma Mantığı:** Convolution katmanından çıkan sonuçlar genellikle ReLU (Rectified Linear Unit) fonksiyonundan geçirilir. Bu fonksiyon, negatif değerleri sıfırlar ve pozitif değerleri aynen bırakır.
* **Matematiksel Mantığı:** f(x) = max(0, x) (Yani değer 0'dan küçükse 0 yap, büyükse aynen bırak)
* **Çıktı / Sonuç:** Negatif (gereksiz) değerlerden arındırılmış, ağın daha karmaşık ve eğimli şekilleri öğrenebilmesine olanak tanıyan doğrusal olmayan özellik haritaları üretilir.

# 3. Pooling (Havuzlama / Ortaklama) Katmanı
* **Amacı:** Görüntünün uzamsal boyutunu küçültmek, hesaplama maliyetini düşürmek ve aşırı öğrenmeyi (overfitting) engellemektir.
* **Çalışma Mantığı:** En yaygın kullanılan "Max Pooling" yönteminde, belirlenen bir pencere (örn. 2x2) özellik haritası üzerinde gezer ve o çerçevenin içindeki en yüksek değeri alır.
* **Matematiksel Mantığı:** Belirlenen N x N boyutundaki bir matris alanındaki en büyük sayıyı (maksimum piksel değerini) seçerek yeni matrise yazar.
* **Çıktı / Sonuç:** Boyutları küçültülmüş, nesnenin resimdeki konumundan bağımsız olarak (Konumsal Değişmezlik) tanınmasını sağlayan özet bir matris yapısı elde edilir.

# 4. Fully Connected (Tam Bağlı) Katmanı
* **Amacı:** Önceki katmanlardan elde edilen süzülmüş özelliklere dayanarak nihai sınıflandırma (tahmin) işlemini gerçekleştirmektir.
* **Çalışma Mantığı:** Pooling katmanından çıkan çok boyutlu matrisler "Flatten" (düzleştirme) işlemiyle tek boyutlu bir vektöre dönüştürülür. Bu vektör, klasik yapay sinir ağına aktarılır ve matematiksel ağırlıklara göre olasılık dağılımı hesaplanır.
* **Matematiksel Mantığı:** Çıkış = (Girdiler × Ağırlıklar) + Bias değeri (Temel denklem: Y = W*X + B)
* **Çıktı / Sonuç:** Modelin görüntüyü analiz etmesi sonucunda, görüntünün hangi sınıfa ait olduğunu gösteren nihai olasılık yüzdeleri (örneğin; %92 Kedi, %8 Köpek) elde edilir.