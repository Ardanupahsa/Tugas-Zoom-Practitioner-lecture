import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

data = {
    'Customer_ID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Order_Amount': [1500, 3200, 4500, 1200, 6000, 2500, 800, 5000],
    'Discount_Given': [0.05, 0.20, 0.10, 0.02, 0.25, 0.05, 0.0, 0.15],
    'Days_Overdue_History': [2, 15, 0, 1, 30, 0, 5, 20],
    'Late_Payment': [0, 1, 0, 0, 1, 0, 0, 1] # Target: 1 jika terlambat, 0 jika tepat waktu
}

df = pd.DataFrame(data)
print("--- Dataframe Transaksi Awal ---")
print(df.head(), "\n")

X = df[['Order_Amount', 'Discount_Given', 'Days_Overdue_History']]
y = df['Late_Payment']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("=== Hasil Evaluasi Model Prediksi Late Payment ===")
print(f"Akurasi Model: {accuracy_score(y_test, y_pred) * 100:.2f}%")
print("\nLaporan Klasifikasi:")
print(classification_report(y_test, y_pred, zero_division=0))