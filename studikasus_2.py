import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Data Dummy untuk Simulasi Prediksi Harga Properti
data = {
    'Size_SQFT': [800, 1200, 1500, 2000, 2400, 3000, 3500, 4000],
    'Bedrooms': [1, 2, 2, 3, 4, 4, 5, 5],
    'Location_Score': [5, 7, 6, 8, 9, 10, 9, 10],
    'Price_In_Million': [500, 750, 900, 1200, 1500, 1900, 2100, 2500]
}

# Membuat DataFrame
df = pd.DataFrame(data)
print("--- Dataframe Berhasil Dimuat ---")
print(df.head(), "\n")

# Memisahkan Fitur (X) dan Target (y)
X = df[['Size_SQFT', 'Bedrooms', 'Location_Score']]
y = df['Price_In_Million']

# Membagi Data Training dan Testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Melatih Model Linear Regression
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluasi Model
y_pred = model.predict(X_test)
print("--- Hasil Evaluasi Model ---")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, y_pred):.2f}")
print(f"R2 Score (Akurasi): {r2_score(y_test, y_pred):.2f}")

# Prediksi Data Baru
new_house = [[2200, 3, 8]]
predicted_price = model.predict(new_house)
print(f"\nEstimasi Harga Rumah Baru: {predicted_price[0]:.2f} Juta")