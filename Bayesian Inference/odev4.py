import numpy as np
import matplotlib.pyplot as plt
import emcee
import corner

# --- 1. VERİLERİ HAZIRLAMA ---

# Hocanın ödevde verdiği gerçek değerleri giriyoruz
true_mu = 150.0      # Galaksinin gerçek parlaklığı
true_sigma = 10.0    # Gözlem sırasındaki hata/gürültü payı
n_obs = 50           # Yapılan ölçüm sayısı

# Rastgele veri üretiyoruz, seed(42) sayesinde her çalıştırdığımızda aynı sonuçlar çıkacak
np.random.seed(42)   
data = true_mu + true_sigma * np.random.randn(n_obs) 

# Gözlem verilerini hızlıca bir histogramla kontrol ediyoruz
plt.figure(figsize=(8, 4))
plt.hist(data, bins=12, color='skyblue', edgecolor='black', alpha=0.7)
plt.axvline(true_mu, color='red', linestyle='--', label=f'Gerçek Değer ({true_mu})')
plt.title("Galaksi Parlaklık Ölçümleri")
plt.xlabel("Parlaklık")
plt.ylabel("Gözlem Sayısı")
plt.legend()
plt.show()

# --- 2. BAYESYEN OLASILIK FONKSİYONLARI ---

# Likelihood: Verilerin, tahmin ettiğimiz mu ve sigma değerlerine ne kadar uyduğuna bakıyor
def log_likelihood(theta, data):
    mu, sigma = theta
    if sigma <= 0: # Negatif hata payı fiziksel olarak imkansız
        return -np.inf
    # Ödevdeki matematiksel formülün koda dökülmüş hali
    return -0.5 * np.sum(((data - mu) / sigma)**2 + np.log(2 * np.pi * sigma**2))

# Prior: Parametreler için mantıklı sınırlar çiziyoruz
def log_prior(theta):
    mu, sigma = theta
    # Parlaklık 0-300, hata payı da 0-50 arası olsun diyoruz
    if 0 < mu < 300 and 0 < sigma < 50:
        return 0.0
    return -np.inf

# Posterior: Prior ve Likelihood'u birleştirip asıl olasılık fonksiyonunu elde ediyoruz
def log_probability(theta, data):
    lp = log_prior(theta)
    if not np.isfinite(lp):
        return -np.inf
    return lp + log_likelihood(theta, data)

# --- 3. MCMC SİMÜLASYONU (YÜRÜTÜCÜLER) ---

# Başlangıç tahminlerimizi yapıyoruz (Gerçek değerlere yakın ama tam üstünde değil)
initial = [140, 5]
n_walkers = 32
ndim = 2

# Yürütücüleri başlangıç noktasının etrafına biraz rastgele dağıtıyoruz
pos = initial + 1e-4 * np.random.randn(n_walkers, ndim)

# Sampler'ı kurup 2000 adım koşturuyoruz
sampler = emcee.EnsembleSampler(n_walkers, ndim, log_probability, args=(data,))
print("MCMC simülasyonu başlıyor...")
sampler.run_mcmc(pos, 2000, progress=True)

# İlk 500 adımı 'ısınma' (burn-in) olarak atıp temiz verileri topluyoruz
flat_samples = sampler.get_chain(discard=500, thin=15, flat=True)
print("Simülasyon bitti!")

# --- 4. SONUÇLARIN GÖRSELLEŞTİRİLMESİ ---

# Corner plot ile tahminlerimizi ve aralarındaki ilişkiyi görüyoruz
fig = corner.corner(
    flat_samples, 
    labels=["$\mu$ (Parlaklık)", "$\sigma$ (Hata)"],
    truths=[true_mu, true_sigma]
)
plt.show()

# Sonuçları ekrana yazdırıp tablodaki değerleri buluyoruz
for i, name in enumerate(["mu", "sigma"]):
    mcmc = np.percentile(flat_samples[:, i], [16, 50, 84])
    q = np.diff(mcmc)
    print(f"{name} tahmini: {mcmc[1]:.2f} (-{q[0]:.2f}, +{q[1]:.2f})")