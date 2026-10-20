import math

# Fungsi menghitung jarak terdekat antar koordinat lintang dan bujur di permukaan bumi (Haversine)
def calculate_geodetic_distance(lat1, lon1, lat2, lon2):
    R = 6371.0  # Radius rata-rata bumi dalam kilometer
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)
    
    a = math.sin(dlat / 2)**2 + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    
    return R * c

# Koordinat Pusat Fasilitas Utama (Contoh: Titik Kota / Rumah Sakit)
central_facility = (-3.8004, 102.2655)

# Daftar Koordinat Insiden / Lokasi Aset di Lapangan
field_assets = [
    {"name": "Titik Infrastruktur A", "lat": -3.7925, "lon": 102.2712},
    {"name": "Titik Infrastruktur B", "lat": -3.8112, "lon": 102.2501},
    {"name": "Titik Infrastruktur C", "lat": -3.7850, "lon": 102.2800}
]

print("=== ANALISIS SPASIAL JARAK GIS ===")
for asset in field_assets:
    distance = calculate_geodetic_distance(
        central_facility[0], central_facility[1], 
        asset["lat"], asset["lon"]
    )
    print(f"Jarak dari Pusat ke {asset['name']}: {distance:.2f} km")