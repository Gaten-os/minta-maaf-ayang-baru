import streamlit as st

# Pengaturan halaman web
st.set_page_config(page_title="Mini Game untuk Ayang", page_icon="🎮", layout="centered")

# Styling CSS: Tema game romantis, estetik, & animasi kelopak bunga jatuh
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
        background-color: rgba(255, 255, 255, 0.9);
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

# Inisialisasi status game & tingkat ngambek
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'nyawa_ngambek' not in st.session_state:
    st.session_state.nyawa_ngambek = 0

# --- LEVEL 1: Misi Membuka Game ---
if st.session_state.level == 1:
    st.markdown("### 🎮 Level 1: Misi Dimulai")
    st.markdown("### Mood Ayang: 0%")
    st.progress(0)
    
    st.markdown("# Halo Sayang... 🌷")
    st.write("")
    st.markdown("<p>Selamat datang di mini game buatan Hendi khusus buat ayang! Misi pertama: apakah ayang siap mendengarkan penjelasan Hendi?</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Siap, Mulai Game! 🚀", use_container_width=True):
        st.session_state.level = 2
        st.rerun()

# --- LEVEL 2: Tantangan Pengakuan (Pilih Alasan yang Benar) ---
elif st.session_state.level == 2:
    st.markdown("### 🎮 Level 2: Pertanyaan Kejujuran")
    st.markdown("### Mood Ayang: 25%")
    st.progress(25)
    
    st.markdown("# Kenapa Hendi Bikin Game Ini? 🤔")
    st.write("")
    st.markdown("<p>Pilih jawaban yang paling bener menurut ayang:</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Karena Hendi mau minta maaf secara tulus 🥺", use_container_width=True):
        st.session_state.level = 3
        st.rerun()
    if st.button("Karena Hendi gabut doang 😜", use_container_width=True):
        st.warning("Eitss, bukan itu! Coba pilih jawaban yang lain ya sayang.")
    if st.button("Karena Hendi kangen ayang 🤍", use_container_width=True):
        st.session_state.level = 3
        st.rerun()

# --- LEVEL 3: Tantangan Tombol Menghindar (Ujian Ngambek) ---
elif st.session_state.level == 3:
    st.markdown("### 🎮 Level 3: Ujian Kesabaran")
    st.markdown("### Mood Ayang: 50%")
    st.progress(50)
    
    st.markdown("# Masih Ngambek Sama Hendi? 😤")
    st.write("")
    
    pesan_rayuan = [
        "<p>Hendi tahu akhir-akhir ini bikin ayang kesal. Tapi jangan ngambek terus dong, nanti cantiknya ilang lho! 🌸</p>",
        "<p>Eh, tombol di atas masih dipencet juga? 🥺 Ayang mah suka usil nih, padahal Hendi udah melas banget.</p>",
        "<p>Gak mempan ya tombol atasnya? 😜 Ayo ngaku, sebenarnya ayang udah mau dimaafin kan sama Hendi?</p>",
        "<p>Udah dong ngambeknya sayang... Hendi janji bakal jadi lebih baik lagi buat ayang tercinta! ❤️</p>"
    ]
    st.markdown(pesan_rayuan[min(st.session_state.nyawa_ngambek, 3)], unsafe_allow_html=True)
    st.write("")
    
    # Tombol atas (menghindar/menolak)
    label_pilihan_atas = [
        "Hmm... Masih agak kesal 😤", 
        "Yakin nih masih mau kesal? 😜", 
        "Eitss, tombol atas iseng ya! 🙈", 
        "Pencet tombol bawah aja sayang plis! 🥺"
    ]
    current_text = label_pilihan_atas[min(st.session_state.nyawa_ngambek, 3)]
    
    if st.button(current_text, use_container_width=True):
        st.session_state.nyawa_ngambek += 1
        st.rerun()
        
    st.write("")
    
    # Tombol bawah (jalan keluar game)
    if st.button("Iya deh, dimaafin kok sayang ❤️🌸", use_container_width=True):
        st.session_state.nyawa_ngambek = 0
        st.session_state.level = 4
        st.rerun()

# --- LEVEL 4: Janji & Hadiah Game ---
elif st.session_state.level == 4:
    st.markdown("### 🎮 Level 4: Bonus Rahasia")
    st.markdown("### Mood Ayang: 75%")
    st.progress(75)
    
    st.markdown("# Yeay, Level Berhasil Dilewati! ✨")
    st.write("")
    st.markdown("<p>Hendi janji bakal pelan-pelan belajar buat ngertiin ayang lebih baik lagi, dan gak ngulangin kesalahan yang sama. Terima kasih ya sudah bertahan sampai level ini! Hehe.</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Buka Hadiah Terakhir 🎁", use_container_width=True):
        st.session_state.level = 5
        st.rerun()

# --- LEVEL 5: Menang Game (Selesai) ---
elif st.session_state.level == 5:
    st.balloons()
    st.markdown("### 🏆 GAME COMPLETED!")
    st.markdown("### Mood Ayang: 100% (Full Bahagia!)")
    st.progress(100)
    
    st.markdown("# You Win, Sayang! 🥰🎉")
    st.write("")
    st.markdown("<p>Terima kasih ya sayang sudah main game buatan Hendi dan mau memaafkan Hendi. Semoga hari-hari ayang selalu ceria dan bahagia terus. Kiriman peluk hangat dari Hendi buat ayang! 🤗🌸</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Mainkan Game dari Awal Lagi 🔄", use_container_width=True):
        st.session_state.level = 1
        st.session_state.nyawa_ngambek = 0
        st.rerun()
