import streamlit as st

st.title("🎈 Selamat Datang di Pangan Tycoon")
st.write(
    "Let's play the game, try to make new innovation"
)
import random

# Data bahan baku (nama, kandungan gizi, biaya, tingkat inovasi)
bahan_baku = {
    "Kacang Hijau": {"protein": 8, "serat": 7, "biaya": 5, "inovasi": 6},
    "Ubi Ungu": {"protein": 4, "serat": 8, "biaya": 4, "inovasi": 7},
    "Keju": {"protein": 9, "serat": 2, "biaya": 8, "inovasi": 5},
    "Rumput Laut": {"protein": 6, "serat": 9, "biaya": 6, "inovasi": 8}
}

# Data metode pengolahan (nama, tingkat rasa, inovasi)
metode_pengolahan = {
    "Panggang": {"rasa": 8, "inovasi": 6},
    "Fermentasi": {"rasa": 7, "inovasi": 9},
    "Goreng": {"rasa": 9, "inovasi": 4},
    "Kukus": {"rasa": 6, "inovasi": 7}
}

# Memperkenalkan game
print("🎉 Selamat Datang di Game Inovasi Produk Pangan! 🎉")
print("Tugasmu adalah membuat produk pangan inovatif dengan bahan dan metode terbaik.")

# Pemilihan bahan baku
print("\nPilih bahan baku:")
for idx, bahan in enumerate(bahan_baku, 1):
    print(f"{idx}. {bahan}")

pilihan_bahan = int(input("Masukkan nomor bahan baku: ")) - 1
bahan_terpilih = list(bahan_baku.keys())[pilihan_bahan]

# Pemilihan metode pengolahan
print("\nPilih metode pengolahan:")
for idx, metode in enumerate(metode_pengolahan, 1):
    print(f"{idx}. {metode}")

pilihan_metode = int(input("Masukkan nomor metode pengolahan: ")) - 1
metode_terpilih = list(metode_pengolahan.keys())[pilihan_metode]

# Menghitung skor produk
bahan = bahan_baku[bahan_terpilih]
metode = metode_pengolahan[metode_terpilih]

skor_gizi = (bahan["protein"] + bahan["serat"]) / 2
skor_rasa = metode["rasa"]
skor_inovasi = (bahan["inovasi"] + metode["inovasi"]) / 2
biaya_produksi = bahan["biaya"] + random.randint(1, 3)

# Memberikan hasil dan feedback
print("\n🔍 Hasil Inovasi Produk Panganmu 🔍")
print(f"Bahan Baku: {bahan_terpilih}")
print(f"Metode Pengolahan: {metode_terpilih}")
print(f"Skor Gizi: {skor_gizi}/10")
print(f"Skor Rasa: {skor_rasa}/10")
print(f"Skor Inovasi: {skor_inovasi}/10")
print(f"Biaya Produksi: Rp{biaya_produksi}K")

# Penilaian akhir
if skor_gizi > 7 and skor_rasa > 7 and skor_inovasi > 7:
    print("\n🎉 Produkmu luar biasa! Ini bisa jadi tren pangan baru!")
elif skor_gizi > 5 and skor_rasa > 5 and skor_inovasi > 5:
    print("\n👍 Produkmu cukup baik, tapi masih bisa dikembangkan!")
else:
    print("\n🤔 Produkmu kurang menarik, coba eksplorasi kombinasi yang lain.")

print("\nTerima kasih sudah bermain! 🍽")
