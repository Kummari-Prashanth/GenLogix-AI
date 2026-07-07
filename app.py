import os
import streamlit as st

from config import APP_NAME

# ==========================
# Streamlit Config
# ==========================

st.set_page_config(
    page_title=APP_NAME,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================
# Load CSS
# ==========================

def load_css():
    css_path = "assets/styles.css"
    if os.path.exists(css_path):
        with open(css_path) as f:
            st.markdown(
                f"<style>{f.read()}</style>",
                unsafe_allow_html=True
            )

load_css()

# ==========================
# Import Pages
# ==========================

from pages.dashboard import show_dashboard
from pages.ai_copilot import show_ai_copilot
from pages.transportation import show_transportation
from pages.route_optimizer import show_route_optimizer
from pages.analytics import show_analytics
from pages.risk_prediction import show_risk_prediction
from pages.scenario_simulator import show_scenario
from pages.reports import show_reports
from pages.knowledge_base import show_knowledge_base
from pages.settings import show_settings
from pages.multi_agent import show_multi_agent

# ==========================
# Sidebar
# ==========================

try:
    st.sidebar.image("assets/logo.png", width=170)
except:
    st.sidebar.markdown("# GenLogix AI")

st.sidebar.markdown("## Enterprise Logistics Intelligence Platform")

st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigation",
    [
        "Executive Dashboard",
        "AI Command Center",
        "Multi-Agent Center",
        "Live Transportation",
        "Smart Route Optimizer",
        "Cost Intelligence",
        "AI Risk Prediction",
        "AI Scenario Simulator",
        "AI Reports",
        "Knowledge Hub",
        "Settings"
    ]
)

st.sidebar.markdown("---")

st.sidebar.success("System Online")

st.sidebar.info("""
Version : 2.0

AI Engine : Gemini

Architecture : Multi-Agent AI

Platform : Streamlit
""")

# ==========================
# Routing
# ==========================

if page == "Executive Dashboard":
    show_dashboard()

elif page == "AI Command Center":
    show_ai_copilot()

elif page == "Multi-Agent Center":
    show_multi_agent()

elif page == "Live Transportation":
    show_transportation()

elif page == "Smart Route Optimizer":
    show_route_optimizer()

elif page == "Cost Intelligence":
    show_analytics()

elif page == "AI Risk Prediction":
    show_risk_prediction()

elif page == "AI Scenario Simulator":
    show_scenario()

elif page == "AI Reports":
    show_reports()

elif page == "Knowledge Hub":
    show_knowledge_base()

elif page == "Settings":
    show_settings()

# ==========================
# Footer
# ==========================

st.markdown("---")

st.caption(
    "© 2026 GenLogix AI | "
    "An Autonomous Multi-Agent Generative AI Platform "
    "for Transportation Bottleneck Analysis and Logistics Cost Optimization"
)