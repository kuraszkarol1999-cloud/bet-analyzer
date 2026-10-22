import streamlit as st

# Konfiguracja - wymuszamy ciemny motyw i szeroki układ
st.set_page_config(page_title="FlashBet AI - Dashboard", layout="wide", initial_sidebar_state="expanded")

# ==========================================
# PANEL BOCZNY (SIDEBAR)
# ==========================================
st.sidebar.title("⚡ FlashBet AI")
st.sidebar.markdown("---")

st.sidebar.caption("STATYSTYCZNE")
menu = st.sidebar.radio("Nawigacja", [
    "📈 Value Bets", 
    "🚩 Rożne", 
    "⚽ Gole", 
    "🟨 Kartki", 
    "⚖️ Sędziowie",
    "🤖 Generator AKO"
])

# ==========================================
# GŁÓWNA STRONA - ZAKŁADKA VALUE BETS
# ==========================================
if menu == "📈 Value Bets":
    # Nagłówek
    col_title, col_btn = st.columns([4, 1])
    with col_title:
        st.header("Value Bets 🚀 +EV")
        st.markdown("Kursy wyższe, niż wynika z historii drużyn. Automatyczne typy oparte na twardych danych.")
    with col_btn:
        st.button("Oblokuj pełny dostęp", type="primary")

    # Filtry
    st.markdown("---")
    col_f1, col_f2, col_f3, col_f4 = st.columns([1, 1, 1, 4])
    col_f1.button("Wczoraj")
    col_f2.button("Dziś", type="primary")
    col_f3.button("Jutro")
    col_f4.text_input("🔍 Szukaj drużyny lub ligi...")
    
    st.subheader("Darmowe typy na dziś")
    st.caption("Trzy najwyższe odchylenia przy kursach 1.50–1.90, cały mecz")

    # Kafelki z meczami (wzorowane na PredictStats)
    c1, c2, c3 = st.columns(3)

    # KAFELEK 1
    with c1:
        with st.container(border=True):
            st.caption("🏆 UEFA Europa League • 18:45")
            st.markdown("### Trabzonspor\n### Heart of Midlothian")
            st.success("🟢 Poniżej 3.5 Bramki")
            
            # Statystyki z dużą czcionką
            st.metric(label="Odchylenie wartości", value="+28,0%", delta="Kurs: 1.73", delta_color="off")
            
            # Paski postępu dla wizualizacji
            st.progress(74, text="74% historycznie (model AI)")
            st.progress(58, text="58% szansa bukmachera (z kursu)")
            
            st.button("Pełna Analiza ➔", key="btn1", use_container_width=True)

    # KAFELEK 2
    with c2:
        with st.container(border=True):
            st.caption("🏆 UEFA Europa League • 21:00")
            st.markdown("### Omonia Nicosia\n### Benfica")
            st.error("🔴 Ponad 3.5 Kartki")
            
            st.metric(label="Odchylenie wartości", value="+27,3%", delta="Kurs: 1.83", delta_color="off")
            
            st.progress(70, text="70% historycznie (model AI)")
            st.progress(55, text="55% szansa bukmachera (z kursu)")
            
            st.button("Pełna Analiza ➔", key="btn2", use_container_width=True)

    # KAFELEK 3
    with c3:
        with st.container(border=True):
            st.caption("🏆 Copa Venezuela • 21:00")
            st.markdown("### Metropolitanos FC\n### Anzoategui FC")
            st.warning("🟠 Poniżej 10.5 Rzuty rożne")
            
            st.metric(label="Odchylenie wartości", value="+26,2%", delta="Kurs: 1.73", delta_color="off")
            
            st.progress(73, text="73% historycznie (model AI)")
            st.progress(58, text="58% szansa bukmachera (z kursu)")
            
            st.button("Pełna Analiza ➔", key="btn3", use_container_width=True)

else:
    st.info(f"Zakładka {menu} jest w budowie. Tutaj pojawią się dedykowane filtry.")
