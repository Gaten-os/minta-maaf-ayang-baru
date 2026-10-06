import streamlit as st

# Pengaturan halaman web
st.set_page_config(page_title="Petualangan Hati untuk Ayang", page_icon="🎮", layout="centered")

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

# Inisialisasi status game
if 'level' not in st.session_state:
    st.session_state.level = 1
if 'skor' not in st.session_state:
    st.session_state.skor = 0
if 'nyawa_ngambek' not in st.session_state:
    st.session_state.nyawa_ngambek = 0

# --- LEVEL 1 ---
if st.session_state.level == 1:
    st.markdown("### 🎮 Level 1")
    st.markdown("### Mood Ayang: 0% | Skor: 0")
    st.progress(0)
    
    st.markdown("# Halo Sayang... 🌷")
    st.write("")
    st.markdown("<p>Selamat datang di game spesial buatan Hendi! Di sini, ayang harus menyelesaikan beberapa tantangan sebelum bisa membukakan pintu maaf buat Hendi. Siap berpetualang?</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Siap, Lanjut ke Level 2! 🚀", use_container_width=True):
        st.session_state.skor += 20
        st.session_state.level = 2
        st.rerun()

# --- LEVEL 2 ---
elif st.session_state.level == 2:
    st.markdown("### 🎮 Level 2")
    st.markdown("### Mood Ayang: 20% | Skor: 20")
    st.progress(20)
    
    st.markdown("# Kenapa Hendi Bikin Game Ini? 🤔")
    st.write("")
    st.markdown("<p>Coba tebak, apa alasan utama Hendi bersusah payah bikin web game ini khusus buat ayang?</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Karena Hendi mau minta maaf dengan tulus 🥺", use_container_width=True):
        st.session_state.skor += 20
        st.session_state.level = 3
        st.rerun()
    if st.button("Karena Hendi lagi gabut gak ada kerjaan 😜", use_container_width=True):
        st.warning("Eitss, salah! Hendi serius nih, coba pilih jawaban yang lain ya sayang.")
    if st.button("Karena Hendi kangen berat sama ayang 🤍", use_container_width=True):
        st.session_state.skor += 20
        st.session_state.level = 3
        st.rerun()

# --- LEVEL 3 ---
elif st.session_state.level == 3:
    st.markdown("### 🎮 Level 3")
    st.markdown("### Mood Ayang: 40% | Skor: 40")
    st.progress(40)
    
    st.markdown("# Jujur sama Hendi, masih ngambek kan? 😤")
    st.write("")
    
    pesan_rayuan = [
        "<p>Hendi tahu akhir-akhir ini sering bikin ayang kesal. Tapi jangan ngambek terus dong, nanti cantiknya ilang lho! 🌸</p>",
        "<p>Eh, tombol atasnya masih dipencet juga? 🥺 Ayang mah suka usil banget, padahal Hendi udah melas.</p>",
        "<p>Gak mempan ya tombol atasnya? 😜 Ngaku deh, sebenarnya ayang udah mau dimaafin kan sama Hendi?</p>",
        "<p>Udah dong ngambeknya sayang... Hendi janji bakal jadi jauh lebih baik lagi buat ayang tercinta! ❤️</p>"
    ]
    st.markdown(pesan_rayuan[min(st.session_state.nyawa_ngambek, 3)], unsafe_allow_html=True)
    st.write("")
    
    # Tombol atas (menghindar)
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
    
    # Tombol bawah (jalan keluar)
    if st.button("Iya deh, dimaafin kok sayang ❤️🌸", use_container_width=True):
        st.session_state.skor += 20
        st.session_state.nyawa_ngambek = 0
        st.session_state.level = 4
        st.rerun()

# --- LEVEL 4 ---
elif st.session_state.level == 4:
    st.markdown("### 🎮 Level 4")
    st.markdown("### Mood Ayang: 60% | Skor: 60")
    st.progress(60)
    
    st.markdown("# Pilih Janji Hendi untuk Kedepannya ✨")
    st.write("")
    st.markdown("<p>Sebagai bukti Hendi mau berubah, apa janji yang harus Hendi pegang teguh di depan ayang?</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Lebih sabar, lebih peka, dan gak gampang bikin ayang overthinking 🤍", use_container_width=True):
        st.session_state.skor += 20
        st.session_state.level = 5
        st.rerun()
    if st.button("Sering-sering ngajak jalan dan traktir makanan enak 🍕", use_container_width=True):
        st.session_state.skor += 20
        st.session_state.level = 5
        st.rerun()

# --- LEVEL 5 ---
elif st.session_state.level == 5:
    st.markdown("### 🎮 Level 5")
    st.markdown("### Mood Ayang: 80% | Skor: 80")
    st.progress(80)
    
    st.markdown("# Hore, Sebentar Lagi Menang! 🎁")
    st.write("")
    st.markdown("<p>Ayang hebat banget sudah bertahan sampai level terakhir ini! Tinggal satu langkah lagi buat membuka pesan utama dan pelukan virtual dari Hendi.</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Buka Kotak Kejutan Terakhir 🔓", use_container_width=True):
        st.session_state.skor += 20
        st.session_state.level = 6
        st.rerun()

# --- TAMAT (YOU WIN) ---
elif st.session_state.level == 6:
    st.balloons()
    st.markdown("### 🏆 GAME COMPLETED - 100% SUCCESS!")
    st.markdown("### Mood Ayang: 100% (Full Bahagia!) | Skor Sempurna: 100")
    st.progress(100)
    
    st.markdown("# Selamat, Ayang Menang! 🥰🎉")
    st.write("")
    st.markdown("<p>Terima kasih banyak ya sayang sudah sabar mainin game buatan Hendi dari awal sampai akhir, dan mau memaafkan Hendi. Semoga setelah ini hari-hari ayang dipenuhi senyuman dan kebahagiaan terus. Kiriman peluk dan cium hangat dari Hendi buat ayang tercinta! 🤗🌸</p>", unsafe_allow_html=True)
    st.write("")
    
    if st.button("Mainkan Petualangan Ini dari Awal 🔄", use_container_width=True):
        st.session_state.level = 1
        st.session_state.skor = 0
        st.session_state.nyawa_ngambek = 0
        st.rerun()
