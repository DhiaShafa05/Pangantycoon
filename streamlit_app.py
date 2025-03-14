import streamlit as st

st.title("🎈 Selamat Datang di Pangan Tycoon")
st.write(
    "Let's play the game, try to make new innovation"
)
# Penjelasan untuk skor
def beri_penjelasan(skor, tipe):
    if tipe == "gizi":
        if skor > 8:
            return "🔍 Kandungan gizi produkmu sangat baik dan seimbang. Cocok jadi produk sehat!"
        elif skor > 5:
            return "👍 Produkmu punya gizi cukup, tapi masih bisa ditingkatkan."
        else:
            return "⚠ Gizi produk ini kurang optimal, coba tambahkan bahan yang lebih bernutrisi."
    
    if tipe == "rasa":
        if skor > 8:
            return "😋 Rasa produk ini lezat dan bisa disukai banyak orang!"
        elif skor > 5:
            return "🙂 Rasanya cukup enak, tapi belum terlalu menonjol."
        else:
            return "😬 Rasa produk ini kurang menarik, mungkin perlu kombinasi bahan dan metode yang berbeda."

    if tipe == "inovasi":
        if skor > 8:
            return "🌟 Inovasi luar biasa! Produk ini unik dan berpotensi jadi tren baru."
        elif skor > 5:
            return "✨ Inovasi cukup baik, meski masih ada peluang kreativitas lebih."
        else:
            return "🧠 Inovasi kurang terasa, coba eksplorasi bahan dan metode baru."

    if tipe == "keamanan":
        if skor > 8:
            return "✅ Produk ini sangat aman dan layak konsumsi."
        elif skor > 5:
            return "⚠ Produk cukup aman, tapi perhatikan kebersihan dan kualitas bahan."
        else:
            return "❌ Keamanan produk ini diragukan, pastikan bahan dan proses pengolahan higienis."

    if tipe == "keuntungan":
        if skor > 5:
            return "💰 Produk ini menguntungkan! Kamu bisa mempertimbangkan produksi massal."
        elif skor > 2:
            return "📈 Ada keuntungan, tapi kecil. Coba efisiensikan biaya atau naikkan harga."
        else:
            return "📉 Produk ini belum menguntungkan, cek lagi biaya dan harga jual."

# Menampilkan hasil dengan penjelasan
st.subheader("🔍 Hasil Inovasi Produk Panganmu:")
st.write(f"*Skor Gizi:* {skor_gizi:.1f}/10 - {beri_penjelasan(skor_gizi, 'gizi')}")
st.write(f"*Skor Rasa:* {skor_rasa}/10 - {beri_penjelasan(skor_rasa, 'rasa')}")
st.write(f"*Skor Inovasi:* {skor_inovasi:.1f}/10 - {beri_penjelasan(skor_inovasi, 'inovasi')}")
st.write(f"*Skor Keamanan:* {skor_keamanan}/10 - {beri_penjelasan(skor_keamanan, 'keamanan')}")
st.write(f"*Keuntungan:* Rp{keuntungan}K - {beri_penjelasan(keuntungan, 'keuntungan')}")
