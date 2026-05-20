import streamlit as st

# 1. KODE CSS (Taruh di paling atas biar langsung jadi putih)
st.markdown("""
    <style>
    .stApp {
        background-color: white;
    }
    h1, h2, h3, p, span, label, .stMarkdown {
        color: black !important;
    }
    .stNumberInput input, .stSelectbox div {
        color: black !important;
        background-color: #f0f2f6 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. KONFIGURASI HALAMAN
st.title("🍔 Kantin Digital SMK")
st.markdown("---")

# 3. LAYOUT KOLOM
col1, col2 = st.columns([1, 2])

with col1:
    st.image("https://images.unsplash.com/photo-1513104890138-7c749659a591?w=500", caption="Menu Spesial")

with col2:
    menu = st.selectbox("Pilih Menu:", ["Nasi Goreng", "Mie Ayam", "Bakso", "Ayam Geprek"])
    
    # Atur harga otomatis
    if menu == "Nasi Goreng":
        harga_default = 15000
    elif menu == "Mie Ayam":
        harga_default = 12000
    elif menu == "Bakso":
        harga_default = 13000
    else:
        harga_default = 10000

    harga = st.number_input("Harga Satuan (Rp)", value=harga_default)
    jumlah = st.number_input("Beli Berapa Banyak?", min_value=1, value=1)
    
    total = harga * jumlah
    st.subheader(f"Total: Rp {total:,}")

st.markdown("---")

# 4. PEMBAYARAN
bayar = st.number_input("Uang Pembayaran (Rp)", min_value=0, step=500)

if st.button("PROSES TRANSAKSI"):
    kembalian = bayar - total
    
    if kembalian >= 0:
        st.balloons()
        st.success(f"Transaksi Berhasil! Kembalian: Rp {kembalian:,}")
        
        # --- TARUH STRUKNYA DI SINI (Menjorok ke dalam) ---
        st.markdown("---")
        st.subheader("🧾 Struk Belanja kamu")
        st.write(f"**Pesanan:** {menu}")
        st.write(f"**Total Bayar:** Rp {total:,}")
        st.info(f"**Kembalian:** Rp {kembalian:,}")
        # ------------------------------------------------
    else:
        st.error(f"Uang Kurang: Rp {abs(kembalian):,}")