import streamlit as st

# Set page configuration to wide mode
st.set_page_config(
    page_title="DatNet Mockup - Favoriten", 
    page_icon="★",
    layout="wide"
)

# Custom CSS for a professional DatNet Enterprise look
st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background-color: #f4f7f9;
    }
    
    /* Header Bar */
    .header-style {
        background-color: #2c3e50;
        padding: 20px;
        color: white;
        border-radius: 8px;
        margin-bottom: 25px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    /* Document Row Styling */
    .doc-row {
        background-color: white;
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 10px;
        border: 1px solid #e1e4e8;
        display: flex;
        align-items: center;
    }
    
    /* Custom Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #e1e4e8;
    }
    </style>
    """, unsafe_allow_html=True)

# 1. State Management: Persistence during the session
if 'favorites' not in st.session_state:
    st.session_state.favorites = set()
if 'view' not in st.session_state:
    st.session_state.view = 'all'

# 2. Mock Data (Based on your Screenshots)
documents = [
    {"id": 1, "name": "2026-04-28_Tages-La_Süd.pdf", "size": "1.2 MB", "type": "PDF"},
    {"id": 2, "name": "2026-04-29_Tages-La_Süd.pdf", "size": "4.5 MB", "type": "PDF"},
    {"id": 3, "name": "2026-04-30_Tages-La_Süd.pdf", "size": "0.8 MB", "type": "PDF"},
    {"id": 4, "name": "2026-05-01_Tages-La_Süd.pdf", "size": "2.1 MB", "type": "PDF"},
    {"id": 5, "name": "2026-05-02_Tages-La_Süd.pdf", "size": "3.2 MB", "type": "IMG"},
]

# 3. Header Section
st.markdown('<div class="header-style"><h1>DatNet Dokumentenmanagement</h1></div>', unsafe_allow_html=True)

# 4. Main Navigation (The "Blue Box" Feature)
col1, col2, col3 = st.columns([1, 1, 3])

with col1:
    if st.button("📁 Dokumentbaum", use_container_width=True):
        st.session_state.view = 'all'
with col2:
    if st.button("📁 aktive Dokumente", use_container_width=True):
        st.session_state.view = 'all'
with col3:
    if st.button("📁 inaktive Dokumente", use_container_width=True):
        st.session_state.view = 'all'
with col5:
    # This represents the "Meine Favoriten" button you sketched
    fav_label = f"★ Meine Favoriten ({len(st.session_state.favorites)})"
    if st.button(fav_label, type="primary", use_container_width=True):
        st.session_state.view = 'favs'

st.divider()

# 5. Content Rendering
if st.session_state.view == 'favs':
    st.subheader("⭐ Ihre persönlichen Favoriten")
    display_docs = [d for d in documents if d['id'] in st.session_state.favorites]
else:
    st.subheader("📂 Alle Dokumente (Ordner: Tages-La)")
    display_docs = documents

if not display_docs:
    st.info("Keine Favoriten gefunden. Markieren Sie Dokumente mit dem Stern ★ für den Schnellzugriff.")
else:
    # Table Header
    h_col1, h_col2, h_col3, h_col4 = st.columns([0.5, 4, 1, 1])
    h_col1.write("**Status**")
    h_col2.write("**Dateiname**")
    h_col3.write("**Größe**")
    h_col4.write("**Aktion**")
    
    # Table Rows
    for doc in display_docs:
        is_fav = doc['id'] in st.session_state.favorites
        row_cols = st.columns([0.5, 4, 1, 1])
        
        with row_cols[0]:
            star_icon = "★" if is_fav else "☆"
            if st.button(star_icon, key=f"fav_{doc['id']}"):
                if is_fav:
                    st.session_state.favorites.remove(doc['id'])
                else:
                    st.session_state.favorites.add(doc['id'])
                st.rerun()
                
        with row_cols[1]:
            st.write(doc['name'])
            
        with row_cols[2]:
            st.caption(doc['size'])
            
        with row_cols[3]:
            st.button("Vorschau", key=f"pre_{doc['id']}", use_container_width=True)

# 6. Sidebar (Personal Button Context)
with st.sidebar:
    st.title("Dokumentenmangementsystem")
    st.write("Eingeloggt als: **00_Tages La**")
    st.write("Eingeloggt als: **01_AAT_Ammersee-Altmühltal**")
    st.write("Eingeloggt als: **02_OL_Oberland**")
    st.progress(len(st.session_state.favorites) / len(documents), text="Speicherauslastung Favoriten")
    
    st.divider()
    if st.button("Abmelden"):
        st.toast("Abmeldung erfolgreich")
