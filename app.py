import streamlit as st

st.set_page_config(
    page_title="Smart Waste AI",
    page_icon="🌱",
    layout="wide"
)

st.markdown(
    """
    <h1 style='text-align: center;'>🌱 Smart Waste Segregation Assistant</h1>
    <p style='text-align: center; font-size: 18px;'>
        AI-powered solution for responsible waste management
    </p>
    """,
    unsafe_allow_html=True
)

st.write("\n\n")

# CENTERED BUTTON
col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("♻️ Waste Analyser", use_container_width=True):
        st.switch_page("pages/1_Waste_Analysis.py")
