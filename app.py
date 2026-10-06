import streamlit as st

# Pengaturan halaman web
st.set_page_config(page_title="Untuk Kamu, dari Hendi", page_icon="🌸", layout="centered")

# Styling CSS: Estetik, santai, animasi bunga jatuh, & tombol ngambek yang dinamis
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ffccd5, #ffe5ec);
        overflow: hidden;
    }
    h1, h3 {
        color: #8b0000;
        text-align: center;
        font-family: 'Courier New', monospace;
    }
    p {
        color: #590d22;
        font-size: 18px;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.85);
        padding: 20px;
        border-radius: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    }
    
    /* Animasi Kelopak Bunga Jatuh */
    @keyframes fall {
        0% { transform: translateY(-10vh) translateX(0); opacity: 1; }
        100% { transform: translateY(105vh) translateX(50px); opacity: 0; }
    }
    .flower {
        position: fixed;
        top: -10vh;
        font-size: 24px;
        animation: fall linear infinite;
        z-index: 999;
    }
    </style>
    
    <!-- Elemen Bunga yang Bergerak Jatuh ke Bawah -->
    <div class="flower" style="left: 10%; animation-duration: 7s;">🌸</div>
    <div class="flower" style="left: 30%; animation-duration: 9s; animation-delay: 1s;">🌷</div>
    <div class="flower" style="left: 50%; animation-duration: 6s; animation-delay: 2s;">🌸</div>
    <div class="flower" style="left: 70%; animation-duration: 8s; animation-delay: 0.5s;">🌺</div>
    <div class="flower" style="left: 90%; animation-duration: 10s; animation-delay: 3s;">🌸</div>
    """,
    unsafe_allow_html=True,
)

# Inisialisasi alur halaman & level tombol ngambek
if 'tahap' not in st.session_state:
    st.session_state.tahap = 0
if 'tingkat_ngambek' not in st.session_state:
    st.session_state.tingkat_ngambek = 0

# --- TAHAP 0: Pembuka Santai ---
if st.session_state.tahap == 0:
    st.markdown("### Mood: 0%")
    st.progress(0)
    
    st.markdown("# Hai Kamu... 🌷")
    st.write("")
    st.markdown("<p>Lagi senggang kan? Hendi cuma mau minta waktu sebentar aja buat nunjukin sesuatu ke kamu. Dibaca sampai selesai ya.</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Buka Pesan dari Hendi 🌸", use_container_width=True):
        st.session_state.tahap = 1
        st.rerun()

# --- TAHAP 1: Pengakuan Jujur ---
elif st.session_state.tahap == 1:
    st.markdown("### Mood: 25%")
    st.progress(25)
    
    st.markdown("# Maafin Hendi ya 🥺")
    st.write("")
    st.markdown("<p>Hendi sadar akhir-akhir ini sering banget bikin kamu kesal atau overthinking. Hendi gak mau cari alasan, karena emang Hendi yang salah.</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Lanjut baca 🤍", use_container_width=True):
        st.session_state.tahap = 2
        st.rerun()

# --- TAHAP 2: Pilihan Interaktif & Tombol Ngambek yang Menghindar ---
elif st.session_state.tahap == 2:
    st.markdown("### Mood: 50%")
    st.progress(50)
    
    st.markdown("# Masih ngambek, ya? 🌷")
    st.write("")
    
    # Pesan akan berubah-ubah makin melas kalau tombol ngambek ditekan terus
    teks_gombal = [
        "<p>Kata maaf emang gak langsung bikin semuanya balik normal begitu aja. Tapi Hendi bener-bener tulus pengen belajar jadi lebih baik buat kamu.</p>",
        "<p>Eh, kok masih mau mencet tombol sebelah kanan terus sih? 🥺 Ayo dong dimaafin, gak boleh ngambek lama-lama!</p>",
        "<p>Tombol 'Masih ngambek'-nya gak bisa ditekan buat nolak loh! 😜 Mending pencet tombol kiri yuk, cantik?</p>",
        "<p>Udah dong ngambeknya, Hendi sedih nih kalau kamu cuekin terus... 😭❤️</p>"
    ]
    st.markdown(teks_gombal[min(st.session_state.tingkat_ngambek, 3)], unsafe_allow_html=True)
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iya dimaafin kok 🌸", use_container_width=True):
            st.session_state.tingkat_ngambek = 0
            st.session_state.tahap = 3
            st.rerun()
    with col2:
        # Teks tombol sebelah kanan akan berubah menolak ditekan dan menaikkan tingkat kemalasan teks
        label_tombol = ["Hmm... masih agak kesal 😤", "Yakin nih masih kesal? 😜", "Eits, gak bisa dipencet! 🙈", "Pencet kiri aja plis! 🥺"]
        current_label = label_tombol[min(st.session_state.tingkat_ngambek, 3)]
        
        if st.button(current_label, use_container_width=True):
            st.session_state.tingkat_ngambek += 1
            st.rerun()

# --- TAHAP 3: Janji Hendi ---
elif st.session_state.tahap == 3:
    st.markdown("### Mood: 75%")
    st.progress(75)
    
    st.markdown("# Makasih banyak ya... ✨")
    st.write("")
    st.markdown("<p>Hendi janji bakal pelan-pelan belajar buat ngertiin kamu lebih baik lagi, dan gak ngulangin kesalahan yang sama. Jangan senyum-senyum sendiri ya bacanya! Hehe.</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Satu tahap lagi 🌷", use_container_width=True):
        st.session_state.tahap = 4
        st.rerun()

# --- TAHAP 4: Penutup Manis ---
elif st.session_state.tahap == 4:
    st.markdown("### Mood: 100%")
    st.progress(100)
    
    st.markdown("# Yeay, Selesai! 🥰")
    st.write("")
    st.markdown("<p>Terima kasih ya sudah mau baca curhatan Hendi sampai habis. Semoga setelah ini harimu jauh lebih ceria lagi. Kiriman peluk hangat dari Hendi! 🤗🌸</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Ulangi dari awal 🔄", use_container_width=True):
        st.session_state.tahap = 0
        st.session_state.tingkat_ngambek = 0
        st.rerun()
