# 3. Laboratuvar Ödevi: Özdeğer ve Özvektör Analizi

## 1. Matris Manipülasyonu, Özdeğer ve Özvektör Tanımları ve Makine Öğrenmesi ile İlişkisi

### Temel Tanımlar

* **Matris Manipülasyonu:** En basit haliyle matrisler, sayıların satır ve sütunlar şeklinde dizildiği tablolardır. Bilgisayar bilimlerinde biz bunlara **2D Array (2 Boyutlu Dizi)** diyoruz. Bu matrisler üzerinde yaptığımız toplama, çarpma veya tersini alma gibi işlemlerin tamamına matris manipülasyonu denir. Makine öğrenmesinde veriyi bilgisayara tanıtmak ve üzerinde işlem yapabilmek için bu manipülasyonları sürekli kullanırız.
* **Özvektör (Eigenvector) ve Özdeğer (Eigenvalue):** Normalde bir matrisle bir vektörü çarptığımızda o vektörün hem yönü hem de boyu değişir. Ancak bazı özel vektörler vardır ki, matrisle çarpılsalar bile yönleri hiç değişmez, sadece boyları uzar veya kısalır. 
    * Yönü değişmeyen bu "sadık" vektörlere **özvektör** diyoruz.
    * Bu vektörün ne kadar uzadığını veya kısaldığını gösteren katsayıya ($\lambda$) ise **özdeğer** diyoruz.
* **Matematiksel İfade:** Bu durumu $Av = \lambda v$ formülüyle gösteririz (Burada $A$ matris, $v$ özvektör, $\lambda$ ise özdeğerdir).



---

### Makine Öğrenmesi ile İlişkisi ve Kullanılan Yöntemler

Makine öğrenmesinde özdeğerler ve özvektörler aslında verinin "özetini" çıkarmamıza yarar. En önemli kullanım alanları şunlardır:

1.  **Boyut İndirgeme (PCA - Temel Bileşen Analizi):** Makine öğrenmesinde elimizde bazen yüzlerce özellik (sütun) olur ve bunların hepsi önemli değildir. **PCA** algoritması, verideki en önemli yönleri bulmak için özdeğer ve özvektörleri kullanır. En büyük özdeğere sahip olan özvektör, verinin en çok bilgi içeren kısmını temsil eder. Böylece veriyi bilgisayarı yormadan sadeleştirmiş oluruz.
2.  **Özellik Çıkarımı (Feature Extraction):** Özellikle görüntü işleme gibi alanlarda, bir resmin en belirgin hatlarını (kenarlar, dokular vb.) matematiksel olarak ifade etmek için matrislerin özdeğer analizinden yararlanılır.
3.  **Tavsiye Sistemleri:** Netflix veya Spotify gibi platformların sunduğu öneri algoritmalarında, büyük veri matrislerini daha anlamlı küçük parçalara ayırmak için bu kavramlar temel teşkil eder.

---

### Kaynakça
* *Introduction to Matrices and Matrix Arithmetic for Machine Learning - MachineLearningMastery.com*
* *Gentle Introduction to Eigenvalues and Eigenvectors for Machine Learning - MachineLearningMastery.com*