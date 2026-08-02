import cv2

# Görüntüyü Okuma
resim = cv2.imread('test.jpg')

# Boyutlandırma (Ekrana sığması için küçültme işlemi)
yeni_boyut = (500, 500)
kucuk_resim = cv2.resize(resim, yeni_boyut)

# Gaussian Blur Uygulama
# (15, 15) bulanıklık şiddeti, tek sayı olmak zorunda.
bulanik_resim = cv2.GaussianBlur(kucuk_resim, (15, 15), 0)

# Görüntüleri Ekranda Gösterme
cv2.imshow("Orijinal Resim", kucuk_resim)
cv2.imshow("Gaussian Blur Uygulanmis Resim", bulanik_resim)

# Pencerelerin bir tuşa basana kadar kapanmaması için:
cv2.waitKey(0)
cv2.destroyAllWindows()