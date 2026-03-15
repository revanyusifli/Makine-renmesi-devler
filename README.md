# HMM ile Kelime Tanıma Sistemi (Ödev 1)

Bu depo, Ankara Üniversitesi Makine Öğrenmesi dersi (YZM212) için hazırladığım ilk laboratuvar çalışmasını içeriyor. Projede, Gizli Markov Modelleri (HMM) kullanarak "EV" ve "OKUL" kelimelerini birbirinden ayıran basit bir simülasyon yaptım. 

## Neler Yaptım?
* **Teorik Hesaplama:** Viterbi algoritmasını kullanarak "EV" kelimesi için en mantıklı fonem dizisini elle hesapladım.
* **Python Uygulaması:** `numpy` kullanarak Forward algoritmasını kodladım.Bu sayede sisteme gelen yeni ses verilerinin hangi kelimeye (EV mi OKUL mu) ait olduğunu olasılık puanlarına bakarak bulabiliyoruz.

## Proje Yapısı 
* `src/recognizer.py`: Yazdığım Python kodu.
* `report/cozum_anahtari.md`: El hesaplamalarım ve analiz sorularına verdiğim cevaplar.
* `requirements.txt`: Çalıştırmak için gereken kütüphane (numpy).

---
