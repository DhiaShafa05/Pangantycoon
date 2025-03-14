import streamlit as st

st.title("🎈 Selamat Datang di Pangan Tycoon")
st.write(
    "Let's play the game, try to make new innovation"
)
# Data bahan baku dengan keterangan gizi dan kalori
bahan_baku = {
    "Kacang Hijau": {"protein": 8, "serat": 7, "karbohidrat": 17, "lemak": 1, "vitamin": 8, "kalori": 150, "biaya": 5, "inovasi": 6, "keamanan": 8},
    "Ubi Ungu": {"protein": 4, "serat": 8, "karbohidrat": 21, "lemak": 0.5, "vitamin": 9, "kalori": 120, "biaya": 4, "inovasi": 7, "keamanan": 9},
    "Keju": {"protein": 9, "serat": 2, "karbohidrat": 2, "lemak": 9, "vitamin": 4, "kalori": 200, "biaya": 8, "inovasi": 5, "keamanan": 7},
    "Rumput Laut": {"protein": 6, "serat": 9, "karbohidrat": 12, "lemak": 1, "vitamin": 10, "kalori": 50, "biaya": 6, "inovasi": 8, "keamanan": 9},
    "Tempe": {"protein": 10, "serat": 8, "karbohidrat": 14, "lemak": 5, "vitamin": 7, "kalori": 160, "biaya": 5, "inovasi": 9, "keamanan": 10},
    "Bayam": {"protein": 3, "serat": 6, "karbohidrat": 4, "lemak": 0.5, "vitamin": 10, "kalori": 40, "biaya": 3, "inovasi": 7, "keamanan": 9},
    "Tahu": {"protein": 8, "serat": 5, "karbohidrat": 2, "lemak": 4, "vitamin": 6, "kalori": 100, "biaya": 4, "inovasi": 6, "keamanan": 8},
    "Jagung": {"protein": 5, "serat": 5, "karbohidrat": 19, "lemak": 1, "vitamin": 6, "kalori": 130, "biaya": 4, "inovasi": 7, "keamanan": 9},
    "Alpukat": {"protein": 2, "serat": 7, "karbohidrat": 9, "lemak": 15, "vitamin": 9, "kalori": 200, "biaya": 7, "inovasi": 8, "keamanan": 9},
    "Telur": {"protein": 13, "serat": 0, "karbohidrat": 1, "lemak": 11, "vitamin": 5, "kalori": 155, "biaya": 6, "inovasi": 6, "keamanan": 9}
}

# Data metode pengolahan
metode_pengolahan = {
    "Panggang": {"rasa": 8, "inovasi": 6, "biaya": 3},
    "Fermentasi": {"rasa": 7, "inovasi": 9, "biaya": 4},
    "Goreng": {"rasa": 9, "inovasi": 4, "biaya": 2},
    "Kukus": {"rasa": 6, "inovasi": 7, "biaya": 2},
    "Dehidrasi": {"rasa": 5, "inovasi": 8, "biaya": 3}
}

# Judul aplikasi
st.title("🍽 Game Inovasi Produk Pangan - Mix Bahan dengan Info Gizi")

# Pilih dua bahan baku
bahan1 = st.selectbox("Pilih Bahan Baku 1:", list(bahan_baku.keys()))
bahan2 = st.selectbox("Pilih Bahan Baku 2:", list(bahan_baku.keys()))

# Pilih metode pengolahan
metode = st.selectbox("Pilih Metode Pengolahan:", list(metode_pengolahan.keys()))

# Masukkan harga jual
harga_jual = st.number_input("Masukkan Harga Jual (dalam K):", min_value=0, step=1)

# Tombol untuk menghitung hasil
if st.button("🔍 Lihat Hasil Inovasi"):
    if bahan1 == bahan2:
        st.warning("⚠ Pilih dua bahan yang berbeda untuk membuat inovasi!")
    else:
        data_bahan1 = bahan_baku[bahan1]
        data_bahan2 = bahan_baku[bahan2]
        data_metode = metode_pengolahan[metode]

        # Menggabungkan kualitas bahan
        skor_gizi = (data_bahan1["protein"] + data_bahan1["serat"] + data_bahan2["protein"] + data_bahan2["serat"]) / 4
        skor_rasa = data_metode["rasa"]
        skor_inovasi = (data_bahan1["inovasi"] + data_bahan2["inovasi"] + data_metode["inovasi"]) / 3
        skor_keamanan = min(data_bahan1["keamanan"], data_bahan2["keamanan"])
        biaya_produksi = data_bahan1["biaya"] + data_bahan2["biaya"] + data_metode["biaya"]

        # Menghitung total gizi dan kalori
        total_karbohidrat = (data_bahan1["karbohidrat"] + data_bahan2["karbohidrat"]) / 2
        total_lemak = (data_bahan1["lemak"] + data_bahan2["lemak"]) / 2
        total_vitamin = (data_bahan1["vitamin"] + data_bahan2["vitamin"]) / 2
        total_kalori = data_bahan1["kalori"] + data_bahan2["kalori"]

        keuntungan = harga_jual - biaya_produksi

        # Menampilkan hasil
        st.subheader("🔍 Hasil Inovasi Produk Panganmu:")
        st.write(f"*Campuran Bahan:* {bahan1} + {bahan2}")
        st.write(f"*Metode Pengolahan:* {metode}")
        st.write(f"*Skor Gizi:* {skor_gizi:.1f}/10")
        st.write(f"*Skor Rasa:* {skor_rasa}/10")
        st.write(f"*Skor Inovasi:* {skor_inovasi:.1f}/10")
        st.write(f"*Skor Keamanan:* {skor_keamanan}/10")
        st.write(f"*Biaya Produksi:* Rp{biaya_produksi}K")
        st.write(f"*Harga Jual:* Rp{harga_jual}K")
        st.write(f"*Keuntungan:* Rp{keuntungan}K")

        # Menampilkan info gizi
        st.subheader("📊 Informasi Gizi:")
        st.write(f"*Karbohidrat:* {total_karbohidrat}g")
        st.write(f"*Lemak:* {total_lemak}g")
        st.write(f"*Vitamin:* {total_vitamin}/10")
        st.write(f"*Kalori:* {total_kalori} kcal")

        # Evaluasi produk
        if skor_gizi > 7 and skor_rasa > 7 and skor_inovasi > 7 and skor_keamanan > 8 and keuntungan > 5:
            st.success("🎉 Produk campuranmu luar biasa! Potensial jadi tren baru!")
        elif skor_gizi > 5 and skor_rasa > 5 and skor_inovasi > 5 and skor_keamanan > 6 and keuntungan > 2:
            st.info("👍 Kombinasi ini cukup baik, tapi bisa lebih inovatif!")
        else:
            st.warning("🤔 Campuran ini kurang menarik, coba kombinasi yang lain.")


