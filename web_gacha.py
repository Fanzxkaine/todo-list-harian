import streamlit as st
import random
import time

# 1. SETTING TAMPILAN
st.set_page_config(page_title="Strinova Gacha", page_icon="💫")
st.markdown("""
    <style>
    .stApp { background-color: white; }
    h1, h2, h3, p, label { color: black !important; }
    </style>
    """, unsafe_allow_html=True)

# 2. DATABASE KARAKTER
s_rank = ["Nobunaga", "Michele", "Meredith", "Lawine"]
a_rank = ["Fuchsia", "Kanami", "Celestia", "Eika", "Flavia"]
b_rank = ["Kokona", "Yugiri", "Baimo", "Maddelena"]

st.title("💫 Strinova Gacha Simulator")

def pull():
    persentase = random.randint(1, 100)
    if persentase <= 5:
        return random.choice(s_rank), "S-RANK ✨", "#D4AF37" 
    elif persentase <= 20:
        return random.choice(a_rank), "A-RANK 💜", "#A020F0" 
    else:
        return random.choice(b_rank), "B-RANK 💙", "#1E90FF"

# 3. TOMBOL GACHA
col1, col2 = st.columns(2)

with col1:
    if st.button("🚀 Single Pull (1x)"):
        char, rarity, warna = pull()
        st.write("Nge-pull...")
        time.sleep(0.5)
        st.markdown(f"<div style='color: {warna}; font-size: 30px; font-weight: bold;'>{char}</div>", unsafe_allow_html=True)
        st.write(f"Rarity: {rarity}")
        
        if "S-RANK" in rarity:
            st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJueGZ3bmZ3bmZ3bmZ3/3o7TKMGpxxcaNnU5vG/giphy.gif")
            st.snow()
            st.warning("✨ JACKPOT! S-RANK IS REAL! ✨")

with col2:
    if st.button("🔥 Multi Pull (10x)"):
        st.write("Hasil 10 Pull:")
        results = [pull() for _ in range(10)]
        for char, rarity, warna in results:
            st.markdown(f"<div style='color: {warna}; font-weight: bold;'>● {char} ({rarity})</div>", unsafe_allow_html=True)
        
        if any("S-RANK" in r[1] for r in results):
            st.image("https://tenor.com/id/view/michele-michelle-michele-lee-michelle-lee-strinova-gif-11505481409987885158")
            st.snow()
            st.warning("✨ GELOOO LU DAPET EMAS JIR ! ✨")