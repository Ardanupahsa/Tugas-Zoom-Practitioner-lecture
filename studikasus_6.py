import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, f1_score

# 1. Simulasi Tumpukan Data Citra Satelit (Image Stack Stack Features)
# Fitur Optik (Sentinel-2: Band B4, B8, NDVI) + Radar (Sentinel-1: VV, VH Backscatter)
np.random.seed(42)
num_samples = 1000

# Generating synthetic Sentinel-1 & Sentinel-2 spectral/radar values
sentinel2_ndvi = np.random.uniform(-0.2, 0.8, num_samples) # Vegetasi
sentinel1_vh = np.random.uniform(-25, -5, num_samples)    # Struktur tajuk/penetrasi radar
luas_area_ha = np.random.uniform(0.5, 50.0, num_samples)   # Ukuran luasan perubahan

X = pd.DataFrame({
    'S2_NDVI': sentinel2_ndvi,
    'S1_VH_Backscatter': sentinel1_vh,
    'Ukuran_Area_Ha': luas_area_ha
})

# Class Labels (Driver Deforestasi): 
# 0: Pertanian Skala Kecil, 1: Penebangan Terpilih, 2: Tambang Ilegal, 3: Kebakaran Hutan
y = np.random.choice([0, 1, 2, 3], size=num_samples, p=[0.5, 0.25, 0.15, 0.10])

# 2. Split Dataset Train/Test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# 3. Training Model Klasifikasi (Simulasi Klasifikasi Multi-Sensor)
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 4. Prediksi & Evaluasi Kinerja Model
y_pred = model.predict(X_test)

target_names = ['Pertanian Skala Kecil', 'Penebangan Terpilih', 'Tambang Ilegal', 'Kebakaran Hutan']

# Menghitung Overall Accuracy vs Macro F1-Score (Penting untuk ketidakseimbangan kelas)
acc = accuracy_score(y_test, y_pred)
macro_f1 = f1_score(y_test, y_pred, average='macro')

print("=== EVALUASI MODEL AI DEFORESTASI ===")
print(f"Overall Accuracy : {acc * 100:.2f}%")
print(f"Macro F1-Score   : {macro_f1 * 100:.2f}% (Indikator Keadilan Deteksi Kelas Minoritas)\n")
print("Laporan Per-Kelas:")
print(classification_report(y_test, y_pred, target_names=target_names))