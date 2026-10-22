import streamlit as st

# Konfiguracja strony
st.set_page_config(page_title="FlashBet AI - Super Agent 2.0", page_icon="⚽", layout="wide")

st.title("⚽ FlashBet AI – Super Agent Bukmacherski 2.0")
st.markdown("Profesjonalny system analityczny z filtrowaniem pułapek, kalkulacją Value oraz uwzględnianiem sędziego i kontuzji.")

st.divider()

# Zakładki aplikacji
tab1, tab2 = st.tabs(["⚡ Sygnały AI (Typy Dnia)", "🧠 Zaawansowany Warsztat & Kalkulator Value"])

# ==========================================
# ZAKŁADKA 1: SYGNAŁY AI
# ==========================================
with tab1:
    st.subheader("🔥 Dzisiejsze Sygnały o Wysokiej Wartości (Value)")
    
    col_s1, col_s2 = st.columns(2)
    
    with col_s1:
        st.info("### 🇪🇬 Nottingham vs Arsenal\n"
                "* **Szansa AI:** 78%\n"
                "* **Rekomendacja:** Bet Builder (Rożne + Faule)\n"
                "* **Uzasadnienie:** Ominięto niski kurs na czyste rożne. Sędzia wstrzemięźliwy, wysoka intensywność bocznych sektorów.")
    
    with col_s2:
        st.success("### 🇪🇺 Lech Poznań vs Sunderland\n"
                 "* **Szansa AI:** 82% (Pewniak)\n"
                 "* **Rekomendacja:** Poniżej 4.5 bramek\n"
                 "* **Uzasadnienie:** Obie ekipy defensywne w delegacjach/pucharach. Brak absencji w bloku obronnym.")

# ==========================================
# ZAKŁADKA 2: WARSZTAT AGENTA I KALKULATOR
# ==========================================
with tab2:
    st.subheader("🛠️ Panel Precyzyjnej Analizy i Weryfikacji Kursów")
    
    col1, col2 = st.columns(2)
    
    with col1:
        mecz_nazwa = st.text_input("Nazwa spotkania", "np. Real Madryt vs Barcelona")
        szacunek_ai = st.slider("Szacowane przez AI prawdopodobieństwo wejścia (%)", 10, 95, 70)
        kurs_buk = st.number_input("Kurs oferowany przez bukmachera", min_value=1.01, max_value=10.0, value=1.55)
        
    with col2:
        st.markdown("#### ⚖️ Dodatkowe czynniki ryzyka:")
        kontuzje = st.checkbox("⚠️ Brak kluczowego strzelca / obrońcy w jednej z drużyn")
        sędzia_surowy = st.checkbox("🟨 Sędzia z wysoką średnią kartek/fauli")
        derby = st.checkbox("🔥 Mecz derbowy / podwyższone ryzyko remisu")

    if st.button("🚀 Uruchom Audyt Agenta AI", type="primary"):
        # Matematyczne wyliczenie opłacalności (Value)
        implied_probability = (1 / kurs_buk) * 100
        
        # Korekta o czynniki ryzyka
        ostateczna_szansa = szacunek_ai
        if kontuzje:
            ostateczna_szansa -= 8
        if derby:
            ostateczna_szansa -= 10
        if sędzia_surowy and szacunek_ai > 50:
            ostateczna_szansa += 3

        st.divider()
        st.markdown(f"### 📊 Raport Audytu dla: *{mecz_nazwa}*")
        
        # Ocena kursu
        col_res1, col_res2, col_res3 = st.columns(3)
        col_res1.metric("Skorygowana szansa AI", f"{ostateczna_szansa}%")
        col_res2.metric("Szansa bukmachera (z kursu)", f"{implied_probability:.1f}%")
        col_res3.metric("Różnica (Value)", f"+{ostateczna_szansa - implied_probability:.1f}%" if ostateczna_szansa > implied_probability else "Brak Value")

        # Werdykt i filtrowanie pułapek
        if kurs_buk < 1.30:
            st.error("❌ **ODRADZANE:** Kurs poniżej 1.30 to klasyczna pułapka bukmacherska. Nie opłaca się grać tego pojedynczo ani jako 'zapychacz'.")
        elif ostateczna_szansa - implied_probability > 5:
            st.success("✅ **ZNALEZIONO VALUEBET!** Prawdopodobieństwo wyliczone przez model jest wyższe niż wycena bukmachera. Zakład ma sens ekonomiczny.")
        else:
            st.warning("⚠️ **NEUTRALNIE:** Kurs jest uczciwie oszacowany przez rynek. Brak wyraźnej przewagi statystycznej.")
