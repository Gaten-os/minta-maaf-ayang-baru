
import streamlit as st

# Pengaturan halaman web
st.set_page_config(page_title="Maafin Hendi Ya Sayang", page_icon="🥺", layout="centered")

# Styling CSS biar tampilannya cantik
st.markdown(
    """
    <style>
    .stApp {
        background-color: #fff0f3;
    }
    h1 {
        color: #ff4d6d;
        text-align: center;
    }
    p {
        color: #590d22;
        font-size: 18px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Konten Utama Website dengan Namamu
st.markdown("# 🥺 Maafin Hendi Ya, Sayang... 🥺")
st.write("")
st.markdown(
    "<p>Aku tahu Hendi punya salah dan bikin kamu kesal. Hendi bener-bener minta maaf ya, Sayang. Jangan ngambek sama Hendi lagi dong... 😭❤️</p>",
    unsafe_allow_html=True,
)

st.write("")
st.write("")

# Tombol Interaktif Pilihan
col1, col2 = st.columns(2)

with col1:
    if st.button("Iya, dimaafin Hendi! ❤️", use_container_width=True):
        st.balloons()
        st.success(
            "Yey! Makasih ya sayangku cintaku udah maafin Hendi! Janji gak bakal diulangin lagi 🥰"
        )

with col2:
    if st.button("Masih ngambek sama Hendi 😤", use_container_width=True):
        st.error(
            "Duh... jangan ngambek dong sama Hendi, pencet tombol sebelah kiri aja ya plis? 🥺"
        )
