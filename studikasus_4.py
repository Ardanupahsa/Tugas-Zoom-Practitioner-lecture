import pandas as pd
from sklearn.cluster import KMeans

# Simulasi data perilaku pelanggan/pasien
data = {
    'Frekuensi_Kunjungan': [2, 12, 1, 15, 3, 14, 2, 13, 4, 11],
    'Total_Pengeluaran_Rata_Rata': [150000, 1500000, 100000, 1600000, 200000, 1450000, 180000, 1350000, 250000, 1250000]
}

df = pd.DataFrame(data)
print("--- Data Mentah Pengguna ---")
print(df.head(), "\n")

# Inisialisasi Model K-Means untuk membagi data menjadi 2 klaster (Reguler dan VIP)
kmeans_model = KMeans(n_clusters=2, random_state=42, n_init=10)

# Melakukan proses training unsupervised clustering
df['Cluster_Segment'] = kmeans_model.fit_predict(df[['Frekuensi_Kunjungan', 'Total_Pengeluaran_Rata_Rata']])

# Pelabelan klaster agar mudah dibaca
df['Kategori_Pelanggan'] = df['Cluster_Segment'].apply(lambda x: 'Segmen VIP / Premium' if x == 1 else 'Segmen Reguler')

print("--- Hasil Segmentasi Machine Learning (K-Means) ---")
print(df[['Frekuensi_Kunjungan', 'Total_Pengeluaran_Rata_Rata', 'Kategori_Pelanggan']])
print("\nTitik Pusat Klaster (Centroids):")
print(kmeans_model.cluster_centers_)