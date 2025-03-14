import streamlit as st

st.title("🎈 Selamat Datang di Pangan Tycoon")
st.write(
    "Let's play the game, try to make new innovation"
)
#Data bahan baku (nama, kandungan gizi, biaya, tingkat inovasi)
bahan_baku = {
    "Kacang Hijau": {"protein": 8, "serat": 7, "biaya": 5, "inovasi": 6},
    "ubi ungu": {"protein": 4, "serat": 8, "biaya": 4, "inovasi": 7},
    "keju": {"protein": 9, "serat": 2, "biaya": 8, "inovasi": 5},
    "Rumput Laut": {"protein": 6,"serat": 9, "biaya": 6, "inovasi": 8}
}
