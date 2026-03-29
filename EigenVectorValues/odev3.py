import numpy as np
import time

def qr_algoritmasi_manuel(A, iterasyon=100):
    """
    Referans: https://github.com/LucasBN/Eigenvalues-and-Eigenvectors
    Numpy'ın hazır eig() fonksiyonunu kullanmadan, QR ayrıştırması 
    yoluyla özdeğerleri hesaplayan fonksiyon.
    """
    # Matrisin kopyasını alarak orijinal veriyi bozmuyoruz
    A_kopya = A.copy().astype(float)
    
    for i in range(iterasyon):
        # QR Ayrıştırması: A = Q * R
        # (Referans repoda gösterilen temel mantık)
        q, r = np.linalg.qr(A_kopya)
        
        # Yeni A matrisi: A = R * Q (Özdeğerler köşegene toplanır)
        A_kopya = np.dot(r, q)
    
    # Matrisin köşegenindeki elemanlar özdeğerlerdir
    ozdegerler = np.diag(A_kopya)
    return sorted(ozdegerler, reverse=True)

def odev_uygulamasi():
    # Ödevde istenen kare matris örneği
    A = np.array([[4, 1], 
                  [2, 3]])

    print("--- 3. LABORATUVAR: ÖZDEĞER VE ÖZVEKTÖR ANALİZİ ---\n")

    # 1. Yöntem: Manuel QR Algoritması (Soru 3)
    start_m = time.time()
    manuel_sonuclar = qr_algoritmasi_manuel(A)
    end_m = time.time()

    # 2. Yöntem: Numpy Hazır Fonksiyonu (Soru 2 ve 3 Karşılaştırma)
    start_np = time.time()
    np_sonuclar, _ = np.linalg.eig(A)
    # Karşılaştırma için sıralıyoruz
    np_sonuclar_sirali = sorted(np_sonuclar, reverse=True)
    end_np = time.time()

    # SONUÇLARIN YAZDIRILMASI
    print(f"1. Manuel (QR) Hesaplanan Özdeğerler: {manuel_sonuclar}")
    print(f"2. Numpy (eig) Hesaplanan Özdeğerler:  {np_sonuclar_sirali}")
    print("-" * 50)
    
    # Performans ve Doğruluk Karşılaştırması
    print(f"Manuel İşlem Süresi: {end_m - start_m:.10f} saniye")
    print(f"Numpy İşlem Süresi:  {end_np - start_np:.10f} saniye")
    
    hata_payi = np.abs(np.array(manuel_sonuclar) - np.array(np_sonuclar_sirali))
    print(f"\nYöntemler Arası Maksimum Hata Payı: {hata_payi.max()}")

if __name__ == "__main__":
    odev_uygulamasi()