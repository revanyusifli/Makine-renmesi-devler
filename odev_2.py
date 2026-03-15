import numpy as np
import scipy.optimize as opt
import matplotlib.pyplot as plt
from scipy.stats import poisson

# --- Bölüm 2: Sayısal Çözüm ---

#  Trafik verilerini giriyoruz

traffic_data = np.array([12, 15, 10, 8, 14, 11, 13, 16, 9, 12, 11, 14, 10, 15])

def negative_log_likelihood(lam, data):

    """
    Poisson için Negatif Log-Likelihood hesabı.
    Ipucuna göre log(k!) kısmını sabit olduğu için çıkardık.

    """

    n = len(data)

    # Formül: -(-n * lambda + log(lambda) * toplam_veri)

    nll = -(-n * lam + np.log(lam) * np.sum(data))

    return nll

# Başlangıç tahmini ve optimizasyon

initial_guess = 1.0

result = opt.minimize(negative_log_likelihood, initial_guess, args=(traffic_data,), bounds=[(0.001, None)])

mle_lambda = result.x[0]

# Sonuçları yazdırıyoruz (Analitik ve Sayısal karşılaştırması için)

print(f"Sayısal Tahmin (MLE lambda): {mle_lambda:.4f}")

print(f"Analitik Tahmin (Ortalama): {np.mean(traffic_data):.4f}")

# --- Bölüm 3: Grafik Çizimi ---

plt.figure(figsize=(10, 6))


# Gerçek verinin histogramı

plt.hist(traffic_data, bins=range(min(traffic_data), max(traffic_data) + 2),

         density=True, alpha=0.5, color='gray', label='Gerçek Veri Histogramı', align='left')

# Poisson PMF grafiği (Modelin uyumu için)

x = np.arange(0, 25)

plt.plot(x, poisson.pmf(x, mle_lambda), 'bo-', label=f'Poisson Modeli (lambda={mle_lambda:.2f})')

plt.title('Trafik Verisi ve Poisson Modeli Karşılaştırması')

plt.xlabel('Araç Sayısı')

plt.ylabel('Olasılık')

plt.legend()

plt.show()