import numpy as np
import math
import cv2
import time

def gaussian_kernel_olustur(boyut, sigma):
    # Filtremizin merkez noktasını buluyoruz.
    merkez = boyut // 2
    
    # İçi sıfırlarla dolu, istediğimiz boyutta boş bir matris oluşturuyoruz.
    kernel = np.zeros((boyut, boyut))
    
    # Matrisin her hücresini tek tek dolaşıyoruz
    for x in range(boyut):
        for y in range(boyut):

            # Bulunduğumuz noktanın merkeze uzaklığını hesaplıyoruz
            x_uzaklik = x - merkez
            y_uzaklik = y - merkez
            
            # GAUSSIAN FORMÜLÜ 
            # Pi sayısı için math.pi kullanıyoruz.
            pay = -(x_uzaklik**2 + y_uzaklik**2) / (2 * (sigma**2))
            payda = 2 * math.pi * (sigma**2)

            # Formüldeki e^ üzeri işlemi için np.exp() kullanıyoruz.
            kernel[x, y] = np.exp(pay) / payda

    # Normalizasyon: Matrisi kendi toplamına bölerek genel toplamı 1 yapıyoruz
    kernel = kernel / np.sum(kernel)

    return kernel

def konvolusyon_uygula(resim, kernel):
    # Resim ve Kernel boyutlarını alıyoruz
    resim_yukseklik, resim_genislik = resim.shape
    kernel_boyut = kernel.shape[0]
    
    # Padding (Çerçeve) kalınlığını hesaplıyoruz
    pad_miktari = kernel_boyut // 2
    
    # Reflect (Aynalama) yöntemiyle resmin etrafına sanal çerçeve ekliyoruz
    cerceveli_resim = np.pad(resim, pad_miktari, mode='reflect')
    
    # Sonuçları kaydedeceğimiz, orijinal resimle aynı boyutta simsiyah boş bir tuval oluşturuyoruz
    yeni_resim = np.zeros((resim_yukseklik, resim_genislik))
    
    # Filtreyi resmin üzerinde kaydırma döngüleri
    for y in range(resim_yukseklik):
        for x in range(resim_genislik):
            
            # Büyütecin (Kernel'in) o anki konumunda gördüğü alanı (kesiti) alıyoruz
            kesit = cerceveli_resim[y : y + kernel_boyut, x : x + kernel_boyut]
            
            # Kesit ile Kernel'i karşılıklı çarpıp topluyoruz
            yeni_piksel = np.sum(kesit * kernel)
            
            # Çıkan değeri yeni tuvalimizdeki yerine koyuyoruz
            yeni_resim[y, x] = yeni_piksel
            
    return yeni_resim

# Fonksiyonu test etmek için 5x5 boyutunda ve sigma değeri 1.0 olan bir filtre istiyoruz.
benim_filtrem = gaussian_kernel_olustur(5, 1.0)

# Ekrana düzgün yazdırabilmek için virgülden sonrasının ayarlamasını yapıyoruz (virgülden sonra 4 hane)
np.set_printoptions(formatter={'float': '{: 0.4f}'.format})

print("Oluşturulan Normalleştirilmiş Kernel:")
print(benim_filtrem)
print("Yeni Matrisin Toplamı:", np.sum(benim_filtrem))




# --- TEST VE KARŞILAŞTIRMA AŞAMASI ---

# Bulanıklığı daha net görebilmek için kernel boyutunu 15x15, sigma'yı 5.0 yapıyoruz
benim_filtrem = gaussian_kernel_olustur(15, 5.0)

# Resmi siyah-beyaz olarak içeri alıyoruz
orijinal_resim = cv2.imread('test.jpg', cv2.IMREAD_GRAYSCALE)

print("\n1. Kendi Algoritmamız Çalışıyor...")
print("(Lütfen işlem bitene kadar bekleyiniz...)")

# Kendi fonksiyonumuzun süresini ölçüyoruz
baslangic_benim = time.time()
bulanik_resim_benim = konvolusyon_uygula(orijinal_resim, benim_filtrem)
bitis_benim = time.time()

# Çıkan küsuratlı sonucu 0-255 arası tamsayılara (resim formatına) çeviriyoruz
bulanik_resim_benim = np.uint8(bulanik_resim_benim)
sure_benim = bitis_benim - baslangic_benim
print(f"-> Kendi kodumuzun çalışma süresi: {sure_benim:.4f} saniye")

print("\n2. OpenCV'nin Hazır Fonksiyonu Çalışıyor...")

# OpenCV'nin süresini ölçüyoruz
baslangic_cv2 = time.time()
bulanik_resim_cv2 = cv2.GaussianBlur(orijinal_resim, (15, 15), 5.0)
bitis_cv2 = time.time()

sure_cv2 = bitis_cv2 - baslangic_cv2
print(f"-> OpenCV'nin çalışma süresi: {sure_cv2:.4f} saniye")

# İstatistik yazdıralım
hiz_farki = sure_benim / sure_cv2 if sure_cv2 > 0 else 0
print(f"\nSONUÇ: OpenCV bizim Python döngülerimizden yaklaşık {hiz_farki:.0f} kat daha hızlı çalıştı!")

# Tüm sonuçları yan yana ekranda açıyoruz
cv2.imshow("1 - Orijinal Resim", orijinal_resim)
cv2.imshow("2 - Kendi Yazdigimiz (15x15 Yogun Blur)", bulanik_resim_benim)
cv2.imshow("3 - OpenCV (15x15 Yogun Blur)", bulanik_resim_cv2)

print("\nİşlem tamamlandı! Pencereleri kapatmak için herhangi bir tuşa basabilirsin.")
cv2.waitKey(0)
cv2.destroyAllWindows()