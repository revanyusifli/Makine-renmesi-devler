# MLE ile Akıllı Şehir Trafik Planlaması

Bu proje, şehir trafiğinin yoğunluğunu modellemek amacıyla Poisson Dağılımı ve Maksimum Olabilirlik Tahmini (Maximum Likelihood Estimation - MLE) yöntemlerinin kullanımını içermektedir.

## Problem Tanımı
Bir belediyenin ulaşım departmanında, caddelerdeki araç trafiğini optimize etmek için veriye dayalı bir modelleme yapılması hedeflenmektedir. Belirli bir caddeden dakikada geçen araç sayılarının Poisson dağılımına uyduğu varsayılmış ve elimizdeki örneklem verileri üzerinden en uygun yoğunluk parametresinin ($\lambda$) bulunması amaçlanmıştır.

## Veri Seti
Analiz sürecinde kullanılan, birer dakikalık aralıklarla toplanan araç geçiş sayıları:
`[12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15]`

## Yöntem
Projede iki aşamalı bir çözüm yolu izlenmiştir:
1. **Analitik Yaklaşım:** Poisson olasılık fonksiyonu kullanılarak Likelihood ve Log-Likelihood fonksiyonları türetilmiştir. Türev alma yöntemiyle teorik olarak en iyi tahminin verilerin ortalaması olduğu kanıtlanmıştır.
2. **Sayısal Yaklaşım:** Python dili ve `scipy.optimize` kütüphanesi yardımıyla negatif log-likelihood fonksiyonu minimize edilerek sayısal sonuç elde edilmiştir.

## Sonuçlar
Yapılan hesaplamalar sonucunda elde edilen değerler:
* **Sayısal Tahmin (MLE lambda):** 12.1429
* **Analitik Tahmin (Aritmetik Ortalama):** 12.1429

Her iki yöntemin de tutarlı sonuçlar vermesi, kurulan matematiksel modelin doğru olduğunu göstermektedir.

## Yorum ve Tartışma
* **Model Başarısı:** Görselleştirme aşamasında çizilen Poisson PMF grafiği, gerçek veri histogramı ile örtüşmektedir. Bu durum, modelin trafik akışını temsil etme yeteneğinin yüksek olduğunu gösterir.
* **Aykırı Değer (Outlier) Analizi:** Veri setine "200" gibi yüksek bir değerin eklenmesi durumunda, MLE yöntemi (ortalamaya dayalı olduğu için) bu sapmadan ciddi şekilde etkilenmektedir. Bu durum belediyenin trafiği olduğundan çok daha yoğun sanmasına ve hatalı altyapı yatırımları (gereksiz yol genişletme vb.) yapmasına neden olabilir. Bu nedenle modelleme öncesi veri temizliği hayati önem taşır.

