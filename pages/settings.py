import streamlit as st


def show_settings():

    st.title("Settings")

    st.text_input("Company Name")

    st.text_input("Administrator")

    st.selectbox(
        "AI Model",
        [
            "Gemini 2.5 Flash"
        ]
    )

    st.slider(
        "Temperature",
        0.0,
        1.0,
        0.3
    )

    st.button("Save Settings")