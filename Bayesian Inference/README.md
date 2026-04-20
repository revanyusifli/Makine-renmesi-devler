# Makine Öğrenmesi 4. Ödev - Bayesyen Çıkarım

Bu ödevde, uzak bir galaksinin parlaklık verilerini analiz ediyoruz. Astronomide veriler genelde çok gürültülü olduğu için gerçek değerleri bulmak zor oluyor, bu yüzden Bayesyen yöntemleri kullanarak bir simülasyon yapmamız gerek. Amacımız, gürültülü veriler üzerinden galaksinin asıl parlaklığını ($\mu$) ve ölçüm hatasını ($\sigma$) tahmin etmekti.

### Ne Yapmamız gerek?
Verilen parametrelerle (`mu=150.0`, `sigma=10.0`) 50 tane sahte gözlem verisi üretiyoruz. Sonra bu verileri kullanarak Bayesyen fonksiyonlarını (Likelihood, Prior, Posterior) tanımlıyoruz. MCMC simülasyonu koşturuyoruz ve binlerce deneme sonucunda en mantıklı parametreleri bulmaya çalışıyoruz.

### Simülasyon Sonuçları
Kodumdan aldığım sonuçlarla doldurduğum tablo şu şekilde:

| Değişken | Gerçek Değer | Tahmin Edilen | Alt Sınır | Üst Sınır | Mutlak Hata |
| :--- | :---: | :---: | :---: | :---: | :---: |
| μ (Parlaklık) | 150.0 | 147.79 | 146.43 | 149.08 | 2.21 |
| σ (Hata Payı) | 10.0 | 9.49 | 8.55 | 10.53 | 0.51 |

### Analiz ve Yorumlar
- **Doğruluk:** Verilerde gürültü olmasına rağmen modelimiz 150.0 değerine çok yaklaştı. Aradaki 2.21'lik fark, yöntemin ne kadar iyi çalıştığını gösteriyor.
- **Hassasiyet:** Parlaklık tahmini, hata payı tahminine göre daha dar bir aralıkta çıktı. Bunun sebebi ortalamayı tahmin etmenin varyansı tahmin etmekten istatistiksel olarak daha kesin sonuç vermesi.
- **Korelasyon:** Corner Plot grafiğindeki elips dik duruyor. Bu da parlaklık tahmini ile gözlem hatasının birbirinden bağımsız olduğunu, yani aralarında bir bağlantı olmadığını gösteriyor.

### Kurulum
Kodun çalışması için şu kütüphaneler lazım:
`numpy matplotlib emcee corner`

Dosyayı çalıştırmak için:
`odev4.py`