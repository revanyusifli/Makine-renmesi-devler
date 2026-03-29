# 2. Kısım: Numpy linalg.eig Fonksiyonu Teknik İncelemesi

Bu bölümde, makine öğrenmesi ve veri biliminde sıkça kullandığımız `numpy.linalg.eig` fonksiyonunun arka plandaki çalışma mekanizmasını, resmi dokümantasyonu ve kaynak kodları üzerinden inceledim.

### Fonksiyonun Temel Amacı
`numpy.linalg.eig(a)` fonksiyonu, girdi olarak verilen kare bir matrisin ($A$) özdeğerlerini ($\lambda$) ve bunlara karşılık gelen sağ özvektörlerini ($v$) hesaplar. Fonksiyon temel olarak şu matematiksel eşitliği çözer:
$$A \cdot v = \lambda \cdot v$$

### Dokümantasyon ve Kaynak Kod Analizi

Numpy'ın resmi dokümantasyonunu ve GitHub üzerindeki `linalg.py` kaynak kodlarını incelediğimde şu teknik detaylara ulaştım:

**1. Hata Kontrolü ve Ön Hazırlık:**
Kaynak kod seviyesinde fonksiyonun ilk yaptığı iş, girdi olarak verilen matrisin tipini ve boyutunu kontrol etmektir. Matrisin mutlaka "kare" (satır ve sütun sayısı eşit) olması gerekir. Eğer kare bir matris girilmezse, Numpy `LinAlgError` hatası fırlatarak işlemi durdurur.

**2. LAPACK Entegrasyonu (Arka Plan):**
Numpy, bu ağır matematiksel hesaplamaları doğrudan Python diliyle yapmaz. Kaynak kodda gördüğüm üzere, fonksiyon aslında bir "wrapper" (sarmalayıcı) görevi görür. Asıl hesaplama işini, Fortran ve C ile yazılmış olan yüksek performanslı **LAPACK** (Linear Algebra Package) kütüphanesine devreder. 
* Gerçek sayılar içeren matrisler için `dgeev` rutini kullanılır.
* Karmaşık sayılar içeren matrisler için `zgeev` rutini devreye girer.

**3. Kullanılan Algoritma ve Karmaşıklık:**
Fonksiyon, özdeğerleri bulmak için genellikle **QR Algoritması** mantığını kullanır. Matris önce "Hessenberg Formu"na dönüştürülür ve ardından iteratif yöntemlerle çözüme gidilir. Dokümantasyonda işlemin zaman karmaşıklığının $O(n^3)$ olduğu belirtilmiştir; yani matris boyutu arttıkça işlem yükü kübik bir hızla artmaktadır.

**4. Çıktıların Formatı:**
* **Normalizasyon:** Fonksiyonun döndürdüğü özvektörlerin her birinin öklid normu (boyu) 1'e eşittir. Bu, sonuçların standart ve karşılaştırılabilir olmasını sağlar.
* **Veri Tipleri:** Girdi matrisi gerçek sayılardan oluşsa bile, bazı durumlarda özdeğerler karmaşık (complex) sayılar olabilir. Numpy bu durumu otomatik olarak yönetir.

### Sonuç
Yaptığım inceleme sonucunda, `linalg.eig` fonksiyonunun sadece bir Python fonksiyonu olmadığını, arkasında onlarca yıllık optimize edilmiş matematiksel kütüphanelerin (LAPACK) gücünü barındıran, performans odaklı bir araç olduğunu anladım.