import streamlit as st

st.title("🎈 Selamat Datang di Pangan Tycoon")
st.write(
    "Let's play the game, try to make new innovation"
)
import tkinter as tk
from tkinter import messagebox
import random

# Data bahan baku
bahan_baku = {
    "Kacang Hijau": {"protein": 8, "serat": 7, "biaya": 5, "inovasi": 6, "keamanan": 8},
    "Ubi Ungu": {"protein": 4, "serat": 8, "biaya": 4, "inovasi": 7, "keamanan": 9},
    "Keju": {"protein": 9, "serat": 2, "biaya": 8, "inovasi": 5, "keamanan": 7},
    "Rumput Laut": {"protein": 6, "serat": 9, "biaya": 6, "inovasi": 8, "keamanan": 9},
    "Tempe": {"protein": 10, "serat": 8, "biaya": 5, "inovasi": 9, "keamanan": 10}
}

# Data metode pengolahan
metode_pengolahan = {
    "Panggang": {"rasa": 8, "inovasi": 6, "biaya": 3},
    "Fermentasi": {"rasa": 7, "inovasi": 9, "biaya": 4},
    "Goreng": {"rasa": 9, "inovasi": 4, "biaya": 2},
    "Kukus": {"rasa": 6, "inovasi": 7, "biaya": 2},
    "Dehidrasi": {"rasa": 5, "inovasi": 8, "biaya": 3}
}

# Fungsi untuk menghitung kualitas dan menampilkan hasil
def hitung_hasil():
    bahan = bahan_var.get()
    metode = metode_var.get()
    harga_jual = int(harga_entry.get())

    if bahan not in bahan_baku or metode not in metode_pengolahan:
        messagebox.showerror("Error", "Pilih bahan dan metode dengan benar!")
        return

    data_bahan = bahan_baku[bahan]
    data_metode = metode_pengolahan[metode]

    skor_gizi = (data_bahan["protein"] + data_bahan["serat"]) / 2
    skor_rasa = data_metode["rasa"]
    skor_inovasi = (data_bahan["inovasi"] + data_metode["inovasi"]) / 2
    skor_keamanan = data_bahan["keamanan"]
    biaya_produksi = data_bahan["biaya"] + data_metode["biaya"]

    keuntungan = harga_jual - biaya_produksi

    # Menampilkan hasil dengan messagebox
    hasil = f"""
    🔍 Hasil Inovasi Produk Panganmu 🔍
    Bahan Baku       : {bahan}
    Metode Pengolahan: {metode}
    Skor Gizi        : {skor_gizi}/10
    Skor Rasa        : {skor_rasa}/10
    Skor Inovasi     : {skor_inovasi}/10
    Skor Keamanan    : {skor_keamanan}/10
    Biaya Produksi   : Rp{biaya_produksi}K
    Harga Jual       : Rp{harga_jual}K
    Keuntungan       : Rp{keuntungan}K
    """

    if skor_gizi > 7 and skor_rasa > 7 and skor_inovasi > 7 and skor_keamanan > 8 and keuntungan > 5:
        hasil += "\n🎉 Produkmu luar biasa! Ini bisa jadi tren pangan baru!"
    elif skor_gizi > 5 and skor_rasa > 5 and skor_inovasi > 5 and skor_keamanan > 6 and keuntungan > 2:
        hasil += "\n👍 Produkmu cukup baik, tapi masih bisa dikembangkan!"
    else:
        hasil += "\n🤔 Produkmu kurang menarik, coba eksplorasi kombinasi yang lain."

    messagebox.showinfo("Hasil Produk", hasil)

# Membuat jendela utama
root = tk.Tk()
root.title("Game Inovasi Produk Pangan")
root.geometry("400x300")

# Label dan dropdown bahan baku
tk.Label(root, text="Pilih Bahan Baku:").pack(pady=5)
bahan_var = tk.StringVar(root)
bahan_var.set("Pilih Bahan")
bahan_menu = tk.OptionMenu(root, bahan_var, *bahan_baku.keys())
bahan_menu.pack(pady=5)

# Label dan dropdown metode pengolahan
tk.Label(root, text="Pilih Metode Pengolahan:").pack(pady=5)
metode_var = tk.StringVar(root)
metode_var.set("Pilih Metode")
metode_menu = tk.OptionMenu(root, metode_var, *metode_pengolahan.keys())
metode_menu.pack(pady=5)

# Input harga jual
tk.Label(root, text="Masukkan Harga Jual (dalam K):").pack(pady=5)
harga_entry = tk.Entry(root)
harga_entry.pack(pady=5)

# Tombol hitung
hitung_button = tk.Button(root, text="Hitung Hasil", command=hitung_hasil)
hitung_button.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()
