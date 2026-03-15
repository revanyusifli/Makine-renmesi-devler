# HMM ile Kelime Tanıma Sistemi (Ödev 1)

[cite_start]Bu depo, Ankara Üniversitesi Makine Öğrenmesi dersi (YZM212) için hazırladığım ilk laboratuvar çalışmasını içeriyor. [cite: 1] [cite_start]Projede, Gizli Markov Modelleri (HMM) kullanarak "EV" ve "OKUL" kelimelerini birbirinden ayıran basit bir simülasyon yaptım. [cite: 2]

## Neler Yaptım?
* [cite_start]**Teorik Hesaplama:** Viterbi algoritmasını kullanarak "EV" kelimesi için en mantıklı fonem dizisini elle hesapladım. [cite: 3, 17]
* **Python Uygulaması:** `numpy` kullanarak Forward algoritmasını kodladım. [cite_start]Bu sayede sisteme gelen yeni ses verilerinin hangi kelimeye (EV mi OKUL mu) ait olduğunu olasılık puanlarına bakarak bulabiliyoruz. [cite: 19, 26]

## [cite_start]Proje Yapısı [cite: 44-53]
* `src/recognizer.py`: Yazdığım Python kodu.
* `report/cozum_anahtari.md`: El hesaplamalarım ve analiz sorularına verdiğim cevaplar.
* `requirements.txt`: Çalıştırmak için gereken kütüphane (numpy).

---
[cite_start]**Teslim Tarihi:** 08.03.2026 [cite: 55]