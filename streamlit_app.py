import streamlit as st

st.title("🎈 Selamat Datang di Pangan Tycoon")
st.write(
    "Let's play the game, try to make new innovation"
)
# Data bahan baku dengan info gizi lengkap
bahan_baku = {
    "Kacang Hijau": {"protein": 8, "karbohidrat": 17, "lemak": 1, "vitamin": 8, "mineral": 7, "kalori": 150, "biaya": 5, "inovasi": 6, "keamanan": 8},
    "Ubi Ungu": {"protein": 4, "karbohidrat": 21, "lemak": 0.5, "vitamin": 9, "mineral": 8, "kalori": 120, "biaya": 4, "inovasi": 7, "keamanan": 9},
    "Rumput Laut": {"protein": 6, "karbohidrat": 12, "lemak": 1, "vitamin": 10, "mineral": 9, "kalori": 50, "biaya": 6, "inovasi": 8, "keamanan": 9},
    "Tempe": {"protein": 10, "karbohidrat": 14, "lemak": 5, "vitamin": 7, "mineral": 8, "kalori": 160, "biaya": 5, "inovasi": 9, "keamanan": 10},
    "Bayam": {"protein": 3, "karbohidrat": 4, "lemak": 0.5, "vitamin": 10, "mineral": 10, "kalori": 40, "biaya": 3, "inovasi": 7, "keamanan": 9},
    "Alpukat": {"protein": 2, "karbohidrat": 9, "lemak": 15, "vitamin": 9, "mineral": 7, "kalori": 200, "biaya": 7, "inovasi": 8, "keamanan": 9}
}

# Data metode pengolahan yang lebih bervariasi
metode_pengolahan = {
    "Panggang": {"rasa": 8, "inovasi": 6, "biaya": 3},
    "Fermentasi": {"rasa": 7, "inovasi": 9, "biaya": 4},
    "Kukus": {"rasa": 6, "inovasi": 7, "biaya": 2},
    "Rebus": {"rasa": 5, "inovasi": 5, "biaya": 1},
    "Goreng": {"rasa": 9, "inovasi": 4, "biaya": 3},
    "Dehidrasi": {"rasa": 5, "inovasi": 8, "biaya": 3},
    "Asap": {"rasa": 8, "inovasi": 7, "biaya": 4},
    "Sous Vide": {"rasa": 9, "inovasi": 10, "biaya": 6},
    "Grill": {"rasa": 8, "inovasi": 6, "biaya": 3},
    "Blansir": {"rasa": 6, "inovasi": 5, "biaya": 2}
}

# Fungsi memberikan saran dan penjelasan
def beri_saran(skor, tipe):
    if tipe == "gizi":
        if skor > 8:
            return "✅ Gizi sangat baik dan seimbang."
        elif skor > 5:
            return "👍 Gizi cukup baik, tapi masih bisa ditingkatkan."
        else:
            return "⚠ Gizi kurang baik, coba tambah bahan yang lebih bernutrisi."
    if tipe == "rasa":
        return "😋 Rasa enak dan disukai!" if skor > 7 else "🙂 Rasa cukup, bisa lebih baik."
    if tipe == "inovasi":
        return "🌟 Inovasi kreatif dan unik!" if skor > 7 else "✨ Inovasi standar, coba eksplorasi lebih."
    if tipe == "keamanan":
        return "✅ Produk aman dikonsumsi." if skor > 7 else "⚠ Perlu perhatian pada keamanan dan kebersihan."
    if tipe == "keuntungan":
        return "💰 Menguntungkan!" if skor > 5 else "📉 Keuntungan minim, cek biaya dan harga jual."

# Judul aplikasi
st.title("🍽 Game Inovasi Produk Pangan")

# Pilihan bahan dan metode
bahan1 = st.selectbox("Pilih Bahan Baku 1:", list(bahan_baku.keys()))
bahan2 = st.selectbox("Pilih Bahan Baku 2:", list(bahan_baku.keys()))
metode = st.selectbox("Pilih Metode Pengolahan:", list(metode_pengolahan.keys()))
harga_jual = st.number_input("Masukkan Harga Jual (dalam K):", min_value=0, step=1)

if st.button("🔍 Lihat Hasil Inovasi"):
    if bahan1 == bahan2:
        st.warning("⚠ Pilih dua bahan yang berbeda!")
    else:
        data1 = bahan_baku[bahan1]
        data2 = bahan_baku[bahan2]
        metode_data = metode_pengolahan[metode]

        # Perhitungan skor dan info gizi
        skor_gizi = (data1["protein"] + data2["protein"] + data1["vitamin"] + data2["vitamin"] + data1["mineral"] + data2["mineral"]) / 6
        skor_rasa = metode_data["rasa"]
        skor_inovasi = (data1["inovasi"] + data2["inovasi"] + metode_data["inovasi"]) / 3
        skor_keamanan = min(data1["keamanan"], data2["keamanan"])
        biaya_produksi = data1["biaya"] + data2["biaya"] + metode_data["biaya"]

        total_kalori = data1["kalori"] + data2["kalori"]
        total_protein = data1["protein"] + data2["protein"]
        total_karbohidrat = data1["karbohidrat"] + data2["karbohidrat"]
        total_vitamin = (data1["vitamin"] + data2["vitamin"]) / 2
        total_mineral = (data1["mineral"] + data2["mineral"]) / 2

        keuntungan = harga_jual - biaya_produksi

        # Menampilkan hasil
        st.subheader("🔍 Hasil Inovasi Produk Pangan:")
        st.write(f"*Gizi:* {skor_gizi:.1f}/10 - {beri_saran(skor_gizi, 'gizi')}")
        st.write(f"*Rasa:* {skor_rasa}/10 - {beri_saran(skor_rasa, 'rasa')}")
        st.write(f"*Inovasi:* {skor_inovasi:.1f}/10 - {beri_saran(skor_inovasi, 'inovasi')}")
        st.write(f"*Keamanan:* {skor_keamanan}/10 - {beri_saran(skor_keamanan, 'keamanan')}")
        st.write(f"*Kalori Total:* {total_kalori} kcal")
        st.write(f"*Protein:* {total_protein} g")
        st.write(f"*Karbohidrat:* {total_karbohidrat} g")
        st.write(f"*Vitamin:* {total_vitamin:.1f}/10")
        st.write(f"*Mineral:* {total_mineral:.1f}/10")
        st.write(f"*Biaya Produksi:* Rp{biaya_produksi}K")
        st.write(f"*Keuntungan:* Rp{keuntungan}K - {beri_saran(keuntungan, 'keuntungan')}")

st.markdown("---")
st.caption("💡 Dibuat dengan Python dan Streamlit")
