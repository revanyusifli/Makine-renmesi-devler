import numpy as np

class HMMRecognizer:
    def __init__(self, start_p, trans_p, emiss_p):
        self.start_p = start_p
        self.trans_p = trans_p
        self.emiss_p = emiss_p

    def get_score(self, obs):
        """Forward algoritması ile kelimenin olasılığını (Log-Likelihood) hesaplar."""
        n_states = self.trans_p.shape[0]
        n_obs = len(obs)
        fwd = np.zeros((n_obs, n_states))
        
        # Başlangıç adımı
        fwd[0, :] = self.start_p * self.emiss_p[:, obs[0]]
        
        # Zaman adımları üzerinden ilerleme
        for t in range(1, n_obs):
            for s in range(n_states):
                fwd[t, s] = np.sum(fwd[t-1, :] * self.trans_p[:, s]) * self.emiss_p[s, obs[t]]
        
        # Toplam olasılığın logaritmasını döndürüyoruz
        return np.log(np.sum(fwd[-1, :]) + 1e-100)

def main():
    # PDF'teki 'EV' modeli parametreleri [cite: 11-16, 18]
    ev_model = HMMRecognizer(
        np.array([1.0, 0.0]), # Başlangıç: P(e)=1.0
        np.array([[0.6, 0.4], [0.2, 0.8]]), # Geçiş olasılıkları (A)
        np.array([[0.7, 0.3], [0.1, 0.9]])  # Emisyon olasılıkları (B)
    )

    # Örnek bir 'OKUL' modeli (Kıyaslama yapabilmek için)
    okul_model = HMMRecognizer(
        np.array([1.0, 0.0]),
        np.array([[0.5, 0.5], [0.5, 0.5]]),
        np.array([[0.4, 0.6], [0.6, 0.4]])
    )

    # Test verisi: [High, Low, Low] -> [0, 1, 1] [cite: 33]
    test_data = [0, 1, 1]
    
    score_ev = ev_model.get_score(test_data)
    score_okul = okul_model.get_score(test_data)

    print(f"EV Modeli Puanı: {score_ev:.4f}")
    print(f"OKUL Modeli Puanı: {score_okul:.4f}")
    
    # Hangi model daha yüksek puan verdiyse o kelimeyi seçiyoruz [cite: 26]
    if score_ev > score_okul:
        print("Tahmin: Gelen ses 'EV' kelimesine benziyor.")
    else:
        print("Tahmin: Gelen ses 'OKUL' kelimesine benziyor.")

if __name__ == "__main__":
    main()