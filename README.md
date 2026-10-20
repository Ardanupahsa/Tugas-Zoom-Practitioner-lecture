# Tugas-Zoom-Practitioner-lecture
# Studi Kasus 1: Penerapan Analisis Data dan AI di Sektor Ritel (Berdasarkan Sesi 1: Make Sense of Data with Analysis and AI)
 Latar Belakang Kasus:

PT Swalayan Sejahtera adalah jaringan supermarket nasional yang memiliki puluhan cabang. Selama satu tahun terakhir, manajemen melihat adanya peningkatan jumlah transaksi belanja online dan offline, namun total profit bersih supermarket justru mengalami penurunan sebesar 10%. Manajemen meminta tim data analis untuk mencari penyebab masalah ini dan memberikan rekomendasi aksi.

Penerapan 4 Level Analisis Data:

Descriptive Analytics (Apa yang terjadi?):

Tim menganalisis data transaksi dan menemukan bahwa penjualan kategori produk makanan segar (fresh food) meningkat 25%, namun margin profit dari kategori barang elektronik ringan/peralatan rumah tangga turun drastis.

Diagnostic Analytics (Mengapa terjadi?):

Dengan melakukan pengelompokan (grouping) data pelanggan dan inventaris, ditemukan bahwa stok barang elektronik banyak mengalami pengembalian (returns) karena kerusakan kemasan saat pengiriman, serta adanya pemberian diskon besar-besaran oleh tim pemasaran tanpa melihat biaya operasional logistik.

Predictive Analytics (Apa yang akan terjadi?):

Menggunakan algoritma machine learning (seperti Random Forest dan Logistic Regression), tim membangun model untuk memprediksi pelanggan mana yang berpotensi melakukan retur barang dalam 30 hari ke depan serta item mana yang berisiko tinggi busuk/rusak sebelum terjual.

Prescriptive Analytics (Apa rekomendasi tindakannya?):

Rekomendasi yang dihasilkan mencakup batas maksimal diskon otomatis untuk produk tertentu, penetapan standar batas retur barang, serta optimasi rute pengiriman barang elektronik agar tidak terjadi kerusakan saat perjalanan.

Peran Manusia dan Generative AI:

Generative AI digunakan untuk mempercepat pembuatan skrip pembersihan data (data preparation) dan merangkum pola tren dari ribuan data transaksi. Namun, verifikasi alasan mendasar pemberian diskon oleh staf serta keputusan akhir skema diskon tetap dilakukan oleh analisis dan pertimbangan pengambil keputusan manusia.

# Studi Kasus 2: Mitigasi Bencana Erosi dan Tanah Longsor Menggunakan HPC (Berdasarkan Sesi 2: Bridging Global Infrastructure to Address Local Challenge with HPC)
Latar Belakang Kasus:

Wilayah dataran tinggi di Kabupaten Lembah Hijau sering mengalami tanah longsor saat musim hujan deras tiba, mengancam permukiman warga dan jalur transportasi utama antarprovinsi. Pihak pemerintah daerah membutuhkan sistem peringatan dini spasial berpresisi tinggi yang dapat memprediksi pergerakan tanah dalam hitungan jam sebelum bencana terjadi.

Solusi Berbasis HPC (High Performance Computing):

Pemodelan dan Simulasi Komputasi Skala Besar:

Menggunakan fasilitas Superkomputer (High Performance Computing), peneliti menggabungkan dataset elevasi tanah beresolusi tinggi (LiDAR), data tutupan lahan, data curah hujan real-time dari sensor IoT, serta pemodelan fisik tanah.

Skala Komputasi Terapik (Exaflops/Teraflops):

Simulasi pergerakan air tanah dan stabilitas lereng yang biasanya membutuhkan waktu berhari-hari di komputer biasa dapat diselesaikan dalam waktu kurang dari 30 menit dengan pemrosesan paralel GPU/CPU di HPC.

Integrasi Komunitas dan Pengambil Keputusan (The Integrator):

Mahasiswa dan peneliti informatika bertindak sebagai integrator yang mengolah hasil komputasi rumit HPC menjadi aplikasi peta interaktif di smartphone. Aplikasi ini memberikan alur evakuasi otomatis bagi warga dan dinas penanggulangan bencana setempat secara real-time.

# Studi Kasus 3: Pengelolaan Aset Industri Fasilitas Kesehatan Menggunakan GIS (Berdasarkan Sesi 3: Career and Competition in Industrial Era with GIS)
Latar Belakang Kasus:

Sebuah jaringan rumah sakit swasta RS Medika Group mengelola 15 gedung rumah sakit dan ratusan unit klinik pratama yang tersebar di wilayah perkotaan hingga pelosok. Manajemen mengalami kesulitan dalam memantau kondisi fisik bangunan, distribusi alat medis bernilai tinggi, serta pemeliharaan berkala infrastruktur gedung.

Penerapan Sistem Informasi Geografis (GIS) dan Cloud Integrasi:

Infrastruktur Pemetaan dan Digitalisasi Aset:

Tim GIS menggunakan drone dan teknologi scanner LiDAR untuk membuat peta 3D (Digital Twin) gedung-gedung rumah sakit beserta posisi alat-alat medis utama.

Integrasi Data Spasial Real-time dan Cloud:

Menggunakan aplikasi pemetaan berbasis cloud (seperti integrasi QGIS/ArcGIS dengan database geospasial PostgreSQL/PostGIS), petugas lapangan yang melakukan pengecekan dapat memfoto kerusakan fasilitas (misalnya AC, saluran oksigen, atau atap bocor) melalui ponsel secara langsung (geotagging).

