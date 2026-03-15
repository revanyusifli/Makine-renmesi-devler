# Laboratuvar Çözüm Raporu

## [cite_start]1. Bölüm: Viterbi El Hesaplaması [cite: 3]
[cite_start]"EV" kelimesi için gözlem dizimiz: `[High, Low]` [cite: 17]



### Adım 1: Başlangıç (t=1, Gözlem: High)
* [cite_start]**e durumu:** $P(e) \times P(High|e) = 1.0 \times 0.7 = 0.7$ [cite: 15, 18]
* [cite_start]**v durumu:** $P(v) \times P(High|v) = 0.0 \times 0.1 = 0.0$ [cite: 16, 18]

### Adım 2: Geçiş (t=2, Gözlem: Low)
* [cite_start]**e durumuna geçiş:** $\max(0.7 \times 0.6 \times 0.3, 0 \times 0.2 \times 0.3) = 0.126$ [cite: 12, 13, 15]
* [cite_start]**v durumuna geçiş:** $\max(0.7 \times 0.4 \times 0.9, 0 \times 0.8 \times 0.9) = 0.252$ [cite: 12, 13, 16]

[cite_start]**Sonuç:** $0.252 > 0.126$ olduğu için en olası fonem dizisi **"e-v"** olarak hesaplanmıştır. [cite: 17]

## [cite_start]3. Bölüm: Analiz ve Yorumlama [cite: 36]

**1. [cite_start]Ses verisindeki gürültü emisyon olasılıklarını nasıl etkiler? [cite: 38]**
Aslında olay tamamen sinyalin temizliğiyle alakalı. Ortamda gürültü olduğunda, o anki fonemin (mesela "e" sesinin) karakteristik frekansı gürültüyle karışıyor. Bu da HMM modelindeki **Emisyon Olasılıklarını ($B$ matrisi)** "bulanıklaştırıyor". Yani model, o sesin "e" mi yoksa başka bir şey mi olduğuna dair net bir ayrım yapamıyor; olasılıklar birbirine yaklaşıyor. Bu belirsizlik arttığında da sistemin hata yapma payı doğal olarak fırlıyor.

**2. [cite_start]Neden Viterbi yerine Derin Öğrenme tercih ediliyor? [cite: 39]**
Viterbi ve klasik HMM yapısı, bu tip küçük ödevlerde çok güzel çalışıyor ama iş binlerce kelimeye, farklı şivelere veya arka plan gürültülerine gelince tıkanıyor. Her kelimeyi ayrı ayrı modellemek ve her olasılığı hesaplamak inanılmaz bir işlem yükü demek. **Derin Öğrenme (özellikle RNN, Transformer gibi yapılar)**, verideki karmaşık desenleri ve sesin zaman içindeki değişimini çok daha iyi kavrıyor. Üstelik elle kural yazmak yerine, devasa verilerden kendi kendine özellik çıkarabildiği için günümüzdeki modern asistanların kalbi haline geldi.