import cv2

# 1. Ana görüntüyü gri tonlamalı okuyup %50 oranında küçültüyoruz
resim1 = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
resim1 = cv2.resize(resim1, (0, 0), fx=0.5, fy=0.5)

# 2. Eşleştirme testi için birinci resmin ortasından kırpılmış ikinci bir resim oluşturuyoruz
h, w = resim1.shape
resim2 = resim1[int(h*0.1):int(h*0.8), int(w*0.1):int(w*0.8)]

# 3. SIFT nesnesini oluşturup her iki resim için kilit noktaları ve tanımlayıcıları çıkarıyoruz
sift = cv2.SIFT_create()
kp1, des1 = sift.detectAndCompute(resim1, None)
kp2, des2 = sift.detectAndCompute(resim2, None)

# 4. BFMatcher (Brute-Force Matcher) ile kilit noktaları eşleştiriyoruz
bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
eslesmeler = bf.match(des1, des2)

# Eşleşmeleri benzerlik kalitesine (mesafeye) göre sıralıyoruz
eslesmeler = sorted(eslesmeler, key=lambda x: x.distance)

# En başarılı 25 eşleşmeyi iki görsel arasında çizgilerle birleştirip çizdiriyoruz
resim_eslesme = cv2.drawMatches(
    resim1, kp1, 
    resim2, kp2, 
    eslesmeler[:25], None, 
    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
)

# Sonucu ekranda gösterme
cv2.imshow("SIFT ile Ozellik Eslestirme", resim_eslesme)

cv2.waitKey(0)
cv2.destroyAllWindows()