import streamlit as st

# Pengaturan halaman web
st.set_page_config(page_title="Maafin Hendi Ya Sayang", page_icon="🥺", layout="centered")

# Styling CSS agar mirip tampilan modern & romantis
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom, #ff9a9e, #fecfef);
    }
    h1, h3 {
        color: #fff;
        text-align: center;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.2);
    }
    p {
        color: #590d22;
        font-size: 18px;
        text-align: center;
        background-color: rgba(255, 255, 255, 0.7);
        padding: 15px;
        border-radius: 15px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Inisialisasi status halaman
if 'tahap' not in st.session_state:
    st.session_state.tahap = 0

# --- TAHAP 0: Pembuka ---
if st.session_state.tahap == 0:
    st.markdown("### Hati Kamu: 0%")
    st.progress(0)
    
    st.markdown("# Hi Sayang ❤️")
    st.write("")
    st.markdown("<p>Aku tahu akhir-akhir ini aku banyak bikin hati kecil kamu sedih. Aku cuma minta waktu sebentar buat baca ini.</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Buka Surat 💌", use_container_width=True):
        st.session_state.tahap = 1
        st.rerun()

# --- TAHAP 1: Pengakuan ---
elif st.session_state.tahap == 1:
    st.markdown("### Hati Kamu: 25%")
    st.progress(25)
    
    st.markdown("# Maafin Hendi ya... 🥺")
    st.write("")
    st.markdown("<p>Aku sadar mungkin aku terlalu sering bikin kamu kecewa. Aku gak akan membela diri. Aku cuma mau ngaku kalau aku memang salah.</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Next 🤍", use_container_width=True):
        st.session_state.tahap = 2
        st.rerun()

# --- TAHAP 2: Pertanyaan / Pilihan ---
elif st.session_state.tahap == 2:
    st.markdown("### Hati Kamu: 50%")
    st.progress(50)
    
    st.markdown("# Masih Mau Lanjut? 💔")
    st.write("")
    st.markdown("<p>Aku tahu kata maaf gak langsung menghilangkan rasa kecewa. Tapi aku benar-benar ingin berubah demi kamu.</p>", unsafe_allow_html=True)
    st.write("")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Iya, Lanjut ❤️", use_container_width=True):
            st.session_state.tahap = 3
            st.rerun()
    with col2:
        if st.button("Masih Ngambek 😤", use_container_width=True):
            st.session_state.tahap = 2 # Tetap di situ atau bisa dikustomisasi
            st.rerun()

# --- TAHAP 3: Janji & Harapan ---
elif st.session_state.tahap == 3:
    st.markdown("### Hati Kamu: 75%")
    st.progress(75)
    
    st.markdown("# Sayang... ✨")
    st.write("")
    st.markdown("<p>Aku gak janji bakal langsung sempurna. Tapi aku janji bakal terus belajar supaya gak mengulang kesalahan yang sama. Semoga kamu masih mau kasih aku kesempatan. Aku sayang kamu. Selalu. ❤️</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Aku Janji Berubah 🤍", use_container_width=True):
        st.session_state.tahap = 4
        st.rerun()

# --- TAHAP 4: Penutup / Sukses ---
elif st.session_state.tahap == 4:
    st.balloons()
    st.markdown("### Hati Kamu: 100%")
    st.progress(100)
    
    st.markdown("# Terima Kasih Sayang! 🥰")
    st.write("")
    st.markdown("<p>Terima kasih sudah membaca semuanya. Semoga setelah ini kita bisa sama-sama memperbaiki semuanya. Peluk virtual dari Hendi! 🤗</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Ulangi dari Awal 🔄", use_container_width=True):
        st.session_state.tahap = 0
        st.rerun()
