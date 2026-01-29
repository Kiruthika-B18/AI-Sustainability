import streamlit as st
from utils import analyze_waste



st.title("🗑️ Waste Analysis")

st.markdown("""
Enter a waste item and let the AI analyze its sustainability properties.
""")

# Center the entire analyzer
left, center, right = st.columns([1, 2, 1])

with center:
    st.subheader("🔍 Waste Analyzer")

    waste_item = st.text_input(
        "✍️ Enter waste item (e.g., plastic bottle, banana peel, paper, battery):"
    )

    # ---- CENTER THE BUTTON ----
    btn_left, btn_center, btn_right = st.columns([1, 1, 1])

    with btn_left:
        analyze_clicked = st.button("🔍 Analyze Waste", use_container_width=True)

    if analyze_clicked:
        if waste_item.strip() == "":
            st.warning("⚠️ Please enter a waste item.")
        else:
            result = analyze_waste(waste_item)

            st.success("✅ Analysis Complete")

            st.metric("🧪 Waste Type", result["type"])
            st.metric("🌱 Degradable", result["degradable"])
            st.metric("♻️ Reusable / Recyclable", result["recyclable"])
            st.metric("🚮 Disposal Method", result["disposal"])

            st.info(f"🌍 Environmental Impact: {result['impact']}")
