import streamlit as st
import requests
from config import config

st.set_page_config(
    page_title="Smart Agriculture System",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Session state ──────────────────────────────────────────────────────────────
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "token" not in st.session_state:
    st.session_state.token = ""
if "user_name" not in st.session_state:
    st.session_state.user_name = ""

# ── Auth helpers ───────────────────────────────────────────────────────────────
def api_post(endpoint, payload):
    try:
        r = requests.post(f"{config.BACKEND_URL}{endpoint}", json=payload, timeout=5)
        return r.json()
    except Exception as e:
        return {"error": str(e)}

# ── Login / Register page ──────────────────────────────────────────────────────
def auth_page():
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown("## 🌾 Smart Agriculture System")
        st.markdown("AI-powered farm management platform")
        tab1, tab2 = st.tabs(["Login", "Register"])

        with tab1:
            with st.form("login_form"):
                email = st.tex
t_input("Email", placeholder="you@example.com")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Login", use_container_width=True)
                if submitted:
                    res = api_post("/auth/login", {"email": email, "password": password})
                    if "access_token" in res:
                        st.session_state.logged_in = True
                        st.session_state.token = res["access_token"]
                        st.session_state.user_name = res.get("name", email)
                        st.success(f"Welcome back, {st.session_state.user_name}!")
                        st.rerun()
                    else:
                        st.error(res.get("detail", "Login failed"))

        with tab2:
            with st.form("register_form"):
                name = st.text_input("Full Name")
                email = st.text_input("Email", placeholder="you@example.com")
                password = st.text_input("Password", type="password")
                submitted = st.form_submit_button("Register", use_container_width=True)
                if submitted:
                    res = api_post("/auth/register", {"name": name, "email": email, "password": password})
                    if "message" in res and "successful" in res["message"]:
                        st.success("Registered! Please login.")
                    else:
                        st.error(res.get("detail", "Registration failed"))

# ── Main dashboard ─────────────────────────────────────────────────────────────
def main_app():
    with st.sidebar:
        st.image("https://img.icons8.com/color/96/farm.png", width=70)
        st.markdown(f"**{st.session_state.user_name}**")
        st.divider()
        page = st.radio("Navigate", [
            "🏠 Dashboard", "🌱 Crop Monitoring", "🪱 Soil Analysis",
            "🌤️ Weather Forecast", "🔬 Disease Detection", "💧 Irrigation",
            "📈 Yield Prediction", "💹 Market Prices", "🐛 Pest Detection", "📄 Reports"
        ])
        st.divider()
        if st.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.token = ""
            st.rerun()

    # Route to pages
    if page == "🏠 Dashboard":
        from frontend.pages.dashboard import show; show()
    elif page == "🌱 Crop Monitoring":
        from frontend.pages.crop_monitoring import show; show()
    elif page == "🪱 Soil Analysis":
        from frontend.pages.soil_analysis import show; show()
    elif page == "🌤️ Weather Forecast":
        from frontend.pages.weather_forecast import show; show()
    elif page == "🔬 Disease Detection":
        from frontend.pages.disease_detection import show; show()
    elif page == "💧 Irrigation":
        from frontend.pages.irrigation_system import show; show()
    elif page == "📈 Yield Prediction":
        from frontend.pages.yield_prediction import show; show()
    elif page == "💹 Market Prices":
        from frontend.pages.market_prediction import show; show()
    elif page == "🐛 Pest Detection":
        from frontend.pages.pest_detection import show; show()
    elif page == "📄 Reports":
        from frontend.pages.reports import show; show()

# ── Entry point ────────────────────────────────────────────────────────────────
if not st.session_state.logged_in:
    auth_page()
else:
    main_app()
