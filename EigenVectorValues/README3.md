# 3. Kısım: Özdeğer Hesaplama Uygulaması ve Analiz

Bu bölümde, 2. kısımda teknik detayları incelenen `numpy.linalg.eig` fonksiyonunun işlevi, herhangi bir hazır kütüphane fonksiyonu kullanmadan **Güç Yöntemi (Power Iteration)** algoritmasıyla uygulanmıştır. Çalışmanın amacı, teorik bir algoritma ile optimize edilmiş hazır bir fonksiyon arasındaki farkları gözlemlemektir.

### 1. Uygulanan Algoritma: Güç Yöntemi
Kodlama aşamasında, rastgele bir başlangıç vektörünün matrisle iteratif olarak çarpılmasına dayanan Güç Yöntemi tercih edilmiştir. Bu yöntem, her adımda yapılan normalizasyon işlemleriyle vektörün en baskın özvektör doğrultusuna yakınsamasını sağlar. Karakteristik denklem çözümüne göre kodlaması daha verimli ve bilgisayar bilimlerindeki iteratif süreçleri anlamak açısından daha uygundur.



### 2. Numpy ile Karşılaştırma ve Gözlemler

Güç Yöntemi uygulaması ile Numpy sonuçları kıyaslandığında şu teknik çıkarımlara varılmıştır:

* **Kapsam ve Çıktı:** Güç Yöntemi yapısı gereği matristeki yalnızca **en büyük (dominant)** özdeğeri bulabilirken; Numpy, QR ayrıştırması gibi daha ileri yöntemler kullanarak matrisin tüm özdeğer ve özvektör setini tek seferde sunmaktadır.
* **Hassasiyet:** Küçük ölçekli matrislerde her iki yöntem de birbirine çok yakın sonuçlar üretmiştir. Ancak Numpy'ın LAPACK tabanlı altyapısı, çok daha yüksek basamak hassasiyeti (floating-point precision) sağlamaktadır. Manuel uygulamada benzer hassasiyete ulaşmak için iterasyon sayısının artırılması gerekmektedir.
* **Performans:** Matris boyutları büyüdükçe Python döngüleri üzerinde çalışan manuel algoritmanın işlem süresi artmaktadır. 2. kısımda belirtilen $O(n^3)$ karmaşıklığına rağmen Numpy, düşük seviyeli dil optimizasyonları sayesinde çok daha hızlı sonuç vermektedir.

### 3. Genel Değerlendirme
Bu uygulama, özdeğer hesaplamanın temel mantığını ve iteratif yaklaşımların çalışma prensibini somutlaştırmıştır. Güç Yöntemi, algoritmanın işleyişini anlamak açısından oldukça öğretici olsa da; hız, tüm özdeğerleri kapsama ve yüksek doğruluk payı gibi kriterler söz konusu olduğunda Numpy gibi profesyonel araçların sağladığı avantajlar net bir şekilde anlaşılmıştır.