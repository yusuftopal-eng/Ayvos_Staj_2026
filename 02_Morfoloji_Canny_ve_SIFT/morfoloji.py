import cv2
import numpy as np

# Görüntüyü gri tonlamalı okuyoruz
resim_gri = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

# Resmi gri tonlamalı okuyup %50 oranında küçültüyoruz
resim_gri = cv2.resize(resim_gri, (0, 0), fx=0.5, fy=0.5)

# Küçülmüş resim üzerinden eşikleme yapıyoruz
ret, esiklenmis_resim = cv2.threshold(resim_gri, 127, 255, cv2.THRESH_BINARY)

# Morfolojik işlemler için 5x5 boyutunda 1'lerden oluşan kernel matrisi
kernel = np.ones((5,5), np.uint8)

# 1 - Erode (Aşındırma): işlemi ile beyaz alanları inceltme
asindirilmis_resim = cv2.erode(esiklenmis_resim, kernel, iterations=1)

# 2 - Dilate (Genişletme): işlemi ile beyaz alanları kalınlaştırma
genisletilmis_resim = cv2.dilate(esiklenmis_resim, kernel, iterations=1)

# 3 - Opening (Açma): Önce aşındır, sonra genişlet (Dışarıdaki gürültüleri siler)
acma_resim = cv2.morphologyEx(esiklenmis_resim, cv2.MORPH_OPEN, kernel)

# 4 - Closing (Kapatma): Önce genişlet, sonra aşındır (İçerideki siyah delikleri kapatır)
kapatma_resim = cv2.morphologyEx(esiklenmis_resim, cv2.MORPH_CLOSE, kernel)

# 5 - Gradient (Gradyan): Genişletilmiş hali ile aşındırılmış hali arasındaki fark (Kenar çıkarır)
gradyan_resim = cv2.morphologyEx(esiklenmis_resim, cv2.MORPH_GRADIENT, kernel)

# 6 - Top Hat (Üst Şapka): Orijinal resim ile Açma işlemi arasındaki fark
ust_sapka_resim = cv2.morphologyEx(esiklenmis_resim, cv2.MORPH_TOPHAT, kernel)

# 7 - Black Hat (Kara Şapka): Kapatma işlemi ile orijinal resim arasındaki fark
kara_sapka_resim = cv2.morphologyEx(esiklenmis_resim, cv2.MORPH_BLACKHAT, kernel)

# Sonuçları ekranda gösterme
cv2.imshow("1 - Threshold (Esikleme)", esiklenmis_resim)
cv2.imshow("2 - Erode (Asindirma)", asindirilmis_resim)
cv2.imshow("3 - Dilate (Genisletme)", genisletilmis_resim)
cv2.imshow("4 - Opening (Acma)", acma_resim)
cv2.imshow("5 - Closing (Kapatma)", kapatma_resim)
cv2.imshow("6 - Morphological Gradient (Gradyan)", gradyan_resim)
cv2.imshow("7 - Top Hat (Ust Sapka)", ust_sapka_resim)
cv2.imshow("8 - Black Hat (Kara Sapka)", kara_sapka_resim)

# Pencerelerin kapanmaması için bekleme komutları
cv2.waitKey(0)
cv2.destroyAllWindows()