Pengambilan Keputusan Berbasis Data Spasial:

Data laporan dari ponsel petugas secara otomatis tersinkronisasi (seamless) ke dashboard pusat aset. Manajemen dapat melihat kluster fasilitas yang sering rusak dan mengalokasikan anggaran pemeliharaan (maintenance budget) serta rute teknisi secara efisien.

# Studi Kasus 4: Deteksi Transaksi Keuangan Mencurigakan dengan Machine Learning (Berdasarkan Sesi 4: Introduction to Machine Learning)
Latar Belakang Kasus:

Sebuah perusahaan Financial Technology (Fintech) PayKita ingin mencegah kejahatan penipuan (fraud) berupa pencucian uang dan penyalahgunaan akun pengguna yang frekuensinya terus meningkat seiring bertambahnya jumlah pengguna.

Alur dan Penerapan Metode Machine Learning:

Pengumpulan & Pra-pemrosesan Data (Data Preprocessing):

Sistem mengumpulkan data riwayat transaksi pengguna (nominal transaksi, waktu, lokasi IP, jenis perangkat, dan frekuensi transaksi). Data yang memiliki nilai kosong (missing values) atau terduplikasi dibersihkan terlebih dahulu.

Unsupervised Learning (Pengelompokan & Anomaly Detection):

Sistem menggunakan metode clustering (seperti K-Means) dan Anomaly Detection untuk mengenali pola transaksi abnormal yang sangat jauh berbeda dari perilaku belanja biasa pengguna (misalnya, akun yang biasa bertransaksi Rp50.000 tiba-tiba melakukan transfer berturut-turut Rp10.000.000 ke rekening luar negeri dalam waktu kurun 1 menit).

Supervised Learning (Klasifikasi Fraud vs Non-Fraud):

Berdasarkan data histori transaksi yang sudah diberi label (Fraud / Normal), algoritma klasifikasi (seperti Random Forest atau Logistic Regression) dilatih (training). Model ini bertugas memprediksi dan secara otomatis memblokir transaksi baru yang dicurigai sebagai fraud secara real-time.

Evaluasi dan Mitigasi Bias:

Model dievaluasi presisi dan akurasinya menggunakan confusion matrix agar tidak terjadi penolakan berlebihan pada transaksi sah pengguna (False Positive).

# Studi Kasus 5: Perancangan Aplikasi Presensi & Beban Mengajar Dosen (IMK & Psikologi Kognitif)

Latar Belakang & Masalah:

Universitas Nusa Harapan meluncurkan aplikasi seluler baru untuk dosen mencatat kehadiran dan melihat alokasi jam mengajar. Namun, banyak dosen senior mengeluh karena aplikasi penuh dengan angka, teks berukuran kecil, serta tombol yang membingungkan. Mereka sering salah menekan tombol "Selesai Mengajar" padahal perkuliahan baru dimulai.

Pendekatan & Solusi IMK:

1. Prinsip "You are not your user": Tim pengembang melakukan riset empiris langsung kepada kelompok dosen senior, bukan berasumsi dari kodingan pengembang.

2. Meminimalkan Extraneous Cognitive Load: Tata letak antarmuka dirapikan, menghilangkan informasi/elemen dekoratif yang tidak perlu agar beban kognitif otak berkurang.

3. Penggunaan Pre-attentive Attributes: Tombol "Mulai Kelas" diberi warna hijau kontras dan "Akhiri Kelas" diberi warna merah. Atribut warna dan ukuran ini diproses otak dalam waktu kurang dari 200 ms untuk mencegah kesalahan tekan.

4. Penerapan Recognition over Recall: Aplikasi menampilkan daftar jadwal kelas hari ini secara otomatis daripada memaksa dosen mengetik atau mengingat kode mata kuliah.

# Studi Kasus 6: Klasifikasi Penyebab Deforestasi Berbasis AI & Satelit Multi-Sensor (Integrasi Penginderaan Jauh)

Latar Belakang & Masalah:

LSM Lingkungan di Kawasan Ekosistem Leuser membutuhkan sistem peringatan dini yang tidak hanya mendeteksi hilangnya tutupan pohon, tetapi juga mampu mengidentifikasi penyebab langsung (direct driver) di wilayah yang sering tertutup awan tebal.

Pendekatan & Solusi Pembelajaran Mesin / AI:

1. Penggabungan Multi-Sensor (Sentinel-1 & Sentinel-2):
- Menggunakan citra optik (Sentinel-2) untuk kesehatan vegetasi saat cuaca cerah.
- Menggunakan citra radar (Sentinel-1) yang dapat menembus awan untuk konsistensi data mingguan.

2. Penggunaan Convolutional Neural Network (CNN): Citra dikombinasikan menjadi tumpukan multi-band (image stack) dan dimasukkan ke model deep learning CNN untuk mengklasifikasikan penyebab deforestasi secara otomatis (pertanian skala kecil, pembukaan jalan, penebangan terpilih, atau tambang).

3. Disagregasi & Penilaian Akurasi:
- Membedakan kegiatan pertanian berdasarkan ukuran luasan dan indikasi penggunaan api.
- Evaluasi model tidak hanya menggunakan overall accuracy, melainkan melihat nilai Macro F1-Score untuk memastikan kelas minoritas (seperti pertambangan ilegal atau banjir) terdeteksi secara seimbang.
