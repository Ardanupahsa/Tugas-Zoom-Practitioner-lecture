import tkinter as tk
from tkinter import messagebox

class PresensiDosenApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Presensi Mengajar Dosen")
        self.root.geometry("450x500")
        self.root.configure(bg="#F4F6F9") # Background tenang, tingkatkan kontras

        # Header - Jelas dan Terstruktur
        tk.Label(root, text="Jadwal Mengajar Hari Ini", font=("Arial", 16, "bold"), bg="#F4F6F9", fg="#1E293B").pack(pady=15)

        # Informasi Kelas (Recognition over Recall)
        info_card = tk.Frame(root, bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=15)
        info_card.pack(fill="x", padx=20, pady=10)

        tk.Label(info_card, text="Mata Kuliah: Interaksi Manusia & Komputer", font=("Arial", 11, "bold"), bg="#FFFFFF", fg="#0F172A").pack(anchor="w")
        tk.Label(info_card, text="Ruang: Lab Komputer 2 | Waktu: 08.00 - 10.30 WIB", font=("Arial", 10), bg="#FFFFFF", fg="#475569").pack(anchor="w", pady=5)
        
        self.status_label = tk.Label(info_card, text="Status: Belum Dimulai", font=("Arial", 10, "italic"), bg="#FFFFFF", fg="#D97706")
        self.status_label.pack(anchor="w", pady=5)

        # Tombol Utama - Pre-attentive Attributes (Ukuran Besar & Warna Kontras Tinggi)
        self.btn_mulai = tk.Button(root, text="MULAI KELAS", font=("Arial", 12, "bold"), bg="#16A34A", fg="white", 
                                   activebackground="#15803D", height=2, width=25, command=self.mulai_kelas, bd=0, cursor="hand2")
        self.btn_mulai.pack(pady=15)

        self.btn_selesai = tk.Button(root, text="AKHIRI KELAS", font=("Arial", 12, "bold"), bg="#DC2626", fg="white", 
                                     activebackground="#B91C1C", height=2, width=25, command=self.akhiri_kelas, state="disabled", bd=0, cursor="hand2")
        self.btn_selesai.pack(pady=5)

    def mulai_kelas(self):
        self.status_label.config(text="Status: Perkuliahan Sedang Berlangsung", fg="#16A34A")
        self.btn_mulai.config(state="disabled", bg="#9CA3AF")
        self.btn_selesai.config(state="normal", bg="#DC2626")
        messagebox.showinfo("Presensi Berhasil", "Sesi perkuliahan resmi dimulai.")

    def akhiri_kelas(self):
        if messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin mengakhiri kelas sekarang?"):
            self.status_label.config(text="Status: Perkuliahan Selesai", fg="#2563EB")
            self.btn_selesai.config(state="disabled", bg="#9CA3AF")
            messagebox.showinfo("Kelas Selesai", "Data presensi telah disimpan ke server.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PresensiDosenApp(root)
    root.mainloop()