import cv2

# Görüntüyü gri tonlamalı okuyup %50 oranında küçültüyoruz
resim_gri = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)
resim_gri = cv2.resize(resim_gri, (0, 0), fx=0.5, fy=0.5)

# 1. SIFT (Scale-Invariant Feature Transform) Algoritması
sift = cv2.SIFT_create()
kp_sift, des_sift = sift.detectAndCompute(resim_gri, None)

# SIFT kilit noktalarını çizdirme (ölçek ve yön daireleri ile)
resim_sift = cv2.drawKeypoints(
    resim_gri, 
    kp_sift, 
    None, 
    flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS
)

# 2. ORB (Oriented FAST and Rotated BRIEF) Algoritması
orb = cv2.ORB_create()
kp_orb, des_orb = orb.detectAndCompute(resim_gri, None)

# ORB kilit noktalarını çizdirme
resim_orb = cv2.drawKeypoints(
    resim_gri, 
    kp_orb, 
    None, 
    color=(0, 255, 0), 
    flags=0
)

# Sonuçları ekranda gösterme
cv2.imshow("1 - SIFT Kilit Noktalari", resim_sift)
cv2.imshow("2 - ORB Kilit Noktalari", resim_orb)

cv2.waitKey(0)
cv2.destroyAllWindows()