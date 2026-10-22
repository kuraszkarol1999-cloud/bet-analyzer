import streamlit as st
import requests
from datetime import date

# Konfiguracja strony
st.set_page_config(page_title="FlashBet AI - Live", page_icon="⚽", layout="wide")
st.title("⚽ FlashBet AI – Mecze na Żywo (Baza API)")

# 1. Bezpieczne pobranie klucza z sekretów Streamlit
try:
    API_KEY = st.secrets["API_KEY"]
except KeyError:
    st.error("⚠️ Brak klucza API_KEY w Streamlit Secrets!")
    st.stop()

# 2. Funkcja pobierająca dane z serwerów (z pamięcią cache na 1h, żeby oszczędzać limit 100 zapytań dziennie)
@st.cache_data(ttl=3600)
def pobierz_mecze(data_meczu):
    url = "https://v3.football.api-sports.io/fixtures"
    headers = {
        'x-apisports-key': API_KEY
    }
    querystring = {"date": data_meczu}
    
    try:
        response = requests.get(url, headers=headers, params=querystring)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": str(e)}

# 3. Wywołanie silnika i pobranie dzisiejszych spotkań
dzisiaj = str(date.today())
st.info(f"🔄 Nawiązywanie połączenia z bazą... Pobieram terminarz na dziś ({dzisiaj}).")
dane = pobierz_mecze(dzisiaj)

# 4. Wyświetlanie prawdziwych wyników na ekranie
if "error" in dane:
    st.error(f"❌ Błąd połączenia z API: {dane['error']}")
elif dane.get("results", 0) > 0:
    mecze = dane["response"]
    st.success(f"✅ Zaciągnięto do bazy {len(mecze)} meczów z całego świata!")
    
    st.subheader("📌 Najciekawsze dzisiejsze spotkania na żywo:")
    
    # Wyświetlamy pierwsze 15 meczów, żeby strona działała płynnie
    for mecz in mecze[:15]:
        liga = mecz["league"]["name"]
        kraj = mecz["league"]["country"]
        gospodarz = mecz["teams"]["home"]["name"]
        gosc = mecz["teams"]["away"]["name"]
        status = mecz["fixture"]["status"]["short"]
        
        # Zabezpieczenie na wypadek, gdy mecz się jeszcze nie zaczął (brak goli)
        gole_h = mecz["goals"]["home"] if mecz["goals"]["home"] is not None else "-"
        gole_a = mecz["goals"]["away"] if mecz["goals"]["away"] is not None else "-"
        
        # Interfejs pojedynczego meczu
        with st.container():
            col1, col2, col3 = st.columns([2, 4, 1])
            with col1:
                st.caption(f"🏆 {kraj}: {liga}")
            with col2:
                st.markdown(f"**{gospodarz}** &nbsp;&nbsp; {gole_h} - {gole_a} &nbsp;&nbsp; **{gosc}**")
            with col3:
                st.caption(f"Status: {status}")
            st.divider()
    
    if len(mecze) > 15:
        st
